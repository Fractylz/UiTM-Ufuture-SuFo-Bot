# SUFO Bot

A Python automation bot using **Playwright** to fill out SuFO evaluation forms on UiTM’s uFuture portal.  

## 📝 Features

- Automates login to the UiTM uFuture portal.
- Navigates to **Evaluation → SuFO**.
- Selects a lecturer for each course row.
- Submits the lecturer selection.
- Clicks **Evaluate → Start Evaluation** for each course.
- Fills out SuFO forms with **randomized answers** or **values from 1-4**
- Supports multiple forms in one run.

## 📂 Project Structure
SuFo Bot/
│
├── main.py # Main script to run the bot
├── loginScript.py # Handles login functionality
├── goToSufo.py # Navigates to the SuFO page
├── lectEvalBot.py # Form filling logic
├── .venv/ # Python virtual environment (ignored in Git)
├── .gitignore # Ignore unnecessary files & credentials
├── README.md # Project documentation
└── requirements.txt # Python dependencies


---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/sufo-bot.git
cd sufo-bot

# Windows
python -m venv .venv
.venv\Scripts\activate

# Mac/Linux
python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

playwright install