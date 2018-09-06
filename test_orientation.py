import time

from locators import Locators
from actions import Actions
from drivers import Driver as driver


class TestPlayDiffMediaTypes(driver, Actions):

    def test_open_video_portrait_landscape(self, driver):
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.SD_CARD_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.TEST_FOLDER_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.VIDEOS_FOLDER_BUTTON_XP)

        # Test video is playing in PORTRAIT mode
        assert driver.orientation == 'PORTRAIT'

        # Test *.mp4 is playing
        Actions.clickButtonXP(self, driver, Locators.MP4_FILE_XP)
        time.sleep(1)
        driver.tap([(150, 150)])
        start_time = Actions.getTextID(self, driver, Locators.TIME_POSITION_ID)
        time.sleep(3)
        end_time1 = Actions.getTextID(self, driver, Locators.TIME_POSITION_ID)
        assert start_time != end_time1

        driver.orientation = 'LANDSCAPE'
        assert driver.orientation == 'LANDSCAPE'
        time.sleep(1)
        driver.tap([(150, 150)])
        start_time = Actions.getTextID(self, driver, Locators.TIME_POSITION_ID)
        time.sleep(3)
        end_time2 = Actions.getTextID(self, driver, Locators.TIME_POSITION_ID)
        assert start_time != end_time2
        assert end_time1 <= end_time2

        driver.press_keycode(4)
        video_page_title = Actions.getTextID(self, driver, Locators.PAGE_TITLE_ID)
        assert video_page_title == 'Video'

        # Test video is playing in LANDSCAPE mode
        driver.orientation = 'LANDSCAPE'
        assert driver.orientation == 'LANDSCAPE'

        # Test *.mp4 is playing
        Actions.clickButtonXP(self, driver, Locators.MP4_FILE_XP)
        time.sleep(1)
        driver.tap([(150, 150)])
        start_time = Actions.getTextID(self, driver, Locators.TIME_POSITION_ID)
        time.sleep(3)
        end_time3 = Actions.getTextID(self, driver, Locators.TIME_POSITION_ID)
        assert start_time != end_time3

        driver.orientation = 'PORTRAIT'
        assert driver.orientation == 'PORTRAIT'
        time.sleep(1)
        driver.tap([(150, 150)])
        start_time = Actions.getTextID(self, driver, Locators.TIME_POSITION_ID)
        time.sleep(3)
        end_time4 = Actions.getTextID(self, driver, Locators.TIME_POSITION_ID)
        assert start_time != end_time4
        assert end_time3 <= end_time4

        driver.press_keycode(4)
        video_page_title = Actions.getTextID(self, driver, Locators.PAGE_TITLE_ID)
        assert video_page_title == 'Video'

        # driver.orientation = 'PORTRAIT'
        assert driver.orientation == 'PORTRAIT'

    def test_open_picture_portrait_landscape(self, driver):
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.SD_CARD_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.TEST_FOLDER_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.PICTURES_FOLDER_BUTTON_XP)

        # Test picture is displayed in PORTRAIT mode
        assert driver.orientation == 'PORTRAIT'

        # Test *.jpg is playing
        Actions.clickButtonXP(self, driver, Locators.JPEG_FILE_XP)
        time.sleep(1)
        driver.tap([(150, 150)])
        file_name = Actions.getTextID(self, driver, Locators.PICTURE_NAME_ID)
        assert file_name == 'jpg_test'

        driver.press_keycode(4)
        video_page_title = Actions.getTextID(self, driver, Locators.PAGE_TITLE_ID)
        assert video_page_title == 'Pictures'

        # Test picture is playing in LANDSCAPE mode
        driver.orientation = 'LANDSCAPE'
        assert driver.orientation == 'LANDSCAPE'

        # Test *.jpg is playing
        Actions.clickButtonXP(self, driver, Locators.JPEG_FILE_XP)
        time.sleep(1)
        driver.tap([(150, 150)])
        file_name = Actions.getTextID(self, driver, Locators.PICTURE_NAME_ID)
        assert file_name == 'jpg_test'

        driver.press_keycode(4)
        video_page_title = Actions.getTextID(self, driver, Locators.PAGE_TITLE_ID)
        assert video_page_title == 'Pictures'

        driver.orientation = 'PORTRAIT'
        assert driver.orientation == 'PORTRAIT'
