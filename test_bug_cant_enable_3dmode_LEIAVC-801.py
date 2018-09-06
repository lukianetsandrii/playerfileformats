import time

from locators import Locators
from actions import Actions
from drivers import Driver as driver


class TestPlayDiffMediaTypes(driver, Actions):

    def test_bug_cant_enable_3dmode(self, driver):
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.SD_CARD_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.TEST_FOLDER_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.BUGS_FOLDER_BUTTON_XP)

        # Test *.mp4 is playing
        Actions.clickButtonXP(self, driver, Locators.V4_TEST_VIDEO)
        time.sleep(1)
        driver.tap([(150, 150)])
        Actions.clickButtonID(self, driver, Locators.PAUSE_BUTTON_ID)
        Actions.clickButtonID(self, driver, Locators.NEXT_TRACK_BUTTON_ID)
        time.sleep(5)
        driver.tap([(150, 150)])
        Actions.clickButtonID(self, driver, Locators.PAUSE_BUTTON_ID)
        driver.lock(1)
        driver.unlock()
        driver.tap([(150, 150)])
        Actions.clickButtonID(self, driver, Locators.PREV_TRACK_BUTTON_ID)
        Actions.clickButtonID(self, driver, Locators.PREV_TRACK_BUTTON_ID)




