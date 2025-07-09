import logging

from appium import webdriver
from appium.options.common import AppiumOptions

from framework.global_var import GlobalVar


class DeviceManager:
    """
    Use class method to avoid create instance.
    """
    STATIC_DRIVER = None  # None: there will be only one driver instance in whole session.
    KEEP_APP_STATE = False  # True: do not reset App.
    TERMINATE_APP = True  # True: terminate App before create driver instance.


    @classmethod
    def get_driver(cls):
        """
        Create driver if there is no driver instance exist.
        """
        if cls.STATIC_DRIVER is None:
            logging.info('🕹️ Creating test driver...')
            cls.STATIC_DRIVER = cls._create_driver()
        return cls.STATIC_DRIVER

    @classmethod
    def _create_driver(cls):
        """
        Create corresponding driver.
        """
        return cls.android_driver()

    @classmethod
    def android_driver(cls):
        """
        Set Appium Options.
        """

        options = AppiumOptions()
        options.set_capability('platformName', 'Android')
        options.set_capability('udid', GlobalVar.ANDROID_UUID)
        options.set_capability('automationName', 'UiAutomator2')
        options.set_capability('autoGrantPermissions', True)
        options.set_capability('enableMultiWindows', True)
        options.set_capability('shouldTerminateApp', cls.TERMINATE_APP)
        options.set_capability('disableIdLocatorAutocompletion', True)
        options.set_capability('waitForIdleTimeout', 100)
        options.set_capability('adbExecTimeout', 60000)
        options.set_capability('relaxedSecurityEnabled', True)
        options.set_capability('noReset', cls.KEEP_APP_STATE)
        options.set_capability('appPackage', GlobalVar.APP_PACKAGE)
        options.set_capability('appActivity', GlobalVar.APP_ACTIVITY)

        driver = webdriver.Remote(GlobalVar.APPIUM_HOST_4723, options = options)
        logging.info(f'Driver Type: Android - {type(driver)}')
        return driver

