import time
import logging

from framework.nav.navigation_1 import Nav
from framework.device_manager import DeviceManager


class PreConditionBApp:
    case_map = {}

    def setup_method(self, method):
        """
        初始化所有page, 跳過app啟動彈窗
        """
        try:
            self.nav = Nav().bapp
            self.nav.cube.prelogin_process()
            test_name = method.__name__
            if self.case_map.get(test_name, None) is None:
                logging.info("🕹️ skip_setup_method")
                return
            self.nav.cube.login(self.user)
        except Exception as e:
            logging.error(f"Setup Fail: {e}")
            self.teardown_method()

    def teardown_method(self):
        DeviceManager.get_driver().quit()
        DeviceManager.STATIC_DRIVER = None