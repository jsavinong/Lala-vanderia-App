from flet import *
from utils.extras import *
from flet_route import Params, Basket
from state import update_state, get_state
from navigation import navigate_to


def cuenta_db_page_view(page: Page, params: Params=None, basket: Basket=None):
    
    selected_index = get_state("selected_nav_index", default=0)
    
    content = Column(controls=[Text("Página de Cuenta")])

    nombre = get_state("nombre")  # Obtiene el nombre  del estado global.
    

    def on_logout_clicked(e):
        navigate_to(page, "/")

    logout_btn=Container(
        on_click=on_logout_clicked,
        content=Row(
            width=200,
            alignment=MainAxisAlignment.CENTER,
            
            controls=[
                Text(
                    "Log out",
                    color='white' 
                    )
                ]
            )
            
        )
    


        
    def on_navigation_changed(e):
        update_state("selected_nav_index", e.control.selected_index)
        if e.control.selected_index == 0:
            navigate_to(page, "/inicio")
        elif e.control.selected_index == 1:
            navigate_to(page, "/servicios")
        elif e.control.selected_index == 2:
            navigate_to(page, "/pedidos")
        elif e.control.selected_index == 3:
            navigate_to(page, "/cuenta")
    
    navigation_bar = NavigationBar(
        destinations=[
            NavigationDestination(icon=icons.HOME_OUTLINED, selected_icon=icons.HOME, label="Inicio"),
            NavigationDestination(icon=icons.LOCAL_LAUNDRY_SERVICE_OUTLINED,selected_icon=icons.LOCAL_LAUNDRY_SERVICE, label="Servicios"),
            NavigationDestination(icon=icons.SHOP_OUTLINED, selected_icon=icons.SHOP, label="Pedidos"),
            NavigationDestination(icon=icons.ACCOUNT_CIRCLE_OUTLINED, selected_icon=icons.ACCOUNT_CIRCLE, label="Cuenta")
        ],
        selected_index=selected_index,
        on_change=on_navigation_changed
    )
    dashboard_content = Container(
        #height=720,
        content=Column(
            alignment="end",
            controls=[
                navigation_bar
            ]
        )
    )
    
    content = Container(
    
        height=altura_base,
        width=anchura_base,
        bgcolor=color_base,
        clip_behavior=ClipBehavior.ANTI_ALIAS,
        expand=True,
        #border_radius=radio_borde,
        
        content=Column(
            #alignment='center',
            #horizontal_alignment='center',
            controls=[
                Container(height=10),
                Text(
                value=f'Buenas Cuenta!',
                height=50, 
                width=200,
                text_align=TextAlign.CENTER,
                weight=FontWeight.BOLD,
                size=24 

            
                
                ),
                
                logout_btn
                #dashboard_content,
                #content_text
            ]
            ),
        
        
    )
    
    return View("/cuenta", controls=[content, dashboard_content])
