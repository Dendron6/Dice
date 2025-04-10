from playwright.sync_api import Page
import datetime
import random

class ProfilePage:
    def __init__(self, page: Page):
        self.page = page
        # Update locator to find the hidden file input
        self.upload_button = page.get_by_role("button", name="Upload new resume")
        self.no_button = page.get_by_role("button", name="No")
        self.close_button = page.get_by_role("button", name="Close")
        
        # Set a fixed seed for random number generation
        
        day = int(datetime.date.today().strftime("%d"))
        random.seed(day)  # Any number will do

        
    def file_selector_by_random(self)->dict:
        random_number = random.randint(1, 6)
        if random_number == 1 or random_number == 6:
            return {'path':'C:/Users/denis/pythonPW/Dice/docs/Ext2025.pdf', 'name':'Ext2025.pdf'}
        elif random_number == 2 or random_number == 5:
            return {'path':'C:/Users/denis/pythonPW/Dice/docs/Cuc2025.pdf', 'name':'Cuc2025.pdf'}
        else:
            return {'path':'C:/Users/denis/pythonPW/Dice/docs/Res2025.pdf', 'name':'Res2025.pdf'}

    def upload_resume(self) -> dict:
        # Get the absolute path to the PDF file using a fixed random number
        pdf_path = self.file_selector_by_random()
        print(f"PDF Path: {pdf_path['path']}")  # Print the file path for debugging
        
        # Wait for file chooser before clicking the button
        with self.page.expect_file_chooser() as fc_info: 
            self.upload_button.click()
            file_chooser = fc_info.value
            file_chooser.set_files(pdf_path['path'])
        
        self.page.get_by_role("button", name="No").click()
        self.page.wait_for_timeout(1000)
        self.page.get_by_role("button", name="Close").nth(1).click()
        
        # Return the file information so the test can use it for verification
        return pdf_path
        
  
