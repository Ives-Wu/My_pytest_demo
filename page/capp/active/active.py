from appium.webdriver.common.appiumby import AppiumBy

from framework.component.basic_element import BasicObject
from framework.component.component import Component
from framework.component.sliding_element import SlidingObject
from framework.device_manager import DeviceManager


class ActivePage(BasicObject):
    def __init__(self):
        super().__init__()
        self.set_remark("初啟動頁面")
        self.driver = DeviceManager.get_driver()

    def is_page_loaded(self) -> None:
        self.title_.assert_visible(False)
        self.content.assert_visible(False)
        self.nav_login_text.assert_visible(False)

    @property
    def title_(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                             'new UiSelector().text("老朋友請直接登入吧")'),
            f"{self.remark()} - 標題"
        )

    @property
    def content(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//android.widget.TextView[contains(@text, "新朋友？")]'),
            f"{self.remark()} - 內文"
        )

    @property
    def nav_login_text(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.ID,
                                             'com.m104:id/tv_old_member_title'),
            f"{self.remark()} - 登入導向文字"
        )