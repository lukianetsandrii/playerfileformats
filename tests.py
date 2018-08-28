import time

from locators import Locators as locators
from actions import Actions as actions
from drivers import Driver as driver


class TestPlayDiffMediaTypes(driver, actions):

    def test_media_files_types(self, driver):
        actions.clickButtonXP(self, driver, locators.MENU_BUTTON_XP)
        actions.clickButtonXP(self, driver, locators.SD_CARD_BUTTON_XP)
        actions.clickButtonXP(self, driver, locators.TEST_FOLDER_BUTTON_XP)
        actions.clickButtonXP(self, driver, locators.VIDEOS_FOLDER_BUTTON_XP)

        # Test *.mp4 is playing
        actions.clickButtonXP(self, driver, locators.MP4_FILE_XP)
        time.sleep(1)
        driver.tap([(150, 150)])
        start_time = actions.getText(self, driver, locators.TIME_POSITION)
        time.sleep(3)
        end_time = actions.getText(self, driver, locators.TIME_POSITION)
        assert start_time != end_time
        driver.press_keycode(4)

        # Test *.mkv is playing
        actions.clickButtonXP(self, driver, locators.MKV_FILE_XP)
        time.sleep(1)
        driver.tap([(150, 150)])
        start_time = actions.getText(self, driver, locators.TIME_POSITION)
        time.sleep(3)
        end_time = actions.getText(self, driver, locators.TIME_POSITION)
        assert start_time != end_time
        driver.press_keycode(4)

        # Test *.3gp is playing
        actions.clickButtonXP(self, driver, locators.GP3_FILE_XP)
        time.sleep(1)
        driver.tap([(150, 150)])
        start_time = actions.getText(self, driver, locators.TIME_POSITION)
        time.sleep(3)
        end_time = actions.getText(self, driver, locators.TIME_POSITION)
        assert start_time != end_time

        driver.press_keycode(4)
        time.sleep(1)
        driver.press_keycode(4)
        actions.clickButtonXP(self, driver, locators.PICTURES_FOLDER_BUTTON_XP)

        # Test *.jpg is playing
        actions.clickButtonXP(self, driver, locators.JPEG_FILE_XP)
        time.sleep(1)
        driver.tap([(150, 150)])
        file_name = actions.getText(self, driver, locators.PICTURE_NAME_ID)
        assert file_name == 'jpg_test'

        driver.press_keycode(4)

        # Test *.png is playing
        actions.clickButtonXP(self, driver, locators.PNG_FILE_XP)
        time.sleep(1)
        driver.tap([(150, 150)])
        file_name = actions.getText(self, driver, locators.PICTURE_NAME_ID)
        assert file_name == 'png_test'

        driver.press_keycode(4)

        # Test *.webp is playing
        actions.clickButtonXP(self, driver, locators.WEBP_FILE_XP)
        time.sleep(1)
        driver.tap([(150, 150)])
        file_name = actions.getText(self, driver, locators.PICTURE_NAME_ID)
        assert file_name == 'webp_test'
