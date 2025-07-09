from framework.nav.navigation_capp_page import NavCApp
from framework.nav.navigation_bapp_page import NavBApp


class Nav:

    @property
    def capp(self) -> NavCApp:
        return NavCApp()

    @property
    def bapp(self) -> NavBApp:
        return NavBApp()

