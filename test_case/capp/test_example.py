import pytest
from framework.pre_condition.pre_condition_capp import PreConditionCApp


class TestSearch(PreConditionCApp):
    case_map = {
        'test_aaa': 'user3',
        'test_bbb': 'user3'
    }

    @pytest.mark.P0
    @pytest.mark.android
    def test_aaa(self):
        self.nav.home_page.banner_area.assert_visible()
        self.nav.home_page.fail_ele.assert_visible()

    @pytest.mark.P1
    @pytest.mark.android
    def test_bbb(self):
        self.nav.home_page.search_field.click()
        self.nav.search_menu.search_go_button.assert_visible()


