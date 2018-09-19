import time

from locators import Locators
from actions import Actions
from drivers import Driver as driver


class TestPlayDiffMediaTypes(driver, Actions):

    def test_media_files_types(self, driver):

        #TODO to hadle permissions
        if Actions.isObjectExistsID(self, driver, Locators.ALLOW_ACCESS_BUTTON_ID) == True:
            Actions.clickButtonID(self, driver, Locators.ALLOW_ACCESS_BUTTON_ID)

        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.SD_CARD_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.TEST_FOLDER_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.VIDEOS_FOLDER_BUTTON_XP)

        # Test *.mp4 is playing
        Actions.clickButtonXP(self, driver, Locators.MP4_FILE_XP)
        time.sleep(1)
        driver.tap([(150, 150)])
        start_time = Actions.getTextID(self, driver, Locators.TIME_POSITION_ID)
        time.sleep(3)
        end_time = Actions.getTextID(self, driver, Locators.TIME_POSITION_ID)
        assert start_time != end_time
        driver.press_keycode(4)

        # Test *.mkv is playing
        Actions.clickButtonXP(self, driver, Locators.MKV_FILE_XP)
        time.sleep(1)
        driver.tap([(150, 150)])
        start_time = Actions.getTextID(self, driver, Locators.TIME_POSITION_ID)
        time.sleep(3)
        end_time = Actions.getTextID(self, driver, Locators.TIME_POSITION_ID)
        assert start_time != end_time
        driver.press_keycode(4)

        # Test *.3gp is playing
        Actions.clickButtonXP(self, driver, Locators.GP3_FILE_XP)
        time.sleep(1)
        driver.tap([(150, 150)])
        start_time = Actions.getTextID(self, driver, Locators.TIME_POSITION_ID)
        time.sleep(3)
        end_time = Actions.getTextID(self, driver, Locators.TIME_POSITION_ID)
        assert start_time != end_time

        driver.press_keycode(4)
        time.sleep(1)
        driver.press_keycode(4)
        Actions.clickButtonXP(self, driver, Locators.PICTURES_FOLDER_BUTTON_XP)

        # Test *.jpg is playing
        Actions.clickButtonXP(self, driver, Locators.JPEG_FILE_XP)
        time.sleep(1)
        driver.tap([(150, 150)])
        file_name = Actions.getTextID(self, driver, Locators.PICTURE_NAME_ID)
        assert file_name == 'jpg_test'

        driver.press_keycode(4)

        # Test *.png is playing
        Actions.clickButtonXP(self, driver, Locators.PNG_FILE_XP)
        time.sleep(1)
        driver.tap([(150, 150)])
        file_name = Actions.getTextID(self, driver, Locators.PICTURE_NAME_ID)
        assert file_name == 'png_test'

        driver.press_keycode(4)

        # Test *.webp is playing
        Actions.clickButtonXP(self, driver, Locators.WEBP_FILE_XP)
        time.sleep(1)
        driver.tap([(150, 150)])
        file_name = Actions.getTextID(self, driver, Locators.PICTURE_NAME_ID)
        assert file_name == 'webp_test'
