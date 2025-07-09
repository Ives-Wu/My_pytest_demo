from module.login_manager import LoginManager

class NavCSub:

    def __init__(self):
        self.__login_manager = None

    @property
    def login_manager(self) -> LoginManager:
        if self.__login_manager is None:
            self.__login_manager = LoginManager()
        return self.__login_manager