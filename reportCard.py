# Imports
import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
from playwright.sync_api import Page
from telegramBot import send_photo, send_text

# Config
load_dotenv()

USERNAME = os.getenv("SUFO_USERNAME")
PASSWORD = os.getenv("SUFO_PASSWORD")


def reportCard():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        # Login to myStudent
        myStudentLogin(page, USERNAME, PASSWORD)

        # Go to result
        page.goto("https://mystudent.uitm.edu.my/result")
        page.wait_for_timeout(5000)
        print("Navigated to Results page")

        # Screenshot and save
        page.screenshot(path="result.png", full_page=True)
        print("Screenshot saved")

        # Send to Telegram
        send_text("Your UiTM results are ready!")
        send_photo("result.png", caption="Keputusan Peperiksaan")
        browser.close()


def myStudentLogin(page: Page, username: str, password: str):
    page.goto("https://mystudent.uitm.edu.my/login")
    page.fill("#username", username)
    page.fill("#password", password)

    with page.expect_navigation():
        page.click("button[type='submit']")

    print("Logged into myStudent")


if __name__ == "__main__":
    reportCard()
