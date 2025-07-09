from appium.webdriver.common.appiumby import AppiumBy

from framework.component.basic_element import BasicObject
from framework.component.component import Component
from framework.component.sliding_element import SlidingObject
from framework.device_manager import DeviceManager


class CommonPage(BasicObject):
    def __init__(self):
        super().__init__()
        self.set_remark("通用元素")
        self.driver = DeviceManager.get_driver()

    # def is_page_loaded(self) -> None:
    #     pass

    @property
    def loading_icon(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//*[contains(@text, "Loading")]'),
            f"{self.remark()} - Loading icon"
        )

    @property
    def loading(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//*[@text="執行中，請稍後..."]'),
            f"{self.remark()} - Loading icon"
        )