import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from appium.webdriver.common.touch_action import TouchAction

from locators import Locators

import drivers


class Actions(drivers.Driver):

    def isObjectExistsID(self, driver, object):
        objects_list = driver.find_elements_by_id(object)

        if len(objects_list) < 1:
            return False
        elif len(objects_list) > 1:
            return False
        else:
            return True

    def getTextID(self, driver, locator):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, locator)))
        result_text = driver.find_element_by_id(locator).text

        return result_text

    def getTextXP(self, driver, locator):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, locator)))
        result_text = driver.find_element_by_xpath(locator).text

        return result_text

    def getFewTextsID(self, driver, locator):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, locator)))
        elements_list = driver.find_elements_by_id(locator)
        texts_list = []
        for element in elements_list:
            text = element.text
            texts_list.append(text)
        return texts_list

    def clickButtonID(self, driver, button):
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

    def is3DBacklightOn(self):
        is_on = False
        backlight_3d_int = int(os.popen('adb shell cat /sys/class/leds/LM36923H-BL/brightness').read())
        backlight_2d_int = int(os.popen('adb shell cat /sys/class/leds/lcd-backlight/brightness').read())
        if (backlight_2d_int < backlight_3d_int):
            is_on = True
        return is_on

    def fill_field_id(self, driver):
        atime = str(time.clock())
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Locators.POPUP_FIELD_XP)))
        field = driver.find_element_by_xpath(Locators.POPUP_FIELD_XP)
        field.send_keys(Locators.FOLDER_NAME_TEXT + atime)

    def version_text(self, driver):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, Locators.VERSION_TEXT)))
        textik = driver.find_element_by_id(Locators.VERSION_TEXT).text
        version_text = textik[:8]

        return version_text

    def count_of_selected_on_the_screen(self, driver):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, Locators.IS_SELECTED_FILE_ID)))
        elements_list = driver.find_elements_by_id(Locators.IS_SELECTED_FILE_ID)

        return len(elements_list)

    def longtap(self, driver, element):
        actions = TouchAction(driver)
        el = driver.find_element_by_xpath(element)
        actions.long_press(el)
        actions.perform()

    def count_of_all_selected(self, driver):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, Locators.PAGE_TITLE_ID)))
        page_title = driver.find_element_by_id(Locators.PAGE_TITLE_ID).text
        amount = int(page_title.split(' ', 1)[0])

        return amount


