from appium.webdriver.common.appiumby import AppiumBy

from framework.component.basic_element import BasicObject
from framework.component.component import Component
from framework.component.sliding_element import SlidingObject
from framework.device_manager import DeviceManager


class LoginPage(BasicObject):
    def __init__(self):
        super().__init__()
        self.set_remark("登入頁面")
        self.driver = DeviceManager.get_driver()

    def is_page_loaded(self) -> None:
        self.content.assert_visible(False)
        self.next_and_login_button.assert_visible(False)

    @property
    def nav_bar(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.ID,
                                             'com.m104:id/bar_title'),
            f"{self.remark()} - 導覽列標題"
        )

    @property
    def content(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                             'new UiSelector().text("登入104 享受所有會員專屬服務")'),
            f"{self.remark()} - 內文"
        )

    @property
    def identity_field(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                             'new UiSelector().resourceId("identity")'),
            f"{self.remark()} - 身分證輸入匡"
        )

    @property
    def password_field(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                             'new UiSelector().resourceId("password")'),
            f"{self.remark()} - 密碼輸入匡"
        )

    @property
    def next_and_login_button(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//android.widget.Button[@text="登入" or @text="下一步"]'),
            f"{self.remark()} - 下一步或登入按鈕"
        )

    @property
    def login_button(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                             'new UiSelector().text("登入")'),
            f"{self.remark()} - 登入按鈕"
        )

