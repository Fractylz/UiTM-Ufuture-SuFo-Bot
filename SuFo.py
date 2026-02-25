from playwright.sync_api import sync_playwright
from loginScript import login
from lectEvalBot import fill_sufo_form
from goToSufo import go_to_sufo
from processSufoTable import process_sufo_rows
import os
from dotenv import load_dotenv
import threading

# Config
load_dotenv()

USERNAME = os.getenv("SUFO_USERNAME")
PASSWORD = os.getenv("SUFO_PASSWORD")


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Login
        login(page, USERNAME, PASSWORD)

        # Go to SuFo page from Sidebar
        go_to_sufo(page)

        # Process all rows and fill corresponding forms
        process_sufo_rows(page, fill_sufo_form)

        print("All Lecturers Done")
        browser.close()


if __name__ == "__main__":
    main()
