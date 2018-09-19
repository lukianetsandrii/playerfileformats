import time
import os
import subprocess

from locators import Locators
from actions import Actions
from drivers import Driver as driver


class ADB:
    adb_path = ""
    adb = "adb"

    @staticmethod
    def Is3DBacklightOn():
        is_on = False
        backlight_3d_int = int(ADB.Command(['shell', 'cat /sys/class/leds/LM36923H-BL/brightness']))
        backlight_2d_int = int(ADB.Command(['shell', 'cat /sys/class/leds/lcd-backlight/brightness']))
        if (backlight_2d_int < backlight_3d_int):
            is_on = True
        return is_on

    @staticmethod
    def Command(commandsList):
        args = [ADB.adb_path + ADB.adb] + commandsList;
        result = subprocess.check_output(args)[:-1]
        return result

class TestPlayDiffMediaTypes(driver, Actions, ADB):

    # def test_bug_cant_enable_3dmode(self, driver):
    #     Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
    #     Actions.clickButtonXP(self, driver, Locators.SD_CARD_BUTTON_XP)
    #     Actions.clickButtonXP(self, driver, Locators.TEST_FOLDER_BUTTON_XP)
    #     Actions.clickButtonXP(self, driver, Locators.BUGS_FOLDER_BUTTON_XP)
    #
    #     # Test *.mp4 is playing
    #     Actions.clickButtonXP(self, driver, Locators.V4_TEST_VIDEO)
    #     time.sleep(1)
    #     driver.tap([(150, 150)])
    #     Actions.clickButtonID(self, driver, Locators.PAUSE_BUTTON_ID)
    #     Actions.clickButtonID(self, driver, Locators.NEXT_TRACK_BUTTON_ID)
    #     time.sleep(5)
    #     driver.tap([(150, 150)])
    #     Actions.clickButtonID(self, driver, Locators.PAUSE_BUTTON_ID)
    #     driver.lock(1)
    #     driver.unlock()
    #     driver.tap([(150, 150)])
    #     Actions.clickButtonID(self, driver, Locators.PREV_TRACK_BUTTON_ID)
    #     Actions.clickButtonID(self, driver, Locators.PREV_TRACK_BUTTON_ID)

    def test_2d_or_3d_is_on(self, driver):
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.SD_CARD_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.TEST_FOLDER_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.BUGS_FOLDER_BUTTON_XP)

        # Test *.mp4 is playing
        Actions.clickButtonXP(self, driver, Locators.V4_TEST_VIDEO)
        # time.sleep(1)
        assert Actions.is3DBacklightOn(self) is True
        # time.sleep(1)
        driver.tap([(150, 150)])
        Actions.clickButtonID(self, driver, Locators.INTERLACE_BUTTON_ID)
        # time.sleep(1)
        assert Actions.is3DBacklightOn(self) is False



        #
        # time.sleep(1)
        # driver.tap([(150, 150)])
        # Actions.clickButtonID(self, driver, Locators.PAUSE_BUTTON_ID)
        # Actions.clickButtonID(self, driver, Locators.NEXT_TRACK_BUTTON_ID)
        # time.sleep(5)
        # driver.tap([(150, 150)])
        # Actions.clickButtonID(self, driver, Locators.PAUSE_BUTTON_ID)
        # driver.lock(1)
        # driver.unlock()
        # driver.tap([(150, 150)])
        # Actions.clickButtonID(self, driver, Locators.PREV_TRACK_BUTTON_ID)
        # Actions.clickButtonID(self, driver, Locators.PREV_TRACK_BUTTON_ID)


