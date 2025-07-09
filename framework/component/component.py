import pytest
import inspect
import logging

from framework.component.basic_element import BasicObject
from framework.component.string_element import BasicString
from module.common import Utility


class Component(BasicObject):

    def __init__(self, matcher, remark):
        super().__init__()
        self.set_remark(remark)
        self.matcher = matcher

    def is_page_loaded(self) -> None:
        """
        Pre-loading element or pre-condition
        """
        self.assert_visible(False)

    def send_keys(self, text) -> None:
        logging.info(f"{self.remark()} - 輸入({text}) ")
        self.ready()
        self.matcher().send_keys(text)

    def click(self) -> None:
        self.ready()
        logging.info(f"{self.remark()} - 點擊")
        self.matcher().click()

    @property
    def get_coordinates_and_size(self) -> dict[str, int]:
        """
        ['x']: 'x'
        ['y']: 'y'
        ['width']: 'width'
        ['height']: 'height'
        """
        self.ready()

        logging.info(f"{self.remark()} - 回傳 x, y 座標和長寬")
        return {
            'x': self.matcher().location['x'],
            'y': self.matcher().location['y'],
            'width': self.matcher().size['width'],
            'height': self.matcher().size['height']
        }

    @property
    def get_center_coordinates(self) -> dict[str, int]:
        self.ready()

        x = self.matcher().location['x'] + self.matcher().size['width'] * 0.5
        y = self.matcher().location['y'] + self.matcher().size['height'] * 0.5
        logging.info(f"{self.remark()} - 回傳中心點位置")
        return {
            'x': int(x),
            'y': int(y)
        }

    def tap_center(self) -> None:
        self.ready()
        logging.info(f"{self.remark()} - 點擊中心點")
        x = self.get_center_coordinates['x']
        y = self.get_center_coordinates['y']
        Utility.tap([(x, y)])

    def clear(self):
        logging.info(f"{self.remark()} - clear")
        self.ready()
        self.matcher().clear()
        return self.matcher()

    def input(self, text):
        logging.info(f"{self.remark()} - input({text}) ")
        self.ready()
        self.matcher().send_keys(text)

    @property
    def text(self) -> str:
        """
        Return the text from the element.
        """
        self.ready()
        return self.matcher().text

    @property
    def get_text(self):
        """
        Return the text from the element for validation.
        """
        self.ready()
        logging.info(f'{self.remark()} - get string below: ')
        return BasicString(
            lambda: self.matcher().text,
            f'{self.remark()} - get string',
        )

    @property
    def value(self) -> str:
        """
        Return the value from the element.
        """
        logging.info(f"{self.remark()} - get value ('{self.matcher().get_attribute('value')}')")
        self.ready()
        return self.matcher().get_attribute("value")

    @property
    def get_value(self):
        """
        Return the value from the element for validation.
        """
        self.ready()
        logging.info(f'{self.remark()} - get value below: ')
        return BasicString(
            lambda: self.matcher().get_attribute("value"),
            f"{self.remark()} - string ('{self.matcher().get_attribute('value')}')"
        )

    def attribute(self, attr) -> str:
        """
        Return the attribute from the element.
        """
        logging.info(f"{self.remark()} - get attribute ('{self.matcher().get_attribute(attr)}')")
        self.ready()
        return self.matcher().get_attribute(attr)

    def get_attribute(self, attr):
        """
        Return the attribute from the element for validation.
        """
        self.ready()
        logging.info(f'{self.remark()} - get attribute below: ')
        return BasicString(
            lambda: self.matcher().get_attribute(attr),
            f"{self.remark()} - string ('{self.matcher().get_attribute(attr)}')"
        )

    def is_visible(self) -> bool:
        return self.is_matcher(self.matcher)

    def assert_visible(self, screenshot=True) -> None:
        if not self.is_visible():
            self.save_screenshot('', f'{self.remark()} - assert visible') if screenshot else None
            raise Exception(f"{self.remark()} - not visible.")

    def assert_invisible(self, screenshot=True) -> None:
        if self.is_visible():
            self.save_screenshot('', f'{self.remark()} - assert invisible') if screenshot else None
            raise Exception(f"{self.remark()} - should be hidden.")

    def assume_visible(self) -> None:
        caller = inspect.stack()[1]
        pytest.assume(
            self.is_visible(),
            f"{self.remark()} - not visible.\n"
            f"Error occurred at {caller.filename}, line {caller.lineno}"
        )

    def assume_invisible(self) -> None:
        caller = inspect.stack()[1]
        pytest.assume(
            not self.is_visible(),
            f"{self.remark()} - should be hidden.\n"
            f"Error occurred at {caller.filename}, line {caller.lineno}"
        )

    def assume_clickable(self) -> None:
        caller = inspect.stack()[1]
        pytest.assume(
            self.is_visible() and self.is_clickable(),
            f"{self.remark()} - clickable.\n"
            f"Error occurred at {caller.filename}, line {caller.lineno}"
        )

    def assume_not_clickable(self) -> None:
        caller = inspect.stack()[1]
        pytest.assume(
            not self.is_visible() or not self.is_clickable(),
            f"{self.remark()} - Element should not be clickable or visible.\n"
            f"Error occurred at {caller.filename}, line {caller.lineno}"
        )

    def is_clickable(self) -> bool:
        return self.matcher().is_enabled()

    def assert_clickable(self, screenshot=True) -> None:
        """
        Raise Exception and stop testing.
        """
        if self.is_visible():
            if not self.is_clickable():
                self.save_screenshot('', f'{self.remark()} - assert clickable') if screenshot else None
                raise Exception(f"{self.remark()} - not clickable.")
        else:
            raise Exception(f"{self.remark()} - not visible.")

    def assert_not_clickable(self, screenshot=True) -> None:
        """
        Raise Exception and stop testing.
        """
        if self.is_visible():
            if self.is_clickable():
                self.save_screenshot('', f'{self.remark()} - assert not clickable') if screenshot else None
                raise Exception(f"{self.remark()} - clickable.")
        else:
            raise Exception(f"{self.remark()} - not visible.")
