import unittest
from appium import webdriver
from data.data import bikroy_apk
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

dc = DesiredCapabilities.ANDROID
dc['appPackage'] = f"{bikroy_apk}"


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities={
                'platformName': 'Android',
                # 'deviceName': 'emulator-5554',
                'deviceName': '33001b3c1fc1556d',
                # 'platformVersion': '11',
                # 'deviceName': 'c9c5976',
                'automationName': 'uiautomator2',
                'newCommandTimeout': '240',
                'app': f"{bikroy_apk}",
                # 'appPackage': self.data.whatsapp_app_package,
                # 'appActivity': self.data.whatsapp_app_activity,
                # 'app-package': self.data.whatsapp_app_package,
                # 'app-activity': self.data.whatsapp_app_activity,
                # 'app': self.data.whatsapp,
                # 'appWaitPackage': self.data.whatsapp_app_package,
                # 'appWaitActivity': self.data.whatsapp_app_activity,
                'appWaitDuration': '30000',
                'noReset': False,
                'fullReset': False,
                # 'autoGrantPermissions': True,
                # 'unicodeKeyboard': True,
                # 'resetKeyboard': True,
            })

    def tearDown(self):
        self.driver.quit()
        # self.driver.press_button()
        # self.driver.press_keycode()

#
# class TestCase(object):
#     pass
#
#
# if __name__ == "__main__":
#     suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)
#     unittest.TextTestRunner(verbosity=1).run(suite)
