from locators import Locators
from actions import Actions
from drivers import Driver as driver


class TestSortingView(driver, Actions):

    def test_sorting(self, driver):
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.SD_CARD_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.TEST_FOLDER_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.PICTURES_FOLDER_BUTTON_XP)

        # Test DATE DESCENDING
        Actions.clickButtonXP(self, driver, Locators.SORT_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.DATE_DESCENDING_BUTTON_XP)
        file_names_date_desc = Actions.getFewTextsID(self, driver, Locators.FILE_NAME_TEXT_ID)
        assert file_names_date_desc == Locators.DATE_DESCENDING_FILE_LIST

        # Test DATE ASCENDING
        Actions.clickButtonXP(self, driver, Locators.SORT_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.DATE_ASCENDING_BUTTON_XP)
        file_names_date_asc = Actions.getFewTextsID(self, driver, Locators.FILE_NAME_TEXT_ID)
        assert file_names_date_asc == Locators.DATE_ASCENDING_FILE_LIST

        # Test NAME DESCENDING
        Actions.clickButtonXP(self, driver, Locators.SORT_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.NAME_DESCENDING_BUTTON_XP)
        file_names_name_desc = Actions.getFewTextsID(self, driver, Locators.FILE_NAME_TEXT_ID)
        assert file_names_name_desc == Locators.NAME_DESCENDING_FILE_LIST

        # Test NAME ASCENDING
        Actions.clickButtonXP(self, driver, Locators.SORT_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.NAME_ASCENDING_BUTTON_XP)
        file_names_name_asc = Actions.getFewTextsID(self, driver, Locators.FILE_NAME_TEXT_ID)
        assert file_names_name_asc == Locators.NAME_ASCENDING_FILE_LIST

    def test_view_mode(self, driver):
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.SD_CARD_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.TEST_FOLDER_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.PICTURES_FOLDER_BUTTON_XP)

        # Gallery mode view, no date, size, type.
        assert Actions.isObjectExistsID(self, driver, Locators.FILE_DATE_TEXT_ID) is False
        assert Actions.isObjectExistsID(self, driver, Locators.FILE_SIZE_TEXT_ID) is False
        assert Actions.isObjectExistsID(self, driver, Locators.FILE_TYPE_TEXT_ID) is False

        Actions.clickButtonID(self, driver, Locators.VIEW_BUTTON_ID)

        # List mode view
        assert Actions.isObjectExistsID(self, driver, Locators.FILE_DATE_TEXT_ID) is True
        assert Actions.isObjectExistsID(self, driver, Locators.FILE_SIZE_TEXT_ID) is True
        assert Actions.isObjectExistsID(self, driver, Locators.FILE_TYPE_TEXT_ID) is True

        Actions.clickButtonID(self, driver, Locators.VIEW_BUTTON_ID)

        # Gallery mode view
        assert Actions.isObjectExistsID(self, driver, Locators.FILE_DATE_TEXT_ID) is False
        assert Actions.isObjectExistsID(self, driver, Locators.FILE_SIZE_TEXT_ID) is False
        assert Actions.isObjectExistsID(self, driver, Locators.FILE_TYPE_TEXT_ID) is False

