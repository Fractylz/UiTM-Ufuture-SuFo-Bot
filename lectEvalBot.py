from playwright.sync_api import Page
import random


def fill_sufo_form(page):

    # Locate all radio groups
    radio_groups = page.locator("input[type='radio']")
    group_count = radio_groups.count()

    # Uncomment below to choose specific values for every row
    for i in range(0, group_count, 4):

        option_to_select = i + 2
        radio_groups.nth(option_to_select).check()

    # Uncomment below to appply random values for each row
    # for i in range(0, group_count, 4):

    #     option_to_select = i + random.randint(
    #         1, 4
    #     )
    #     radio_groups.nth(option_to_select).check()

    # Submit the form
    submit_btn = page.locator("button:has-text('Submit')")
    submit_btn.click()
    page.wait_for_load_state("networkidle")
    print("Form submitted")
