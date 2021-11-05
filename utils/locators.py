from selenium.webdriver.common.by import By


class BikroyLocators:
    emailText = "ashiq.qups@gmail.com"
    passwordText = "Asdfgh123456"
    postBtn = "com.bikroy:id/btn_post"  # id
    home_btn = "com.bikroy:id/main_bottom_panel_home"  # id
    search_icon = "com.bikroy:id/main_bottom_panel_search"  # id
    # chatBtn = By.ID("com.bikroy:id/main_bottom_panel_chat")
    profileBtn = "com.bikroy:id/main_bottom_panel_my_account"
    # activityClose = By.ID("com.bikroy:id/register_activity_close")
    sign_in_email_btn = "com.bikroy:id/sign_in_sign_up_email_button"
    emailField = "com.bikroy:id/sign_in_email"  # id
    passwordField = "com.bikroy:id/sign_in_password"  # id
    loginBtn = "com.bikroy:id/register_register_button"  # id
    # noAccountBtn = By.ID("com.bikroy:id/register_have_account_text")
    # signUpBtn = By.ID("com.bikroy:id/register_signup_button")
    # forgotPassBtn = By.ID("com.bikroy:id/register_forgot_password")
    logoutBtn = "com.bikroy:id/my_account_logout"  # id
    # confirmPassField = By.ID("পাসওয়ার্ড আবার")
    # nameText = "Abir"
    # signupEmailText = "abir.qups@gmail.com"
    # signUpPasswordText = "Asdfgh123456"
    myAds = "com.bikroy:id/my_account_my_ads"
    myMembership = "com.bikroy:id/my_account_my_membership"
    favorites = "com.bikroy:id/my_account_favorites"
    myProfile = "com.bikroy:id/my_account_my_resume"
    # backButton = "android.widget.ImageButton"  # class_name
    backButton_eng = '//android.widget.ImageButton[@content-desc="Navigate up"]'  # class_name
    backButton_bang = '//android.widget.ImageButton[@content-desc="উপরে নেভিগেট করুন"]'  # class_name
    # headingElements = By.ID("android.widget.TextView")
    # adSliderItems = By.ID("android.widget.FrameLayout")
    editSearchField = "com.bikroy:id/edit_search"
    searchBox = "com.bikroy:id/search_verticals"  # id
    intro_close_btn = "com.bikroy:id/intro_close"
    first_product = "com.bikroy:id/ad_item_fluid_photo"  # id
    gear_icon = "com.bikroy:id/action_settings"
    english_language = '//android.widget.TextView[@package="com.bikroy"][contains(@text,"English")]'  # xpath
    favorite_icon = "com.bikroy:id/action_favorite"  # id
    category_btn = "com.bikroy:id/appbar_category" #id
    jobs_link = '//android.widget.TextView[@package="com.bikroy"][contains(@text,"Jobs")]'  # xpath
    job_search_field = "com.bikroy:id/job_verticals_search_input" #id
    search_btn = 'com.bikroy:id/jobs_vertical_search' #id