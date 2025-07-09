import time

import pytest
from framework.pre_condition.pre_condition_capp import PreConditionCApp
from data.global_data import Job
from module.common import Utility


class TestSearch(PreConditionCApp):
    case_map = {
        'test_C1177114_follow_job': 'user4',
        'test_C1048039_save_job': 'user4'
    }

    @pytest.mark.P0
    @pytest.mark.android
    def test_C1177114_follow_job(self):

        case = '[一般][關注職務] 確認"關注職務"列表同步更新'

        # 開啟工作說明頁
        self.nav.home_page.search_field.click()
        self.nav.search_menu.search_field.click()
        self.nav.search_menu.search_field_input.clear().send_keys(f'{Job.JOB_NAME_C1048039}')
        self.nav.search_menu.find_company_text.click()
        self.nav.job_list.job_tab.click()
        self.nav.job_list.job(Job.JOB_NAME_C1048039).click()
        self.nav.job_desc_page.job_title.get_text.assert_equals(Job.JOB_NAME_C1048039)
        self.nav.job_desc_page.save_screenshot(case, self.nav.job_desc_page.remark())

        # 關注職務
        if '已關注' in self.nav.job_desc_page.follow_button.attribute('content-desc'):
            self.nav.job_desc_page.follow_button.click()
            time.sleep(2)  # 等待元素text變更
        self.nav.job_desc_page.follow_button.click()
        time.sleep(2)  # 等待元素text變更
        self.nav.job_desc_page.follow_button.get_attribute('content-desc').assert_contain('已關注')

        # 到關於我頁開啟我的關注
        # Utility.go_to_homepage()
        Utility.call_homepage()
        self.nav.nav_bar.about.click()
        self.nav.about_me_page.my_followed_button.click()
        self.nav.my_followed_page.followed_job_button(Job.COMPANY_NAME_C1048039).click()
        self.nav.followed_job_list.title_bar.get_text.assert_equals(Job.COMPANY_NAME_C1048039)

        # 取消關注職務
        self.nav.followed_job_list.followed_job_button(Job.JOB_NAME_C1048039).click()
        self.nav.followed_job_list.followed_job_button(Job.JOB_NAME_C1048039).get_attribute('content-desc').assert_contain('未關注')
        Utility.refresh_page()
        self.nav.followed_job_list.followed_job(Job.JOB_NAME_C1048039).assert_invisible()

    @pytest.mark.P1
    @pytest.mark.android
    def test_C1048039_save_job(self):
        """
        [一般][儲存工作] 確認"儲存工作"列表同步更新
        """
        self.nav.home_page.search_field.click()
        self.nav.search_menu.search_go_button.assert_visible()


