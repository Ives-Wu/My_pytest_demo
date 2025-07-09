from appium.webdriver.common.appiumby import AppiumBy

from framework.component.component import Component
from framework.component.sliding_element import SlidingObject
from framework.device_manager import DeviceManager
from page.capp.common import CommonPage
from page.capp.nav_bar import NavBar


class AboutMePage(CommonPage, NavBar):
    def __init__(self):
        super().__init__()
        self.set_remark("關於我頁")

    def is_page_loaded(self) -> None:
        self.loading.assert_invisible(False)
        self.apply_history_button.assert_visible(False)
        self.account_and_assist.assert_visible(False)
        self.about.click()  # Skip new feature hints.

    @property
    def apply_history_button(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.m104:id/apply_history")'),
            f"{self.remark()} - 應徵紀錄按鈕"
        )

    @property
    def account_and_assist(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="帳號與協助"]/parent::android.view.ViewGroup[@resource-id="com.m104:id/front_view"]'),
            f"{self.remark()} - 帳號與協助"
        )

    @property
    def my_followed_button(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.ID,
                                             'com.m104:id/my_follow_frameLayout'),
            f"{self.remark()} - 我的關注_按鈕"
        )

    @property
    def my_saved_button(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.ID,
                                             'com.m104:id/favorite_job_icon_container'),
            f"{self.remark()} - 儲存工作_按鈕"
        )