from appium.webdriver.common.appiumby import AppiumBy

from framework.component.basic_element import BasicObject
from framework.component.component import Component
from framework.component.sliding_element import SlidingObject
from framework.device_manager import DeviceManager
from page.capp.common import CommonPage


class JobList(CommonPage):
    def __init__(self):
        super().__init__()
        self.set_remark("工作列表頁")
        self.driver = DeviceManager.get_driver()

    def is_page_loaded(self) -> None:
        self.loading.assert_invisible(False)
        self.job_tab.assert_visible(False)
        self.company_tab.assert_visible(False)

    @property
    def job_tab(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,
                                             '找工作'),
            f"{self.remark()} - 找工作tab"
        )

    @property
    def company_tab(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,
                                             '找公司'),
            f"{self.remark()} - 找公司tab"
        )


    def job(self, job_name: str = ''):
        SlidingObject().scroll_to_element(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             f'(//android.view.ViewGroup[@resource-id="com.m104:id/front_view"]/android.widget.TextView[@text="{job_name}"])[1]'),
        )
        return Component(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             f'(//android.view.ViewGroup[@resource-id="com.m104:id/front_view"]/android.widget.TextView[@text="{job_name}"])[1]'),
            f"{self.remark()} - 職缺卡片{job_name}"
        )

    def save_job_button(self, job_name: str = ''):
        return Component(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             f'(//android.view.ViewGroup[@resource-id="com.m104:id/front_view"]/android.widget.TextView[@text="{job_name}"])[1]/following-sibling::*[@resource-id="com.m104:id/save_view_switcher"]/*[contains(@content-desc, "儲存按鈕,")]'),
            f"{self.remark()} - 儲存職缺{job_name}按鈕"
        )

