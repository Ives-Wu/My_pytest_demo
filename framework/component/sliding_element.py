import logging

from appium.webdriver.common.touch_action import TouchAction
from selenium.common import NoSuchElementException
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.action_chains import ActionChains

from framework.component.basic_element import BasicObject
from framework.device_manager import DeviceManager


class SlidingObject(BasicObject):

    def __init__(self):
        super().__init__()
        self.driver = DeviceManager.get_driver()

    def get_window_size(self):
        try:
            return self.driver.get_window_size()
        except Exception as e:
            raise Exception(f"Cannot get window size: {str(e)}")

    def execute_scroll(self, start_x, start_y, end_x, end_y, duration):
        touch_input = PointerInput(interaction.POINTER_TOUCH, "touch")
        actions = ActionBuilder(self.driver, mouse=touch_input)

        start_x = int(start_x)
        start_y = int(start_y)
        end_x = int(end_x)
        end_y = int(end_y)
        duration = int(duration)

        try:
            # 構建滾動動作
            actions.pointer_action.move_to_location(start_x, start_y)  # 移動到起始位置
            actions.pointer_action.pointer_down()  # 按下
            actions.pointer_action.pause(duration / 1000)  # 等待 (注意：duration需要轉換為秒)
            actions.pointer_action.move_to_location(end_x, end_y)  # 移動到終點
            actions.pointer_action.release()  # 釋放
            actions.perform()

        except Exception as e:
            raise Exception(f"Error while sliding: {str(e)}")

    def scroll_down(self):
        window_size = self.get_window_size()
        start_x = window_size['width'] / 2
        start_y = window_size['height'] * 0.8
        end_x = start_x
        end_y = start_y - 120
        duration = 100
        self.execute_scroll(start_x, start_y, end_x, end_y, duration)

    # def scroll_down(self):
    #     window_size = self.get_window_size()
    #     start_x = window_size['width'] / 2
    #     start_y = window_size['height'] * 0.8
    #     end_y = window_size['height'] * 0.2
    #
    #     action = TouchAction(self.driver)
    #     action.press(x=start_x, y=start_y).wait(ms=500).move_to(x=start_x, y=end_y).release().perform()

    def scroll_up(self):
        window_size = self.get_window_size()
        start_x = window_size['width'] / 2
        start_y = window_size['height'] * 0.8
        end_x = start_x
        end_y = start_y + 120
        duration = 100
        self.execute_scroll(start_x, start_y, end_x, end_y, duration)

    def scroll_left(self):
        window_size = self.get_window_size()
        start_x = window_size['width'] * 0.5
        start_y = window_size['height'] / 2
        end_x = start_x + 80
        end_y = start_y
        duration = 100
        self.execute_scroll(start_x, start_y, end_x, end_y, duration)

    def scroll_right(self):
        window_size = self.get_window_size()
        start_x = window_size['width'] * 0.5
        start_y = window_size['height'] / 2
        end_x = start_x - 80
        end_y = start_y
        duration = 100
        self.execute_scroll(start_x, start_y, end_x, end_y, duration)

    def scroll_to_top(self):
        # 需避免滑動範圍太大造成頁面reload
        window_size = self.get_window_size()
        start_x = window_size['width'] / 2
        start_y = window_size['height'] * 0.5
        end_x = start_x
        end_y = window_size['height'] * 0.7
        duration = 100
        [self.execute_scroll(start_x, start_y, end_x, end_y, duration) for _ in range(3)]

    def scroll_to_bottom(self):
        window_size = self.get_window_size()
        start_x = window_size['width'] / 2
        start_y = window_size['height'] * 0.8
        end_x = start_x
        end_y = 0
        duration = 100
        self.execute_scroll(start_x, start_y, end_x, end_y, duration)

    def scroll_to_left(self):
        # 需避免滑動範圍太大造成頁面reload
        window_size = self.get_window_size()
        start_x = window_size['width'] * 0.5
        start_y = window_size['height'] / 2
        end_x = window_size['width'] * 0.7
        end_y = start_y
        duration = 100
        [self.execute_scroll(start_x, start_y, end_x, end_y, duration) for _ in range(3)]

    def horizontal_swipe(self, start_x=None, start_y=None, end_x=None, end_y=None, duration=100):
        """
        Perform a horizontal swipe action.

        - start_x: 起始 x 坐标，默认为窗口宽度的 20%。
        - start_y: 起始 y 坐标，默认为窗口高度的中间位置。
        - end_x: 结束 x 坐标，默认为窗口宽度的 80%。
        - end_y: 结束 y 坐标，默认为起始 y 坐标。
        - duration: 滑动持续时间，默认为 100 毫秒。
        """
        window_size = self.get_window_size()

        # 如果没有提供起始坐标，则使用默认值
        if start_x is None:
            start_x = window_size['width'] * 0.2
        if start_y is None:
            start_y = window_size['height'] / 2

        # 如果没有提供结束坐标，则使用默认值
        if end_x is None:
            end_x = window_size['width'] * 0.8
        if end_y is None:
            end_y = start_y

        # 执行滑动
        self.execute_scroll(start_x, start_y, end_x, end_y, duration)

    def scroll_to_element(self, matcher, scroll_up: bool = False, max_swipes=10):
        """
        Perform a vertical swipe action until the specific element is visible.
        """

        # if not self.is_matcher(matcher):
        #     self.scroll_to_top()
        # else:
        #     logging.info("[Swipe Action] Element is present.")
        #     self._start_adjusting_up(matcher)
        #     return

        # if self.is_matcher(matcher):
        #     logging.info("[Swipe Action] Element is present.")
        #     self._start_adjusting_up(matcher)
        #     return

        for count in range(1, max_swipes + 1):
            try:
                if matcher().is_displayed():
                    logging.info("[Swipe Action] Element is present.")
                    self._start_adjusting_up(matcher)
                    return
            except NoSuchElementException:
                pass

            # 使用滑动
            self.scroll_up() if scroll_up else self.scroll_down()
            logging.info(f"[Swipe Action] Sliding times while finding element ({count}/{max_swipes})")

        self.save_screenshot('垂直滑動失敗', matcher().remark())
        raise Exception("❌ Cannot find element and reach max sliding times.")

    def scroll_horizontal_to_element(self, matcher, scroll_left: bool = False, max_swipes=10):
        """
        Perform a horizontal swipe action until the specific element is visible.
        """

        # if not self.is_matcher(matcher):
        #     self.scroll_to_left()
        # else:
        #     logging.info("[Swipe Action] Element is present.")
        #     self._start_adjusting_up_horizontal(matcher)
        #     return

        for count in range(1, max_swipes + 1):
            try:
                if matcher().is_displayed():
                    logging.info("[Swipe Action] Element is present.")
                    self._start_adjusting_up_horizontal(matcher)
                    return
            except NoSuchElementException:
                pass

            # 使用滑动
            self.scroll_left() if scroll_left else self.scroll_right()
            logging.info(f"[Swipe Action] Sliding times while finding element ({count}/{max_swipes})")

        self.save_screenshot('水平滑動失敗', matcher().remark())
        raise Exception("❌ Cannot find element and reach max sliding times.")


    def _start_adjusting_up(self, matcher, max_adjust: int = 3, max_adjust_android: int = 6):
        """
        Perform a vertical swipe action slightly to make the element is fully visible.
        """
        window_size = self.get_window_size()
        viewable_area = {
            'left_side': 0,
            'top_side': window_size['height'] * 0.17,
            'right_side': window_size['width'],
            'bottom_side': window_size['height'] * 0.8
        }

        distance_from_top = matcher().location['y'] - viewable_area['top_side']
        distance_from_bottom = viewable_area['bottom_side'] - (matcher().location['y'] + matcher().size['height'])

        if distance_from_top > 20 and distance_from_bottom < 0:
            for adjust_times in range(1, max_adjust + 1):
                logging.info(f'[Swipe Action] Start adjusting ({adjust_times}/{max_adjust})')
                start_x = end_x = window_size['width'] * 0.5
                start_y = viewable_area['bottom_side']

                end_y = viewable_area['bottom_side'] - (distance_from_top * 0.6)
                duration = 2000
                self.execute_scroll(start_x, start_y, end_x, end_y, duration)
                distance_from_top = matcher().location['y'] - viewable_area['top_side']
                distance_from_bottom = viewable_area['bottom_side'] - (
                    matcher().location['y'] + matcher().size['height'])
                if distance_from_top < 20 or distance_from_bottom > 0:
                    break
            logging.info('[Swipe Action] End adjusting.')
        else:
            logging.info('[Swipe Action] No need adjusting.')

    def _start_adjusting_up_horizontal(self, matcher, max_adjust: int = 3, max_adjust_android: int = 6):
        """
        Perform a horizontal swipe action slightly to make the element is fully visible.
        """
        window_size = self.get_window_size()

        viewable_area = {
            'left_side': window_size['width'] * 0.17,
            'top_side': 0,
            'right_side': window_size['width'] * 0.8,
            'bottom_side': window_size['height']
        }

        distance_from_left = matcher().location['x'] - viewable_area['left_side']
        distance_from_right = viewable_area['right_side'] - (matcher().location['x'] + matcher().size['width'])

        if distance_from_left > 20 and distance_from_right < 0:
            for adjust_times in range(1, max_adjust + 1):
                logging.info(f'Start adjusting ({adjust_times}/{max_adjust})')
                start_y = end_y = window_size['height'] * 0.5
                start_x = viewable_area['right_side']

                end_x = viewable_area['bottom_side'] - (distance_from_left * 0.6)
                duration = 1000
                self.execute_scroll(start_x, start_y, end_x, end_y, duration)
                distance_from_left = matcher().location['x'] - viewable_area['left_side']
                distance_from_right = viewable_area['right_side'] - (
                    matcher().location['x'] + matcher().size['width'])
                if distance_from_left < 20 or distance_from_right > 0:
                    break
            logging.info('End adjusting.')
        else:
            logging.info('No need adjusting.')


