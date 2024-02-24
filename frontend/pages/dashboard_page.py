from flet import *
from utils.extras import *
from flet_route import Params, Basket
from state import update_state, get_state
from navigation import navigate_to

def dashboard_page_view(page: Page, params: Params=None, basket: Basket=None):

    
    
    offset = transform.Offset(0,0,)
    nombre = get_state("nombre")  # Obtiene el nombre  del estado global.
    print(nombre)
    expand = True
    
    logout_btn=Icon(
                icons.LOGOUT_OUTLINED,
                color='black')

    def on_logout_clicked(e):
        navigate_to(page, "/")

    navigation_bar = NavigationBar(
        destinations=[
            NavigationDestination(icon=icons.HOME_OUTLINED, selected_icon=icons.HOME, label="Inicio"),
            NavigationDestination(icon=icons.LOCAL_LAUNDRY_SERVICE_OUTLINED,selected_icon=icons.LOCAL_LAUNDRY_SERVICE, label="Servicios"),
            NavigationDestination(icon=icons.SHOP_OUTLINED, selected_icon=icons.SHOP, label="Pedidos"),
            NavigationDestination(icon=icons.ACCOUNT_CIRCLE_OUTLINED, selected_icon=icons.ACCOUNT_CIRCLE, label="Cuenta")
        ]
    )

    content = Container(
    
        height=altura_base,
        width=anchura_base,
        bgcolor=color_base,
        clip_behavior=ClipBehavior.ANTI_ALIAS,
        expand=True,
        border_radius=radio_borde,
        
        content=Column(
        alignment='center',
        horizontal_alignment='center',
        controls=[
            Text(
            value=f'Buenas!',
            
            ),
            Text(
            value=nombre,
            
            ),
            Container(
            on_click= on_logout_clicked,
            data ='logout',
            height=50,
            width=100,
            border_radius=30,
            bgcolor='white',
            content=logout_btn
            
            ),

        ]
        )
        
    )

    return View("/dashboard", controls=[content,navigation_bar])

