from flet import *
from utils.extras import *
from flet_route import Params, Basket
from state import update_state, get_state

def dashboard_page_view(page: Page, params: Params, basket: Basket):

    offset = transform.Offset(0,0,)
    email = email
    switch_page = switch_page
    expand = True
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
            value=f'Saludos!',
            
            ),
            Text(
            value=f'Tu correo es\n{email}',
            
            ),
            Container(
            on_click= switch_page,
            data ='logout',
            height=50,
            width=100,
            border_radius=30,
            bgcolor='white',
            content=Icon(
                icons.LOGOUT_OUTLINED,
                color='black'
            )
            )
        ]
        )
        
    )
    return View("/dashboard", controls=[content])