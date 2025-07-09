from appium.webdriver.common.appiumby import AppiumBy

from framework.component.basic_element import BasicObject
from framework.component.component import Component
from framework.component.sliding_element import SlidingObject
from framework.device_manager import DeviceManager


class SearchMenu(BasicObject):
    def __init__(self):
        super().__init__()
        self.set_remark("搜尋面板")
        self.driver = DeviceManager.get_driver()

    def is_page_loaded(self) -> None:
        self.more_criteria.assert_visible(False)
        self.search_go_button.assert_visible(False)

    @property
    def search_field(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//android.widget.TextSwitcher[@resource-id="com.m104:id/cv_sbv_hint_text"]/android.widget.TextView'),
            f"{self.remark()} - 搜尋匡"
        )

    @property
    def search_field_input(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                             'new UiSelector().resourceId("com.m104:id/cv_sbv_edit_text")'),
            f"{self.remark()} - 搜尋輸入匡"
        )

    @property
    def find_company_text(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.ID,
                                             'com.m104:id/company_count'),
            f"{self.remark()} - 搜尋匡下方找公司文本"
        )

    @property
    def location(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//android.widget.TextView[@text="地區"]/parent::android.view.ViewGroup'),
            f"{self.remark()} - 地區"
        )

    @property
    def job_category(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//android.widget.TextView[@text="職務類別"]/parent::android.view.ViewGroup'),
            f"{self.remark()} - 職務類別"
        )

    @property
    def job_nature(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//android.widget.TextView[@text="職務性質"]/parent::android.view.ViewGroup'),
            f"{self.remark()} - 職務性質"
        )

    @property
    def more_criteria(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//android.widget.TextView[@text="更多條件"]/parent::android.view.ViewGroup'),
            f"{self.remark()} - 更多條件"
        )

    @property
    def search_go_button(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//android.widget.TextView[@resource-id="com.m104:id/btn_search"]'),
            f"{self.remark()} - 搜尋GO按鈕"
        )