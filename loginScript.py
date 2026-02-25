from playwright.sync_api import Page


def login(page: Page, username: str, password: str):
    page.goto("https://ufuture.uitm.edu.my/login")

    page.check("#studCheckbox")

    page.fill("#usernameInput", username)
    page.fill("#pswrdInput", password)

    page.click("button[type='submit']")

    page.wait_for_load_state("networkidle")

    print("Logged into UFuture")
