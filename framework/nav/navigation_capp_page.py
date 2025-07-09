from appium import webdriver
from framework.device_manager import DeviceManager

from page.capp.common import CommonPage
from page.capp.nav_bar import NavBar
from page.capp.home import HomePage
from page.capp.login import LoginPage
from page.capp.popup import PopUpPage
from page.capp.search_menu import SearchMenu
from page.capp.active.active import ActivePage
from page.capp.about_me.about_me import AboutMePage
from page.capp.about_me.account_and_assist import AccountAndAssistPage, LogoutPopUp
from page.capp.about_me.my_followed import MyFollowed, FollowedJobList
from page.capp.job_list import JobList
from page.capp.job_desc import JobDesc

# from module.login_manager import LoginManager

class NavCApp:

    def __init__(self):

        # Page
        self.__login_page = None
        self.__popup_page = None
        self.__common_page = None
        self.__nav_bar = None
        self.__home_page = None
        self.__search_menu = None
        self.__active_page = None
        self.__about_me_page = None
        self.__account_and_assist_page = None
        self.__logout_popup = None
        self.__job_list = None
        self.__job_desc = None
        self.__my_followed_page = None
        self.__followed_job_list = None

    @property
    def driver(self) -> webdriver:
        return DeviceManager.get_driver()

    @property
    def login_page(self) -> LoginPage:
        if self.__login_page is None:
            self.__login_page = LoginPage().ready()
        return self.__login_page

    @property
    def popup_page(self) -> PopUpPage:
        if self.__popup_page is None:
            self.__popup_page = PopUpPage().ready()
        return self.__popup_page

    @property
    def common_page(self) -> CommonPage:
        if self.__common_page is None:
            self.__common_page = CommonPage().ready()
        return self.__common_page

    @property
    def nav_bar(self) -> NavBar:
        if self.__nav_bar is None:
            self.__nav_bar = NavBar().ready()
        return self.__nav_bar

    @property
    def home_page(self) -> HomePage:
        if self.__home_page is None:
            self.__home_page = HomePage().ready()
        return self.__home_page

    @property
    def search_menu(self) -> SearchMenu:
        if self.__search_menu is None:
            self.__search_menu = SearchMenu().ready()
        return self.__search_menu

    @property
    def active_page(self) -> ActivePage:
        if self.__active_page is None:
            self.__active_page = ActivePage().ready()
        return self.__active_page

    @property
    def about_me_page(self) -> AboutMePage:
        if self.__about_me_page is None:
            self.__about_me_page = AboutMePage().ready()
        return self.__about_me_page

    @property
    def account_and_assist_page(self) -> AccountAndAssistPage:
        if self.__account_and_assist_page is None:
            self.__account_and_assist_page = AccountAndAssistPage().ready()
        return self.__account_and_assist_page

    @property
    def logout_popup(self) -> LogoutPopUp:
        if self.__logout_popup is None:
            self.__logout_popup = LogoutPopUp().ready()
        return self.__logout_popup

    @property
    def job_list(self) -> JobList:
        if self.__job_list is None:
            self.__job_list = JobList().ready()
        return self.__job_list

    @property
    def job_desc_page(self) -> JobDesc:
        if self.__job_desc is None:
            self.__job_desc = JobDesc().ready()
        return self.__job_desc

    @property
    def my_followed_page(self) -> MyFollowed:
        if self.__my_followed_page is None:
            self.__my_followed_page = MyFollowed().ready()
        return self.__my_followed_page

    @property
    def followed_job_list(self) -> FollowedJobList:
        if self.__followed_job_list is None:
            self.__followed_job_list = FollowedJobList().ready()
        return self.__followed_job_list

