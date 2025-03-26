# pytest --headed
# pytest .\tests\test_dice.py --headed
import re
from playwright.sync_api import Page, expect
from dotenv import load_dotenv
from pages.login_dice_page import LoginPage
from pages.profile_page import ProfilePage
import os
import pytest

load_dotenv()   

DICE_URL = os.getenv("DICE_URL")
DICE_USERNAME = os.getenv("DICE_USERNAME")
DICE_PASSWORD = os.getenv("DICE_PASSWORD")

@pytest.fixture(scope="session")
def auth_page(page: Page):
    # Navigate to login page
    page.goto(f"{DICE_URL}/dashboard/login")
    
    # Perform login using the LoginPage POM
    login_page = LoginPage(page)
    login_page.login(DICE_USERNAME, DICE_PASSWORD)
    
    # Verify successful login
    expect(page).to_have_url(re.compile("home-feed"))
    
    # Return the authenticated page object
    return page

def test_login(auth_page: Page):
    # The login is already done in the fixture
    expect(auth_page).to_have_url(re.compile("home-feed"))

def test_go_to_profile(auth_page: Page):
    auth_page.goto(f"{DICE_URL}/dashboard/profiles")
    expect(auth_page).to_have_title("Profile | Dice.com")
    
def test_upload_resume(auth_page: Page):
    profile_page = ProfilePage(auth_page)
    profile_page.upload_resume()
    # Add verification steps here
    file_selector_by_date = profile_page.file_selector_by_date()
    expect(auth_page.get_by_text(f"{file_selector_by_date['name']}DownloadUploaded to")).to_be_visible()
   



    
