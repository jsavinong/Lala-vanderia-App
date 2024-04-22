from flet import *
from pages.main_page import main_page_view
from pages.login_page import login_page_view
from pages.sign_up_page import signup_page_view
#from pages.dashboard_page import dashboard_page_view
from pages.inicio_db_page import inicio_db_page_view
from pages.servicios_db_page import servicios_db_page_view
from pages.pedidos_db_page import pedidos_db_page_view
from pages.cuenta_db_page import cuenta_db_page_view
from pages.planes_page import planes_page_view
from pages.idioma import idioma_page_view
from pages.splash_screen import splash_screen_view
from utils.extras import *
from flet_route import Routing, path
from translations import load_translations


# from pages.dashboard import DashboardPage

# Carga las traducciones para el idioma deseado al inicio de tu aplicación
load_translations("es")  # Cargando inglés por defecto

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

        self.pg = pg
        self.setup_ui()
        self.setup_routing()

    def setup_ui(self):
        # Configuración inicial de la UI
        self.pg.window_title_bar_hidden = False
        self.pg.window_frameless = False
        self.pg.window_title_bar_buttons_hidden = True
        self.pg.bgcolor = colors.WHITE
        self.pg.window_resizable = True
        self.pg.vertical_alignment = "center"
        self.pg.horizontal_alignment = "center"
        self.pg.padding = 0
        self.pg.add(WindowDrag())
    
    def setup_routing(self):
        app_routes = [
            path(url="/", clear=True, view=main_page_view),
            path(url="/login", clear=True, view=login_page_view),
            path(url="/signup", clear=True, view=signup_page_view),
            #path(url="/dashboard", clear=True, view=dashboard_page_view),
            path(url="/inicio", clear=True, view=inicio_db_page_view),
            path(url="/servicios", clear=True, view=servicios_db_page_view),
            path(url="/pedidos", clear=True, view=pedidos_db_page_view),
            path(url="/cuenta", clear=True, view=cuenta_db_page_view),
            path(url="/planes", clear=True, view=planes_page_view),
            path(url="/idioma", clear=True, view=idioma_page_view),
            path(url="/splash", clear=True, view=splash_screen_view),
        ]
        Routing(page=self.pg, app_routes=app_routes)
        self.pg.go(self.pg.route)
        #self.pg.go("/idioma")
        #self.pg.go("/splash")
        #self.pg.update()

app(target=App, assets_dir="assets", view=AppView.WEB_BROWSER)
#app(target=App, assets_dir="assets")

