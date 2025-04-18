# Dice.com Resume Automation

Automated tests for uploading resumes to Dice.com using Playwright and Python.

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Install Playwright browsers:
   ```
   playwright install
   ```

3. Create a `.env` file with your credentials:
   ```
   DICE_URL=https://www.dice.com
   DICE_USERNAME=your_username
   DICE_PASSWORD=your_password
   ```

## Running Tests

Run tests in headless mode (default):
```
pytest tests/test_dice.py
```

Run tests with browser visible:
```
pytest tests/test_dice.py --headed
```

Run tests with visible browser and console output:
```
pytest tests/test_dice.py --headed -s
```

## before pushing to github

ruff check .
ruff check --fix .

