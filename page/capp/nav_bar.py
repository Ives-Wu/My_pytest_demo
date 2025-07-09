from appium.webdriver.common.appiumby import AppiumBy

from framework.component.basic_element import BasicObject
from framework.component.component import Component
from framework.component.sliding_element import SlidingObject
from framework.device_manager import DeviceManager


class NavBar(BasicObject):
    def __init__(self):
        super().__init__()
        self.set_remark("導覽列")
        self.driver = DeviceManager.get_driver()

    def is_page_loaded(self) -> None:
        self.find_job.assert_visible(False)
        self.notification.assert_visible(False)

    @property
    def find_job(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//android.widget.TextView[@text="找頭路"]/parent::*[@class="android.widget.LinearLayout"]'),
            f"{self.remark()} - 找頭路"
        )

    @property
    def find_company(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//android.widget.TextView[@text="找公司"]/parent::*[@class="android.widget.LinearLayout"]'),
            f"{self.remark()} - 找公司"
        )

    @property
    def notification(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//android.widget.TextView[@text="查通知"]/parent::*[@class="android.widget.LinearLayout"]'),
            f"{self.remark()} - 查通知"
        )

    @property
    def growth(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//android.widget.TextView[@text="成長"]/parent::*[@class="android.widget.LinearLayout"]'),
            f"{self.remark()} - 成長"
        )

    @property
    def about(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//android.widget.TextView[@text="關於我"]/parent::*[@class="android.widget.LinearLayout"]'),
            f"{self.remark()} - 關於我"
        )