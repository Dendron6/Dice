import os
import sys
from pathlib import Path
import pytest
from playwright.sync_api import expect, Browser

# Get the absolute path of the project root directory
project_root = Path(__file__).parent
src_path = project_root / "src"

# Add the src directory to the Python path
sys.path.insert(0, str(src_path))

# Configure default timeout values
# @pytest.fixture(scope="session")
# def browser_context_args(browser_context_args):
#     # Check if running in CI environment
#     if os.environ.get('CI') or os.environ.get('JENKINS_URL'):
#         return {
#             **browser_context_args,
#             "viewport": {"width": 1920, "height": 1080},
#             "headless": True,  # Force headless in CI
#         }
#     return {
#         **browser_context_args,
#         "viewport": {"width": 1920, "height": 1080},
#     }

@pytest.fixture(scope="session")
def context(browser: Browser, browser_context_args):
    context = browser.new_context(**browser_context_args)
    yield context
    context.close()

@pytest.fixture(scope="session")
def page(context):
    page = context.new_page()
    page.set_default_timeout(30000)  # Default timeout for all Playwright actions (30 seconds)
    expect.set_options(timeout=30000)  # Default timeout for all expect assertions (30 seconds)
    yield page
    page.close() 