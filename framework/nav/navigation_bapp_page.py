from appium import webdriver
from framework.device_manager import DeviceManager

class NavBApp:

    def __init__(self):
        self.__driver = None
        self.__page = None

        self.__xxx_page = None
        self.__yyy_function = None

    @property
    def driver(self) -> webdriver:
        return DeviceManager.get_driver()
