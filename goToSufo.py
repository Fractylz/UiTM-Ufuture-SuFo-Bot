from playwright.sync_api import Page


def go_to_sufo(page: Page):

    page.click("li > a:has-text('Evaluation')")
    page.click("li > a:has-text('SuFo')")

    page.wait_for_load_state("networkidle")

    print("Navigated to SUFO page")
