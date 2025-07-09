import logging
import os
import time
import json

import logging

from framework.device_manager import DeviceManager
from framework.global_var import GlobalVar


# def read_json_by(file, *keys):
#     """
#     讀取json檔案，並可以任意設定讀到哪個鍵值\\
#     :param *keys: 依照欄位階層順序，最後一個欄位即為欲讀取到的欄位值\\
#         比如 *keys = 'ios', 'cube', 'uat'，則可以讀取到ios內的cube內的uat欄位值
#     """
#     with open(file, 'r', encoding='utf-8') as f:
#         data = json.load(f)
#         for key in keys:
#             data = data[key]
#     return data



class Utility:
    """

    """

    @staticmethod
    def tap(positions, remark: str = "", duration=None):
        logging.info(remark)
        DeviceManager.get_driver().tap(
            positions=positions,
            duration=duration
        )

    @staticmethod
    def skip_popup(check_element, click_element):
        """
        :param check_element: this element exists represents popup exists
        :param click_element: click button to close popup
        """
        if check_element.is_ready(3):
            logging.info(f'{check_element.remark()}出現')
            click_element.click()

    @staticmethod
    def read_json_by(file, *keys):
        """
        讀取json檔案，並可以任意設定讀到哪個鍵值
        :param keys: 依照欄位階層順序，最後一個欄位即為欲讀取到的欄位值 比如 *keys = 'ios', 'cube', 'uat'，則可以讀取到ios內的cube內的uat欄位值
        """
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for key in keys:
                data = data[key]
        return data

    @staticmethod
    def go_to_homepage():
        """
        Close app then restart it.
        """
        logging.info('🕹️ 嘗試重啟App以回到首頁')
        logging.info('關閉App...')
        DeviceManager.get_driver().terminate_app(GlobalVar.APP_PACKAGE)
        time.sleep(1)
        logging.info('開啟App...')
        DeviceManager.get_driver().activate_app(GlobalVar.APP_PACKAGE)
        time.sleep(6)  # 等待蓋板廣告

    @staticmethod
    def call_homepage():
        """
        Call Home Activity.
        """
        logging.info('🕹️ 呼叫Activity以回到首頁')
        DeviceManager.get_driver().execute_script(
            "mobile: startActivity", {
                "component": GlobalVar.APP_PACKAGE + "/" + GlobalVar.APP_HOME_ACTIVITY
            }
        )

    @staticmethod
    def refresh_page():
        """
        Refresh page.
        """
        logging.info('🕹️ 刷新頁面...')
        DeviceManager.get_driver().swipe(500, 800, 500, 1200, 2000)
        time.sleep(1.5)  # Wait DOM refresh.

    @staticmethod
    def press_enter():
        """
        Press "Enter" button.
        """
        logging.info('🕹️ 點擊Enter鍵...')
        DeviceManager.get_driver().press_keycode(66)