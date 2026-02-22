def process_sufo_rows(page, fill_sufo_form):

    rows = page.locator("table tbody tr")
    row_count = rows.count()

    for i in range(row_count):
        row = rows.nth(i)

        # Locate lecturer dropdown
        dropdown = row.locator("select")
        dropdown.wait_for(state="visible")

        # Get all options
        options = dropdown.locator("option").all_text_contents()

        # Pick first valid lecturer (skip placeholders)
        lecturer_selected = False
        for opt_text in options:
            if opt_text not in ["Choose your lecturer", "Not listed"]:
                dropdown.select_option(label=opt_text)
                lecturer_selected = True
                break

        if not lecturer_selected:
            print(f"Row {i}: No valid lecturer found, skipping")
            continue

        # Click submit button
        submit_btn = row.locator("button:has-text('Submit')")
        submit_btn.wait_for(state="visible", timeout=5000)
        submit_btn.click()

        # Wait for table to reload
        page.wait_for_load_state("networkidle")

        # Re-locate row after reload
        rows = page.locator("table tbody tr")
        row = rows.nth(i)

        # Click the Evaluate button
        evaluate_btn = row.locator("a:has-text('Evaluate')")
        evaluate_btn.wait_for(state="visible", timeout=5000)
        evaluate_btn.click()

        page.wait_for_load_state("networkidle")

        start_btn = page.locator("a:has-text('Start Evaluation')")
        start_btn.wait_for(state="visible", timeout=5000)
        start_btn.click()

        page.wait_for_load_state("networkidle")

        fill_sufo_form(page)

        # Return to SUFO table page
        page.go_back()
        page.wait_for_load_state("networkidle")
