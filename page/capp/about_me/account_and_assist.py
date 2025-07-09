from appium.webdriver.common.appiumby import AppiumBy

from framework.component.basic_element import BasicObject
from framework.component.component import Component
from framework.component.sliding_element import SlidingObject
from framework.device_manager import DeviceManager


class AccountAndAssistPage(BasicObject):
    def __init__(self):
        super().__init__()
        self.set_remark("關於我頁")
        self.driver = DeviceManager.get_driver()

    def is_page_loaded(self) -> None:
        self.title_.assert_visible(False)
        self.appearance_mode.assert_visible(False)

    @property
    def title_(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                             'new UiSelector().text("帳號與協助")'),
            f"{self.remark()} - 標題"
        )

    @property
    def appearance_mode(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//android.widget.TextView[contains(@text, "模式")]'),
            f"{self.remark()} - 深淺模式"
        )

    @property
    def login_and_signup(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                             'new UiSelector().resourceId("com.m104:id/btn_login")'),
            f"{self.remark()} - 登入及會員註冊"
        )

    @property
    def logout(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                             'new UiSelector().resourceId("com.m104:id/btn_logout")'),
            f"{self.remark()} - 登出工作快找"
        )

class LogoutPopUp(BasicObject):
    def __init__(self):
        super().__init__()
        self.set_remark("登出彈窗")
        self.driver = DeviceManager.get_driver()

    def is_page_loaded(self) -> None:
        self.title_.assert_visible(False)

    @property
    def title_(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//android.widget.TextView[@text="即將登出服務"]'),
            f"{self.remark()} - 標題"
        )

    @property
    def accept_button(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//android.widget.TextView[@text="果斷登出"]'),
            f"{self.remark()} - 果斷登出按鈕"
        )

    @property
    def deny_button(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//android.widget.TextView[@text="我再想想"]'),
            f"{self.remark()} - 我再想想按鈕"
        )