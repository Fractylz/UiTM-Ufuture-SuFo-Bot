from playwright.sync_api import sync_playwright
from loginScript import login
from lectEvalBot import fill_sufo_form
from goToSufo import go_to_sufo
from processSufoTable import process_sufo_rows
import os
from dotenv import load_dotenv
import threading
from playwright.sync_api import Page
from ExitEvalScript import fill_exit_form

# Config
load_dotenv()

USERNAME = os.getenv("SUFO_USERNAME")
PASSWORD = os.getenv("SUFO_PASSWORD")


def exitSurvey():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Login
        login(page, USERNAME, PASSWORD)

        # Go to Exit Survey Page
        go_to_exit(page)

        # Iterate through all rows for each course and process "Click to Answer"
        process_exit_survey_rows(page, fill_sufo_form)

        print("All Evaluations Done")
        browser.close()


def go_to_exit(page: Page):

    page.click("li > a:has-text('Evaluation')")
    page.click("li > a:has-text('Entrance / Exit Survey')")

    page.wait_for_load_state("networkidle")

    print("Navigated to Exit Survey Page")


def process_exit_survey_rows(page, fill_sufo_form):

    # Iterating through all the rows
    while True:
        rows = page.locator("table tbody tr")
        row_count = rows.count()

        processed_one = False

        for i in range(row_count):
            rows = page.locator("table tbody tr")
            row = rows.nth(i)

            # Get status column
            status_cell = row.locator("td").nth(3)
            status_text = status_cell.inner_text().strip().lower()

            print(f"Row {i} status: {status_text}")

            if "completed" in status_text:
                print(f"Row {i}: Already completed. Skipping.")
                continue

            if "not taken yet" not in status_text:
                print(f"Row {i}: Unknown status. Skipping.")
                continue

            # Start Evaluation

            start_btn = row.locator("a:has-text('Click To Answer')")
            start_btn.wait_for(state="visible", timeout=5000)
            start_btn.click()

            page.wait_for_load_state("networkidle")

            # Fill form

            fill_exit_form(page)

            page.wait_for_load_state("networkidle")

            processed_one = True
            break

        if not processed_one:
            print("No more pending evaluations")
            break


if __name__ == "__main__":
    exitSurvey()
