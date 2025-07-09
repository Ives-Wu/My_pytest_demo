import time
import logging

from framework.nav.navigation_1 import Nav
from framework.nav.navigation_2 import Sub
from framework.device_manager import DeviceManager
from framework.global_var import GlobalVar
from module.common import Utility


class PreConditionCApp:

    case_map = {}

    def setup_method(self, method):
        """
        """
        logging.info('🕹️ Start setup function.')
        DeviceManager.STATIC_DRIVER = None
        try:
            self.nav = Nav().capp
            self.sub = Sub().csub
            test_name = method.__name__
            if self.case_map.get(test_name, None) is None:
                logging.info("🕹️ Test name is None, skip setup method.")
                return
            self.user = Utility.read_json_by(GlobalVar.USER_JSON_PATH, self.case_map.get(test_name))
            self.sub.login_manager.login(self.user['email'], self.user['password'])
        except Exception as e:
            logging.error(f"❌Setup Fail: {e}")
            # self.teardown_method()
            DeviceManager.get_driver().quit()

    def teardown_method(self):

        logging.info('🕹️ Start teardown function.')

        # DeviceManager.get_driver().execute_script(
        #     "mobile: startActivity", {
        #         "component": GlobalVar.APP_PACKAGE + "/" + GlobalVar.APP_HOME_ACTIVITY
        #     }
        # )

        # self.sub.login_manager.logout()
        DeviceManager.get_driver().quit()
        DeviceManager.STATIC_DRIVER = None