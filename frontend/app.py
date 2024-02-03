from flet import *
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.sign_up_page import SignupPage
from utils.extras import *

# from pages.dashboard import DashboardPage


class WindowDrag(UserControl):
    def __init__(self):
        super().__init__()
        # self.color = color

    def build(self):
        return Container(
            content=WindowDragArea(height=10, content=Container(bgcolor="white"))
        )


class App(UserControl):
    def __init__(self, pg: Page):
        super().__init__()

        pg.window_title_bar_hidden = True
        pg.window_frameless = True
        pg.window_title_bar_buttons_hidden = True
        pg.bgcolor = colors.TRANSPARENT
        pg.window_bgcolor = colors.TRANSPARENT
        pg.window_width = anchura_base
        pg.window_height = altura_base

        self.pg = pg
        self.pg.spacing = 0
        self.main_page = MainPage()
        self.screen_views = Stack(
            expand=True,
            controls=[
                self.main_page,
                # LoginPage(),
                # SignupPage()
            ],
        )
        self.init_helper()

    def init_helper(self):
        self.pg.add(
            WindowDrag(),
            self.screen_views,
        )


app(target=App, assets_dir="assets", view=AppView.WEB_BROWSER)
