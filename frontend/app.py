from flet import *
from pages.main_page import main_page_view
from pages.login_page import login_page_view
from pages.sign_up_page import signup_page_view
from pages.dashboard_page import dashboard_page_view
from utils.extras import *
from flet_route import Routing, path


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
        self.setup_routing()
        self.pg.spacing = 0
        # self.main_page = MainPage()
        # self.screen_views = Stack(
        #     expand=True,
        #     controls=[
        #         # self.main_page,
        #         # LoginPage(),
        #         SignupPage()
        #     ],
        # )
        self.init_helper()

    def init_helper(self):
        self.pg.add(
            WindowDrag(),
            #self.screen_views,
        )
    
    def setup_routing(self):
        app_routes = [
            path(url="/", clear=True, view=main_page_view),
            path(url="/login", clear=True, view=login_page_view),
            path(url="/signup", clear=True, view=signup_page_view),
            path(url="/dashboard", clear=True, view=dashboard_page_view),
        ]
        Routing(page=self.pg, app_routes=app_routes)
        self.pg.go(self.pg.route)

        self.pg.update()

# app(target=App, assets_dir="assets", view=AppView.WEB_BROWSER)
app(target=App, assets_dir="assets")

