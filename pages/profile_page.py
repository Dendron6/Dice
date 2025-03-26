from playwright.sync_api import Page
import os
import datetime

class ProfilePage:
    def __init__(self, page: Page):
        self.page = page
        # Update locator to find the hidden file input
        self.upload_button = page.get_by_role("button", name="Upload new resume")
        self.no_button = page.get_by_role("button", name="No")
        self.close_button = page.get_by_role("button", name="Close")
        
    def file_selector_by_date(self)->dict:
        # Get today's date
        current_date = datetime.date.today()
        # Format the date to get only the day
        day_only = int(current_date.strftime("%d"))
        if day_only % 2 == 0:
            return {'path':'C:/Users/denis/pythonPW/Dice/docs/Ext2025.pdf', 'name':'Ext2025.pdf'}
        else:
            return {'path':'C:/Users/denis/pythonPW/Dice/docs/Res2025.pdf', 'name':'Res2025.pdf'}

    def upload_resume(self) -> None:
        # Get the absolute path to the PDF file using a relative path
        pdf_path = self.file_selector_by_date()
        print(f"PDF Path: {pdf_path['path']}")  # Print the file path for debugging
        # Wait for file chooser before clicking the button
        with self.page.expect_file_chooser() as fc_info: 
            self.upload_button.click()
            file_chooser = fc_info.value
            file_chooser.set_files(pdf_path['path'])
        self.page.get_by_role("button", name="No").click()
        self.page.wait_for_timeout(1000)
        self.page.get_by_role("button", name="Close").nth(1).click()
        # self.close_button.click()
        # self.no_button.click()
        
        
        # Handle any confirmation dialogs if they appear
        
      
        
  
