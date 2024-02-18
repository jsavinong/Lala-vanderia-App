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
            
            )
        ]
        )
        
    )
    navigation_bar = NavigationBar(
        destinations=[
            NavigationDestination(icon=icons.EXPLORE, label="Explore"),
            NavigationDestination(icon=icons.COMMUTE, label="Commute"),
            NavigationDestination(
                icon=icons.BOOKMARK_BORDER,
                selected_icon=icons.BOOKMARK,
                label="Bookmarks",
            ),
        ]
    )
    return View("/dashboard", controls=[content,navigation_bar])

