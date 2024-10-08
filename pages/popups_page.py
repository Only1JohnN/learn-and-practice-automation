# pages/popups_page.py
import traceback
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoAlertPresentException
from pages.basepage import BasePage
from utils.screenshot import take_screenshot
from utils.logger import setup_logger

logger = setup_logger()
logger.info("Test started")

class PopupsPage(BasePage):
    ALERT_POPUP = (By.XPATH, "//b[normalize-space()='Alert Popup']")
    CONFIRM_POPUP = (By.XPATH, "//b[normalize-space()='Confirm Popup']")
    CONFIRM_POPUP_RESULT = (By.ID, "confirmResult")
    PROMPT_POPUP = (By.ID, "prompt")
    PROMPT_POPUP_RESULT = (By.ID, "promptResult")
    CLICK_ME_TO_SEE_A_TOOLTIP = (By.CLASS_NAME, "tooltip_1")
    CLICK_ME_TO_SEE_A_TOOLTIP_RESULT = (By.ID, "myTooltip")
    
    def _click_popup(self, locator, screenshot_name):
        try:
            self.wait_for_element_clickable(locator)
            self.click(locator)
        except TimeoutException:
            logger.error(f"Element {locator} not found or not clickable within timeout")
            take_screenshot(self.driver, folder='screenshots', filename=screenshot_name)
        except NoSuchElementException:
            logger.error(f"Element {locator} not found on the page")
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            traceback.print_exc()
    
    def alert_popup(self):
        self._click_popup(self.ALERT_POPUP, 'alert_popup')

    def confirm_popup(self):
        self._click_popup(self.CONFIRM_POPUP, 'confirm_popup')

    def prompt_popup(self):
        self._click_popup(self.PROMPT_POPUP, 'prompt_popup')
            
    def tooltip(self):
        self._click_popup(self.CLICK_ME_TO_SEE_A_TOOLTIP, 'tooltip_popup')
