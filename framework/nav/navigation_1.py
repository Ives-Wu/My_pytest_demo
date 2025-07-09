from framework.nav.navigation_capp_page import NavCApp


class Nav:

    @property
    def capp(self) -> NavCApp:
        return NavCApp()


