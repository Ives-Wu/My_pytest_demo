from appium.webdriver.common.appiumby import AppiumBy

from framework.component.component import Component
from framework.component.sliding_element import SlidingObject
from framework.device_manager import DeviceManager
from page.capp.common import CommonPage


class MyFollowed(CommonPage):
    def __init__(self):
        super().__init__()
        self.set_remark("我的關注頁")
        self.driver = DeviceManager.get_driver()

    def is_page_loaded(self) -> None:
        self.loading.assert_invisible(False)
        self.followed_tab.assert_visible(False)
        self.post_tab.assert_visible(False)
        self.top_tool_bar.click()

    @property
    def top_tool_bar(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.ID,
                                             'com.m104:id/toolbar_constraintLayout'),
            f"{self.remark()} - 頂部工具列"
        )

    @property
    def followed_tab(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,
                                             '關注公司'),
            f"{self.remark()} - 關注公司tab"
        )

    @property
    def post_tab(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,
                                             '企業動態'),
            f"{self.remark()} - 企業動態tab"
        )

    @property
    def new_notification_tab(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,
                                             '新工作通知'),
            f"{self.remark()} - 新工作通知tab"
        )

    def company_card(self, company_name: str = ''):
        return Component(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             f'//android.widget.TextView[@resource-id="com.m104:id/company_name_textView" and @text="{company_name}"]'),
            f"{self.remark()} - {company_name}公司卡片"
        )

    def followed_job_button(self, company_name: str = ''):
        return Component(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             f'//android.widget.TextView[@resource-id="com.m104:id/company_name_textView" and @text="{company_name}"]/following-sibling::*[@resource-id="com.m104:id/id_linear_line"]/*[@resource-id="com.m104:id/company_followed_jobs_count_textView"]'),
            f"{self.remark()} - {company_name}的已關注工作按鈕"
        )

    def job_opportunity_button(self, company_name: str = ''):
        return Component(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             f'//android.widget.TextView[@resource-id="com.m104:id/company_name_textView" and @text="{company_name}"]/following-sibling::*[@resource-id="com.m104:id/id_linear_line"]/*[@resource-id="com.m104:id/company_vacancies_textView"]'),
            f"{self.remark()} - {company_name}的工作機會按鈕"
        )

class FollowedJobList(CommonPage):
    def __init__(self):
        super().__init__()
        self.set_remark("關注職務列表")
        self.driver = DeviceManager.get_driver()

    def is_page_loaded(self) -> None:
        self.loading.assert_invisible(False)
        self.title_bar.assert_visible(False)

    @property
    def title_bar(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.ID,
                                             'com.m104:id/toolbar_title_textView'),
            f"{self.remark()} - 標題列"
        )

    def followed_job(self, job_name: str = ''):
        return Component(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             f'//android.widget.TextView[@resource-id="com.m104:id/job_name_textView" and @text="{job_name}"]'),
            f"{self.remark()} - {job_name}"
        )

    def followed_job_button(self, job_name: str = ''):
        return Component(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             f'//android.widget.TextView[@resource-id="com.m104:id/job_name_textView" and @text="{job_name}"]/following-sibling::*[contains(@content-desc, "關注按鈕,")]'),
            f"{self.remark()} - {job_name}的關注按鈕"
        )

