def process_sufo_rows(page, fill_sufo_form):

    while True:
        rows = page.locator("table tbody tr")
        row_count = rows.count()

        processed_one = False

        for i in range(row_count):
            rows = page.locator("table tbody tr")  # re-fetch every loop
            row = rows.nth(i)

            # --- Get Status Column ---
            # Change nth(3) if your status column is different
            status_cell = row.locator("td").nth(4)
            status_text = status_cell.inner_text().strip().lower()

            print(f"Row {i} status: {status_text}")

            # Skip completed rows
            if "completed" in status_text:
                print(f"Row {i}: Already completed. Skipping.")
                continue

            if "not yet taken" not in status_text:
                print(f"Row {i}: Unknown status. Skipping.")
                continue

            # --- Select Lecturer ---
            dropdown = row.locator("select")
            if dropdown.count() == 0:
                print(f"Row {i}: No dropdown found.")
                continue

            dropdown.wait_for(state="visible")

            options = dropdown.locator("option").all_text_contents()

            lecturer_selected = False
            for opt_text in options:
                if opt_text not in ["Choose your lecturer", "Not listed"]:
                    dropdown.select_option(label=opt_text)
                    lecturer_selected = True
                    break

            if not lecturer_selected:
                print(f"Row {i}: No valid lecturer found.")
                continue

            # --- Submit Lecturer ---
            submit_btn = row.locator("button:has-text('Submit')")
            submit_btn.wait_for(state="visible", timeout=5000)
            submit_btn.click()

            page.wait_for_load_state("networkidle")

            # Re-fetch row after reload
            rows = page.locator("table tbody tr")
            row = rows.nth(i)

            # --- Click Start Evaluation ---
            start_btn = row.locator("a:has-text('Evaluate')")
            start_btn.wait_for(state="visible", timeout=5000)
            start_btn.click()

            page.wait_for_load_state("networkidle")

            start_btn = page.locator("a:has-text('Start Evaluation')")
            start_btn.wait_for(state="visible", timeout=5000)
            start_btn.click()

            page.wait_for_load_state("networkidle")

            # --- Fill Form ---
            fill_sufo_form(page)

            # Return to table
            page.wait_for_load_state("networkidle")

            processed_one = True
            break

        if not processed_one:
            print("No more pending evaluations.")
            break
