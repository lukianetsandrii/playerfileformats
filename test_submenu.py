from locators import Locators
from actions import Actions
from drivers import Driver as driver


class Test_CreateFolder_SelectOneAllfile_Aboutpage_Deletefile(driver, Actions):
    """
    Preconditions: 1. at least 4 files in the pictures folder

    1. Open Pictures folder
    2. Open submenu for the Pictures folder
    3. Open "About" page and check: page title, bootom inscription contains "Version:" text
    4. Back to the Pictures folder
    5. Open submenu and tap "Select all" button
    6. Check that there are at least three selected elements
    7. Back to the Pictures folder
    8. Longtap on one element
    9. Check if the "V" icon is exists

    Post-condition: need to delete created folder. Will be automated when the corresponding functional will be added
    """

    def test_create_folder_select_one_all_about(self, driver):
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.PICTURES_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.SUBMENU_BUTTON_XP)

        # Test about page
        Actions.clickButtonXP(self, driver, Locators.ABOUT_BUTTON_XP)

        assert Actions.getTextID(self, driver, Locators.PAGE_TITLE_ID) == 'About'
        assert Actions.version_text(self, driver) == 'Version:'

        driver.press_keycode(4)

        # Test check select all
        Actions.clickButtonXP(self, driver, Locators.SUBMENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.SELECT_ALL_BUTTON_XP)

        assert Actions.count_of_selected_on_the_screen(self, driver) > 3

        Actions.clickButtonXP(self, driver, Locators.BACK_BUTTON_IF_SELECTED_XP)

        # Select one
        Actions.longtap(self, driver, Locators.ONE_IMAGE_TO_SELECT_XP)

        assert Actions.isObjectExistsID(self, driver, Locators.IS_SELECTED_FILE_ID) == True

        Actions.clickButtonXP(self, driver, Locators.BACK_BUTTON_IF_SELECTED_XP)

        # Test create new folder
        first_file = Actions.getTextXP(self, driver, Locators.FIRST_ITEM_TEXT_PICTURES_PAGE_XP)
        Actions.clickButtonXP(self, driver, Locators.SUBMENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.NEW_FOLDER_BUTTON_XP)

        assert Actions.getTextID(self, driver, Locators.POPUP_NAME_ID) == 'Create new folder'

        Actions.fill_field_id(self, driver)
        Actions.clickButtonID(self, driver, Locators.POPUP_SAVE_BUTTON_ID)

        assert Actions.getTextXP(self, driver, Locators.FIRST_ITEM_TEXT_PICTURES_PAGE_XP) != first_file

    """
    Preconditions: 1. At least one file in the Camera folder

    1. Open Pictures folder
    2. Open submenu for the Pictures folder
    3. Select all files and get digit from title hove many files there are before and store it
    4. Go to the Camera folder
    5. Longtap and select one file, check Cancel button
    6. Check that there are no selected elements
    7. Longtap and select one file, submenu - select "move"
    8. Go to Pictures folder and paste it
    9. Select all files and get digit from title hove many files there are after and store it
    10. Check that count after > count before

    Post-condition: 
    """

    def test_move_file(self, driver):
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.PICTURES_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.SUBMENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.SELECT_ALL_BUTTON_XP)

        count_on_pictures_page_before = Actions.count_of_all_selected(self, driver)

        Actions.clickButtonXP(self, driver, Locators.BACK_BUTTON_IF_SELECTED_XP)
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.CAMERA_BUTTON_XP)

        Actions.longtap(self, driver, Locators.FIRST_FILE_FOLDER_XP)
        Actions.clickButtonXP(self, driver, Locators.SUBMENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.MOVE_BUTTON_XP)
        Actions.clickButtonID(self, driver, Locators.CANCEL_MOVE_BUTTON_ID)

        assert Actions.isObjectExistsID(self, driver, Locators.IS_SELECTED_FILE_ID) == False

        Actions.longtap(self, driver, Locators.FIRST_FILE_FOLDER_XP)
        Actions.clickButtonXP(self, driver, Locators.SUBMENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.MOVE_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.PICTURES_BUTTON_XP)
        Actions.clickButtonID(self, driver, Locators.OK_MOVE_BUTTON_ID)
        driver.lock()
        driver.unlock()
        Actions.clickButtonXP(self, driver, Locators.SUBMENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.SELECT_ALL_BUTTON_XP)

        count_on_pictures_page_after = Actions.count_of_all_selected(self, driver)

        assert count_on_pictures_page_before < count_on_pictures_page_after

    """
   Preconditions: 1. At least one file in the Downloads folder

   1. Open Downloads folder
   2. Open submenu, select all files and get digit from title hove many files there are before and store it
   3. Check that there are at least three selected elements
   4. Back to the Downloads folder
   5. Longtap on one element and delete it
   6. Check popup name, tap ok button
   7. Open submenu, select all files and get digit from title hove many files there are after and store it
   8. Check that count after > count before

   Post-condition: 
   """

    def test_delete_file(self, driver):
        Actions.clickButtonXP(self, driver, Locators.MENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.DOWNLOADS_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.SUBMENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.SELECT_ALL_BUTTON_XP)

        count_on_downloads_page_before = Actions.count_of_all_selected(self, driver)

        Actions.clickButtonXP(self, driver, Locators.BACK_BUTTON_IF_SELECTED_XP)
        Actions.longtap(self, driver, Locators.FIRST_FILE_FOLDER_XP)
        Actions.clickButtonID(self, driver, Locators.DELETE_BUTTON_IF_SELECTED_ID)

        assert Actions.getTextID(self, driver, Locators.POPUP_NAME_ID) == 'Delete files'

        Actions.clickButtonID(self, driver, Locators.POPUP_SAVE_BUTTON_ID)
        Actions.clickButtonXP(self, driver, Locators.SUBMENU_BUTTON_XP)
        Actions.clickButtonXP(self, driver, Locators.SELECT_ALL_BUTTON_XP)

        count_on_downloads_page_after = Actions.count_of_all_selected(self, driver)

        assert count_on_downloads_page_before > count_on_downloads_page_after

        # TODO delete created folder
