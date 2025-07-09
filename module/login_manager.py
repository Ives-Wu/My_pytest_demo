import logging
from module.common import Utility
from framework.nav.navigation_1 import Nav

class LoginManager:

    def __init__(self):
        self.nav = Nav().capp

    def login(self, identity: str, password: str):
        """
        """
        if self.nav.active_page.content.is_ready():
            logging.info('第一次登入')
            self.nav.active_page.nav_login_text.click()
            self.nav.login_page.identity_field.send_keys(identity)
            self.nav.login_page.next_and_login_button.click()
            self.nav.login_page.password_field.send_keys(password)
            self.nav.login_page.next_and_login_button.click()
            Utility.skip_popup(self.nav.popup_page.allow_noti_content, self.nav.popup_page.allow_noti_accept_button)
            self.nav.home_page.ready()
        elif self.nav.home_page.ready():
            logging.info('已在首頁，非第一次登入')
            self.nav.nav_bar.about.click()
            pass
        else:
            logging.error('❌ 出現非預期頁面')

    def logout(self):
        """
        """
        if not self.nav.nav_bar.about.is_ready(3):
            logging.error('❌ 關於我按鈕不存在，需在有關於我按鈕的頁面執行')
            return

        self.nav.nav_bar.about.click()
        self.nav.about_me_page.account_and_assist.click()
        if self.nav.account_and_assist_page.logout.is_ready():
            self.nav.account_and_assist_page.logout.click()
            Utility.skip_popup(self.nav.logout_popup.title_, self.nav.logout_popup.accept_button)
        elif self.nav.account_and_assist_page.login_and_signup.is_ready(0):
            logging.error('❌ 已是登出狀態')
        else:
            logging.error('❌ 出現非預期頁面')

