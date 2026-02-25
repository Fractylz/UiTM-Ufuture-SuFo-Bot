def fill_exit_form(page):

    # Get all unique radio group names
    radio_buttons = page.locator("input[type='radio']")
    count = radio_buttons.count()

    names = set()

    for i in range(count):
        name = radio_buttons.nth(i).get_attribute("name")
        if name:
            names.add(name)

    print(f"Found {len(names)} radio groups")

    # For each group, select one option
    for name in names:
        group = page.locator(f"input[type='radio'][name='{name}']")
        group.nth(3).check()  # choose 4th option (index 3)

    # Submit
    submit_btn = page.locator("button:has-text('Submit')")
    submit_btn.click()

    page.wait_for_load_state("networkidle")
    print("Form submitted")
