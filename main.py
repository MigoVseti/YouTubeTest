import time
import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

            # ТЕСТ 1

    def test_tap(self) -> None:
        el = self.driver.find_element([(133, 2276)])

        self.driver.tap([el])

            # ТЕСТ 2

    def test_swipe(self) -> None:
        self.driver.tap([(505, 725)])

        self.driver.swipe(18, 1014, 307, 1014)

            # ТЕСТ 3

    def test_long_press(self) -> None:
        el = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                       value='new UiSelector().className("android.widget.ImageView").instance(4)')

        self.driver.long_press(el)

            # ТЕСТ 4

    def test_scroll(self) -> None:
        el1 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                       value='new UiSelector().className("android.widget.ImageView").instance(4)')

        el2 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                       value='new UiSelector().className("android.widget.ImageView").instance(5)')

        self.driver.scroll(el1, el2)

            # ТЕСТ 5

    def test_drag_and_drop(self) -> None:
        self.driver.tap([(505, 725)])
        el1 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                       value='new UiSelector().resourceId("com.google.android.youtube:id/watch_while_time_bar_view")')

        el2 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                       value='new UiSelector().resourceId("android:id/navigationBarBackground")')

        self.driver.drag_and_drop(el1, el2)

if __name__ == '__main__':
    unittest.main()
