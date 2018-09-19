from datetime import datetime

class Locators:

    #GENERAL BUTTONS
    ALLOW_ACCESS_BUTTON_ID ='com.android.packageinstaller:id/permission_allow_button'
    MENU_BUTTON_XP = '//android.widget.ImageButton[@content-desc="The drawer has opened."]'
    PAGE_TITLE_ID = 'com.leialoft.redmediaplayer:id/filebrowser_toolbar_title'
    SORT_BUTTON_XP = '//android.widget.ImageView[@content-desc="The File Browser sort icon."]'
    VIEW_BUTTON_ID = 'com.leialoft.redmediaplayer:id/filebrowser_toolbar_tilelist_button'
    SUBMENU_BUTTON_XP = '//android.widget.ImageView[@content-desc="More options"]'

    # Menu buttons
    MOVIES_BUTTON_XP = '//android.support.v7.widget.LinearLayoutCompat[1]//android.widget.CheckedTextView'
    DOWNLOADS_BUTTON_XP = '//android.support.v7.widget.LinearLayoutCompat[2]//android.widget.CheckedTextView'
    CAMERA_BUTTON_XP = '//android.support.v7.widget.LinearLayoutCompat[3]//android.widget.CheckedTextView'
    PICTURES_BUTTON_XP = '//android.support.v7.widget.LinearLayoutCompat[4]//android.widget.CheckedTextView'
    INT_STORAGE_BUTTON_XP = '//android.support.v7.widget.LinearLayoutCompat[5]//android.widget.CheckedTextView'
    SD_CARD_BUTTON_XP = '//android.support.v7.widget.LinearLayoutCompat[6]//android.widget.CheckedTextView'

    # SUBMENU section
    NEW_FOLDER_BUTTON_XP = '//android.widget.LinearLayout[1]'
    SELECT_ALL_BUTTON_XP = '//android.widget.LinearLayout[2]'
    ABOUT_BUTTON_XP = '//android.widget.LinearLayout[3]'
    MOVE_BUTTON_XP = '//android.widget.LinearLayout[1]'

    # NEW FOLDER POPUP
    POPUP_NAME_ID = 'com.leialoft.redmediaplayer:id/alertTitle'
    POPUP_FIELD_XP = '//android.widget.FrameLayout/android.widget.EditText'
    POPUP_CANCEL_BUTTON_ID = 'android:id/button2'
    POPUP_SAVE_BUTTON_ID = 'android:id/button1'

    # MEDIA FILES
    # Folders
    TEST_FOLDER_BUTTON_XP = '//android.widget.TextView[@text="TestMediaData"]'
    VIDEOS_FOLDER_BUTTON_XP = '//android.widget.TextView[@text="Video"]'
    PICTURES_FOLDER_BUTTON_XP = '//android.widget.TextView[@text="Pictures"]'
    BUGS_FOLDER_BUTTON_XP = '//android.widget.TextView[@text="bugs_tests_data"]'

    # Video files
    MP4_FILE_XP = '//android.widget.TextView[@text="mp4_test"]'
    MKV_FILE_XP = '//android.widget.TextView[@text="mkv_test"]'
    GP3_FILE_XP = '//android.widget.TextView[@text="3gp_test"]'
    V4_TEST_VIDEO = '//android.widget.TextView[@text="trailer_sizzle_v4"]'

    # Picture files
    JPEG_FILE_XP = '//android.widget.TextView[@text="jpg_test"]'
    PNG_FILE_XP = '//android.widget.TextView[@text="png_test"]'
    WEBP_FILE_XP = '//android.widget.TextView[@text="webp_test"]'

    # Gallery buttons
    PICTURE_NAME_ID = 'com.leialoft.redmediaplayer:id/photo_content_name'

    # Video player buttons
    TIME_POSITION_ID = 'com.leialoft.redmediaplayer:id/exo_position'
    PAUSE_BUTTON_ID = 'com.leialoft.redmediaplayer:id/exo_pause'
    NEXT_TRACK_BUTTON_ID = 'com.leialoft.redmediaplayer:id/exo_next_video'
    PREV_TRACK_BUTTON_ID ='com.leialoft.redmediaplayer:id/exo_prev_video'
    INTERLACE_BUTTON_ID = 'com.leialoft.redmediaplayer:id/playback_interlace_button'


    # Sort buttons
    DATE_DESCENDING_BUTTON_XP ='//android.widget.LinearLayout[1]/android.widget.TextView'
    DATE_ASCENDING_BUTTON_XP = '//android.widget.LinearLayout[2]/android.widget.TextView'
    NAME_DESCENDING_BUTTON_XP = '//android.widget.LinearLayout[3]/android.widget.TextView'
    NAME_ASCENDING_BUTTON_XP = '//android.widget.LinearLayout[4]/android.widget.TextView'

    # Collect file names
    FILE_NAME_TEXT_ID = 'com.leialoft.redmediaplayer:id/filebrowser_item_title'

    # List folder view
    FILE_DATE_TEXT_ID = 'com.leialoft.redmediaplayer:id/filebrowser_item_date'
    FILE_SIZE_TEXT_ID = 'com.leialoft.redmediaplayer:id/filebrowser_item_size'
    FILE_TYPE_TEXT_ID = 'com.leialoft.redmediaplayer:id/filebrowser_item_type'

    # Static data
    DATE_DESCENDING_FILE_LIST = ['png_test', 'jpg_test', 'webp_test']
    DATE_ASCENDING_FILE_LIST = ['webp_test', 'jpg_test', 'png_test']
    NAME_DESCENDING_FILE_LIST = ['webp_test', 'png_test', 'jpg_test']
    NAME_ASCENDING_FILE_LIST = ['jpg_test', 'png_test', 'webp_test']
    FOLDER_NAME_TEXT = 'my test folder'

    # About page
    VERSION_TEXT = 'com.leialoft.redmediaplayer:id/filebrowser_about_version_text'

    FIRST_ITEM_TEXT_PICTURES_PAGE_XP = '//android.widget.TextView[@resource-id ="com.leialoft.redmediaplayer:id/filebrowser_item_title" and @instance = "1"]'
    IS_SELECTED_FILE_ID = 'com.leialoft.redmediaplayer:id/filebrowser_selected_check'
    BACK_BUTTON_IF_SELECTED_XP = '//android.widget.ImageButton[@content-desc="Navigate up"]'
    DELETE_BUTTON_IF_SELECTED_ID = 'com.leialoft.redmediaplayer:id/filebrowser_toolbar_delete_button'
    ONE_IMAGE_TO_SELECT_XP = '(//android.widget.ImageButton[@resource-id="com.leialoft.redmediaplayer:id/filebrowser_item_thumbnail"])[4]'
    FIRST_FILE_FOLDER_XP = '(//android.widget.ImageButton[@resource-id="com.leialoft.redmediaplayer:id/filebrowser_item_thumbnail"])[1]'


    CANCEL_MOVE_BUTTON_ID = 'com.leialoft.redmediaplayer:id/filebrowser_bottom_toolbar_cancel'
    OK_MOVE_BUTTON_ID = 'com.leialoft.redmediaplayer:id/filebrowser_bottom_toolbar_ok'