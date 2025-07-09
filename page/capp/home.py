from appium.webdriver.common.appiumby import AppiumBy

from framework.component.basic_element import BasicObject
from framework.component.component import Component
from framework.component.sliding_element import SlidingObject
from framework.device_manager import DeviceManager


class HomePage(BasicObject):
    def __init__(self):
        super().__init__()
        self.set_remark("首頁")
        self.driver = DeviceManager.get_driver()

    def is_page_loaded(self) -> None:
        self.search_field.assert_visible(False)
        self.banner_area.assert_visible(False)

    @property
    def search_field(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,
                                             '搜尋框'),
            f"{self.remark()} - 搜尋框"
        )

    @property
    def banner_area(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                             'new UiSelector().resourceId("com.m104:id/banner_mask")'),
            f"{self.remark()} - banner區塊"
        )

    @property
    def fail_ele(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                             'new UiSelector().resourceId("com.m104:id/bbbbbb")'),
            f"{self.remark()} - 測試fail元素"
        )
