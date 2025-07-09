from appium.webdriver.common.appiumby import AppiumBy

from framework.component.basic_element import BasicObject
from framework.component.component import Component
from framework.component.sliding_element import SlidingObject
from framework.device_manager import DeviceManager


class PopUpPage(BasicObject):
    def __init__(self):
        super().__init__()
        self.set_remark("彈窗")
        self.driver = DeviceManager.get_driver()

    # def is_page_loaded(self) -> None:
    #    pass

    # 登入彈窗
    @property
    def allow_noti_content(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.XPATH,
                                             '//android.widget.TextView[@text="要允許「104工作快找」傳送通知嗎？"]'),
            f"{self.remark()} - 允許通知彈窗內文"
        )

    @property
    def allow_noti_accept_button(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.ID,
                                             'com.android.permissioncontroller:id/permission_allow_button'),
            f"{self.remark()} - 允許通知彈窗允許按鈕"
        )

    @property
    def allow_noti_deny_button(self):
        return Component(
            lambda: self.driver.find_element(AppiumBy.ID,
                                             'com.android.permissioncontroller:id/permission_deny_button'),
            f"{self.remark()} - 允許通知彈窗允許按鈕"
        )
