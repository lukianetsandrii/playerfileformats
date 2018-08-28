import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import locators
import drivers


class Actions(drivers.Driver):

    def isObjectPresent(self, driver, object):
        if WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, object))).is_displayed():
            return True
        else:
            return False

    def isObjectExists(self, driver, object):
        objects_list = driver.find_elements_by_id(object)
        assert len(objects_list) < 1

        # if len(objects_list) < 1:
        #     return True
        # else:
        #     return False

    def getText(self, driver, locator):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, locator)))
        result_text = driver.find_element_by_id(locator).text

        return result_text

    def clickButton(self, driver, button):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, button)))
        some_button = driver.find_element_by_id(button)
        some_button.click()

    def clickButtonXP(self, driver, button):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, button)))
        some_button = driver.find_element_by_xpath(button)
        some_button.click()

    def swipeToLeft(self, driver):
        driver.swipe(700, 500, 10, 500, 500)

    def swipeToRight(self, driver):
        driver.swipe(10, 500, 800, 500, 400)

    def selectRegion(self, driver):
        driver.swipe(540, 960, 10, 500, 1500)

    # def getActualRegion(self, driver):
    #     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, MainLocators.MAIN_PAGE_MY_REGION)))
    #     actual_region = driver.find_element_by_id(MainLocators.MAIN_PAGE_MY_REGION)
    #     actual_region_text = actual_region.text
    #
    #     return actual_region_text
    #
    # def pass_introduction(self, driver):
    #     self.clickButton(driver, IntroLocators.INTRO_PAGE_SHOW_BUTTON)
    #     time.sleep(1)
    #     self.swipeToLeft(driver)
    #     time.sleep(1)
    #     self.swipeToLeft(driver)
    #     time.sleep(1)
    #     self.swipeToLeft(driver)
    #
    # def enable_geolocation_button(self, driver):
    #     self.clickButton(driver, IntroLocators.INTRO_PAGE_START_BUTTON)
    #
    #     if WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located((By.ID, IntroLocators.INTRO_PAGE_ALLOW_PERMISSIONS))):
    #         allow_permissions = driver.find_element_by_id(IntroLocators.INTRO_PAGE_ALLOW_PERMISSIONS)
    #
    #         if allow_permissions.is_displayed():
    #             allow_permissions.click()
    #
    #             confirm_allow_permissions = driver.find_elements_by_id(
    #                 IntroLocators.INTRO_PAGE_CONFIRM_ALLOW_PERMISSIONS)
    #
    #             if len(confirm_allow_permissions) != 0:
    #                 confirm_allow_permissions[0].click()
    #             else:
    #                  print('Test OK')
    #         else:
    #             print('Test OK')