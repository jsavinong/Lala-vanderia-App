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
from utils.extras import *
from flet_route import Routing, path
from config.translations import load_translations


# from pages.dashboard import DashboardPage

# Carga las traducciones para el idioma deseado al inicio de tu aplicación
load_translations("en")  # Cargando inglés por defecto

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

        pg.window_title_bar_hidden = True  # Muestra la barra de título para poder arrastrar la ventana
        pg.window_frameless = False  # La ventana con bordes permite redimensionar
        pg.window_title_bar_buttons_hidden = True  # Muestra botones de la barra de título para cerrar, minimizar, etc.
        pg.bgcolor = colors.WHITE  # Define un color de fondo estándar para la ventana
        pg.window_width = 0  # Establece el ancho inicial de la ventana, 0 para automático
        pg.window_height = 700  # Establece la altura inicial de la ventana, 0 para automático
        pg.window_min_width = 400  # Establece el mínimo ancho permitido para la ventana
        pg.window_min_height = 300  # Establece el mínimo altura permitido para la ventana
        pg.window_resizable = True  # Permite que la ventana sea redimensionable
        
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
            #path(url="/dashboard", clear=True, view=dashboard_page_view),
            path(url="/inicio", clear=True, view=inicio_db_page_view),
            path(url="/servicios", clear=True, view=servicios_db_page_view),
            path(url="/pedidos", clear=True, view=pedidos_db_page_view),
            path(url="/cuenta", clear=True, view=cuenta_db_page_view),
            path(url="/planes", clear=True, view=planes_page_view),
        ]
        Routing(page=self.pg, app_routes=app_routes)
        self.pg.go(self.pg.route)

        self.pg.update()

app(target=App, assets_dir="assets", view=AppView.WEB_BROWSER)
#app(target=App, assets_dir="assets")

