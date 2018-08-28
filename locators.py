class Locators:
    MENU_BUTTON_XP = '//android.widget.ImageButton[@content-desc="The drawer has opened."]'

    # Menu buttons
    MOVIES_BUTTON_XP = '//android.support.v7.widget.LinearLayoutCompat[1]//android.widget.CheckedTextView'
    DOWNLOADS_BUTTON_XP = '//android.support.v7.widget.LinearLayoutCompat[2]//android.widget.CheckedTextView'
    CAMERA_BUTTON_XP = '//android.support.v7.widget.LinearLayoutCompat[3]//android.widget.CheckedTextView'
    PICTURES_BUTTON_XP = '//android.support.v7.widget.LinearLayoutCompat[4]//android.widget.CheckedTextView'
    INT_STORAGE_BUTTON_XP = '//android.support.v7.widget.LinearLayoutCompat[5]//android.widget.CheckedTextView'
    SD_CARD_BUTTON_XP = '//android.support.v7.widget.LinearLayoutCompat[6]//android.widget.CheckedTextView'

    # Folders
    TEST_FOLDER_BUTTON_XP = '//android.widget.TextView[@text="TestMediaData"]'
    VIDEOS_FOLDER_BUTTON_XP = '//android.widget.TextView[@text="Video"]'
    PICTURES_FOLDER_BUTTON_XP = '//android.widget.TextView[@text="Pictures"]'

    # Video files
    MP4_FILE_XP = '//android.widget.TextView[@text="mp4_test"]'
    MKV_FILE_XP = '//android.widget.TextView[@text="mkv_test"]'
    GP3_FILE_XP = '//android.widget.TextView[@text="3gp_test"]'

    # Picture files
    JPEG_FILE_XP = '//android.widget.TextView[@text="jpg_test"]'
    PNG_FILE_XP = '//android.widget.TextView[@text="png_test"]'
    WEBP_FILE_XP = '//android.widget.TextView[@text="webp_test"]'

    # Gallery buttons
    PICTURE_NAME_ID = 'com.leialoft.redmediaplayer:id/photo_content_name'

    # Video player buttons
    TIME_POSITION = 'com.leialoft.redmediaplayer:id/exo_position'
