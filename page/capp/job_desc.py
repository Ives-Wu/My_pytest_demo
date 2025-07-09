from appium.webdriver.common.appiumby import AppiumBy

from framework.component.component import Component
from framework.component.sliding_element import SlidingObject
from framework.device_manager import DeviceManager
from page.capp.common import CommonPage


class JobDesc(CommonPage):
    def __init__(self):
        super().__init__()
        self.set_remark("工作說明頁")
        self.driver = DeviceManager.get_driver()

    def is_page_loaded(self) -> None:
        self.loading.assert_invisible(False)
        self.job_title.assert_visible(False)
        self.job_desc_text.assert_visible(False)
        [self.top_tool_bar.click() for _ in range(3)]  # Skip new feature hints.

    @property
    def top_tool_bar(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.ID,
                                             'com.m104:id/toolbar_collapse_layout'),
            f"{self.remark()} - 頂部工具列"
        )

    @property
    def job_title(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.ID,
                                             'com.m104:id/title_box_title'),
            f"{self.remark()} - 職務名稱"
        )

    @property
    def job_desc_text(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                             'new UiSelector().text("工作內容")'),
            f"{self.remark()} - 工作內容_文本"
        )

    @property
    def follow_button(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//android.widget.ImageView[contains(@content-desc, "關注按鈕,")]'),
            f"{self.remark()} - 關注按鈕"
        )

    @property
    def save_buton(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,
                                             '//android.widget.ImageView[contains(@content-desc, "儲存按鈕,")]'),
            f"{self.remark()} - 儲存按鈕"
        )



