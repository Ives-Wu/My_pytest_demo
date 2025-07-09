import inspect
import pytest

from framework.component.basic_element import BasicObject
from framework.component.component import Component


class Components(BasicObject):

    def __init__(self, matchers, remark):
        super().__init__()
        self.set_remark(remark)
        self.matchers = matchers

    def is_page_loaded(self) -> None:
        """
        Pre-loading element or pre-condition
        """
        self.assert_all_visible(False)

    @property
    def texts(self) -> list[str]:
        """
        Return list form all elements.
        """
        self.ready()
        return [element.text for element in self.matchers()]


    @property
    def quantity(self) -> int:
        """
        Return the number of elements.
        """
        return len(self.texts)

    def find(self, index: int) -> Component:
        """
        Return a specific element from the sequence.
        """
        return Component(lambda: self.matchers()[index], remark=self.remark() + f", index: {index}")

    def are_all_visible(self) -> bool:
        return self.is_matchers(self.matchers)

    def assert_all_visible(self, screenshot=True) -> None:
        if not self.are_all_visible():
            self.save_screenshot('', f'{self.remark()} - assert visible') if screenshot else None
            raise Exception(f"{self.remark()} > not visible.")

    def assert_all_invisible(self, screenshot=True) -> None:
        if self.are_all_visible():
            self.save_screenshot('', f'{self.remark()} - assert invisible') if screenshot else None
            raise Exception(f"{self.remark()} > should be hidden.")

    def assume_all_visible(self) -> None:
        caller = inspect.stack()[1]
        pytest.assume(
            self.are_all_visible(),
            f"{self.remark()} - not visible."
            f"Error occurred at {caller.filename}, line {caller.lineno}"
        )

    def assume_all_invisible(self) -> None:
        caller = inspect.stack()[1]
        pytest.assume(
            not self.are_all_visible(),
            f"{self.remark()} - should be hidden."
            f"Error occurred at {caller.filename}, line {caller.lineno}"
        )
