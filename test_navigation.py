from locators import Locators
from actions import Actions
from drivers import Driver as driver


class TestNavigation(driver, Actions):

    def test_switch_between_folders(self, driver):
        # Start folder is movies
        movies_page_title = Actions.getTextID(self, driver, Locators.PAGE_TITLE_ID)
        assert movies_page_title == 'Movies'
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.DOWNLOADS_BUTTON_XP)
        downloads_page_title = Actions.getTextID(self, driver, Locators.PAGE_TITLE_ID)
        assert downloads_page_title == 'Downloads'
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.MOVIES_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.CAMERA_BUTTON_XP)
        camera_page_title = Actions.getTextID(self, driver, Locators.PAGE_TITLE_ID)
        assert camera_page_title == 'Camera'
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.MOVIES_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.PICTURES_BUTTON_XP)
        pictures_page_title = Actions.getTextID(self, driver, Locators.PAGE_TITLE_ID)
        assert pictures_page_title == 'Pictures'
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.MOVIES_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.INT_STORAGE_BUTTON_XP)
        intstorage_page_title = Actions.getTextID(self, driver, Locators.PAGE_TITLE_ID)
        assert intstorage_page_title == 'Internal Storage'
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.MOVIES_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.SD_CARD_BUTTON_XP)
        sdcard_page_title = Actions.getTextID(self, driver, Locators.PAGE_TITLE_ID)
        assert sdcard_page_title == 'SD Card'

        # Start folder is downloads
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.DOWNLOADS_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.MOVIES_BUTTON_XP)
        movies_page_title = Actions.getTextID(self, driver, Locators.PAGE_TITLE_ID)
        assert movies_page_title == 'Movies'
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.DOWNLOADS_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.CAMERA_BUTTON_XP)
        camera_page_title = Actions.getTextID(self, driver, Locators.PAGE_TITLE_ID)
        assert camera_page_title == 'Camera'
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.DOWNLOADS_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.PICTURES_BUTTON_XP)
        pictures_page_title = Actions.getTextID(self, driver, Locators.PAGE_TITLE_ID)
        assert pictures_page_title == 'Pictures'
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.DOWNLOADS_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.INT_STORAGE_BUTTON_XP)
        intstorage_page_title = Actions.getTextID(self, driver, Locators.PAGE_TITLE_ID)
        assert intstorage_page_title == 'Internal Storage'
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.DOWNLOADS_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.SD_CARD_BUTTON_XP)
        sdcard_page_title = Actions.getTextID(self, driver, Locators.PAGE_TITLE_ID)
        assert sdcard_page_title == 'SD Card'

        # Start folder is camera
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.CAMERA_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.MOVIES_BUTTON_XP)
        movies_page_title = Actions.getTextID(self, driver, Locators.PAGE_TITLE_ID)
        assert movies_page_title == 'Movies'
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.CAMERA_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.DOWNLOADS_BUTTON_XP)
        downloads_page_title = Actions.getTextID(self, driver, Locators.PAGE_TITLE_ID)
        assert downloads_page_title == 'Downloads'
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.CAMERA_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.PICTURES_BUTTON_XP)
        pictures_page_title = Actions.getTextID(self, driver, Locators.PAGE_TITLE_ID)
        assert pictures_page_title == 'Pictures'
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.CAMERA_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.INT_STORAGE_BUTTON_XP)
        intstorage_page_title = Actions.getTextID(self, driver, Locators.PAGE_TITLE_ID)
        assert intstorage_page_title == 'Internal Storage'
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.CAMERA_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.SD_CARD_BUTTON_XP)
        sdcard_page_title = Actions.getTextID(self, driver, Locators.PAGE_TITLE_ID)
        assert sdcard_page_title == 'SD Card'

        # Start folder is pictures
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.PICTURES_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.MOVIES_BUTTON_XP)
        movies_page_title = Actions.getTextID(self, driver, Locators.PAGE_TITLE_ID)
        assert movies_page_title == 'Movies'
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.PICTURES_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.DOWNLOADS_BUTTON_XP)
        downloads_page_title = Actions.getTextID(self, driver, Locators.PAGE_TITLE_ID)
        assert downloads_page_title == 'Downloads'
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.PICTURES_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.CAMERA_BUTTON_XP)
        camera_page_title = Actions.getTextID(self, driver, Locators.PAGE_TITLE_ID)
        assert camera_page_title == 'Camera'
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.PICTURES_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.INT_STORAGE_BUTTON_XP)
        intstorage_page_title = Actions.getTextID(self, driver, Locators.PAGE_TITLE_ID)
        assert intstorage_page_title == 'Internal Storage'
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.PICTURES_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.SD_CARD_BUTTON_XP)
        sdcard_page_title = Actions.getTextID(self, driver, Locators.PAGE_TITLE_ID)
        assert sdcard_page_title == 'SD Card'

        # Start folder is internal storage
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.INT_STORAGE_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.MOVIES_BUTTON_XP)
        movies_page_title = Actions.getTextID(self, driver, Locators.PAGE_TITLE_ID)
        assert movies_page_title == 'Movies'
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.INT_STORAGE_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.DOWNLOADS_BUTTON_XP)
        downloads_page_title = Actions.getTextID(self, driver, Locators.PAGE_TITLE_ID)
        assert downloads_page_title == 'Downloads'
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.INT_STORAGE_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.CAMERA_BUTTON_XP)
        camera_page_title = Actions.getTextID(self, driver, Locators.PAGE_TITLE_ID)
        assert camera_page_title == 'Camera'
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.INT_STORAGE_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.PICTURES_BUTTON_XP)
        pictures_page_title = Actions.getTextID(self, driver, Locators.PAGE_TITLE_ID)
        assert pictures_page_title == 'Pictures'
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.INT_STORAGE_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.SD_CARD_BUTTON_XP)
        sdcard_page_title = Actions.getTextID(self, driver, Locators.PAGE_TITLE_ID)
        assert sdcard_page_title == 'SD Card'

        # Start folder is sd card
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.SD_CARD_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.MOVIES_BUTTON_XP)
        movies_page_title = Actions.getTextID(self, driver, Locators.PAGE_TITLE_ID)
        assert movies_page_title == 'Movies'
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.SD_CARD_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.DOWNLOADS_BUTTON_XP)
        downloads_page_title = Actions.getTextID(self, driver, Locators.PAGE_TITLE_ID)
        assert downloads_page_title == 'Downloads'
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.SD_CARD_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.CAMERA_BUTTON_XP)
        camera_page_title = Actions.getTextID(self, driver, Locators.PAGE_TITLE_ID)
        assert camera_page_title == 'Camera'
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.SD_CARD_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.PICTURES_BUTTON_XP)
        pictures_page_title = Actions.getTextID(self, driver, Locators.PAGE_TITLE_ID)
        assert pictures_page_title == 'Pictures'
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.INT_STORAGE_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.INT_STORAGE_BUTTON_XP)
        intstorage_page_title = Actions.getTextID(self, driver, Locators.PAGE_TITLE_ID)
        assert intstorage_page_title == 'Internal Storage'
