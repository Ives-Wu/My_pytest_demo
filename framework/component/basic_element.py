import os
import time

import allure
import logging

from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, InvalidSelectorException
from selenium.webdriver.remote.webelement import WebElement
from framework.component.exception.ElementNotVisibleExceptions import ElementNotVisibleExceptions
from framework.component.exception.InvalidSelectorExceptions import InvalidSelectorExceptions
from framework.component.exception.NoSuchElementExceptions import NoSuchElementExceptions
from framework.component.exception.NotReadyException import NotReadyException
from framework.device_manager import DeviceManager

from framework.global_var import GlobalVar


class BasicObject:
    __remark = ""

    def __init__(self):
        self._page = None
        self.default_retry_times = 3

    def ready(self, retry_times: int = None, screenshot=True) -> 'BasicObject':
        """
        Check element is ready.

        :param retry_times:
        :param screenshot:
        """
        self.retry_method(
            lambda: self.is_page_loaded(),
            retry_times,
            screenshot
        )
        return self

    def is_ready(self, retry_times: int = None) -> bool:
        """

        Args
        - retry_times:
        """
        try:
            self.ready(
                retry_times,
                False
            )
            return True

        except Exception:
            return False

    def is_page_loaded(self) -> None:
        """
        Pre-loading element or pre-condition
        """
        pass

    def set_remark(self, remark) -> None:
        self.__remark = remark

    def remark(self) -> str:
        return self.__remark

    def is_handle_matcher(self, matcher: callable) -> bool:
        try:
            matcher()
            return True

        except InvalidSelectorException as e:
            return False

        except NoSuchElementException as e:
            return False

        except ElementNotVisibleException as e:
            return False

        except Exception as e:
            logging.error(f'{e}')
            return False

    def handle_matcher(self, matcher: callable) -> WebElement | list[WebElement]:
        try:
            return matcher()

        except InvalidSelectorException as e:
            logging.info(e.msg)
            raise InvalidSelectorExceptions(self.remark())

        except NoSuchElementException as e:
            logging.info(e.msg)
            raise NoSuchElementExceptions(self.remark())

        except ElementNotVisibleException as e:
            logging.info(e.msg)
            raise ElementNotVisibleExceptions(self.remark())

        except Exception as e:
            logging.error(f'{e}')

    def is_matcher_visible(self, matcher: callable) -> bool:
        try:
            matcher().is_displayed()
            return True

        except NoSuchElementException:
            return False

        except ElementNotVisibleException:
            return False

        except Exception as e:
            logging.error(f'{e}')
            return False

    def is_matcher(self, matcher: WebElement) -> bool:
        return self.is_matcher_visible(lambda: self.handle_matcher(matcher))

    def is_matchers_all_visible(self, matcher: callable) -> bool:

        try:
            for element in matcher():
                element.is_displayed()
            if len(matcher()) == 0:
                return False
        except NoSuchElementException:
            return False

        except ElementNotVisibleException:
            return False

        except Exception as e:
            logging.error(f'{e}')
            return False
        return True

    def is_matchers(self, matcher: WebElement) -> bool:
        return self.is_matchers_all_visible(lambda: self.handle_matcher(matcher))

    @staticmethod
    def retry_sleep(current_retry: int, total_retry: int, info="") -> None:
        """
        """
        # for number in range(1, total_retry + 1):
        logging.info(f"⏳ Retry {current_retry}/{total_retry} {info}")
        time.sleep(1)

    def retry_method(self, matcher, retry_count: int = None, screenshot=True) -> None:
        """

        """
        if retry_count is not None:
            self.default_retry_times = retry_count

        retry_count = 0

        while True:
            try:
                matcher()
                return None

            except Exception:
                if retry_count == self.default_retry_times:
                    self.save_screenshot('', f'{self.remark()} failed') if screenshot else None
                    raise NotReadyException(
                        f'❌ {self.remark()} failed after {self.default_retry_times} retries.')
                retry_count += 1
                self.retry_sleep(retry_count, self.default_retry_times)

    def save_screenshot(self, case: str = '', name: str | None = None) -> str | None:
        """
        儲存 png 截圖，並附在 allure report 當中
x
        Args:
        - case: 設定截圖存放的資料夾, 如果沒有 name 時則變為 name
        - name: 設定截圖名稱, 並存為 png
        """
        time.sleep(0.5)

        if name is None:
            name_png = f'{case}.png'
            png_path = os.path.join(GlobalVar.IMAGE_PATH, name_png)
        else:
            case_path = os.path.join(GlobalVar.IMAGE_PATH, case)
            os.makedirs(case_path, exist_ok=True)
            name_png = f'{case}_{name}.png'
            png_path = os.path.join(case_path, name_png)

        DeviceManager.get_driver().save_screenshot(png_path)

        attach_type = allure.attachment_type.PNG
        allure.attach.file(png_path, png_path, attach_type)

        return png_path
