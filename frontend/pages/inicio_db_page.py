from flet import *
from utils.extras import *
from flet_route import Params, Basket
from state import update_state, get_state
from navigation import navigate_to
from config.translations import gettext as _


def inicio_db_page_view(page: Page, params: Params=None, basket: Basket=None):
    

    selected_index = get_state("selected_nav_index", default=0)
    
    #
    nombre = get_state("nombre")  # Obtiene el nombre  del estado global.
    




        
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
            NavigationDestination(icon=icons.HOME_OUTLINED, selected_icon=icons.HOME, label=_("home")),
            NavigationDestination(icon=icons.LOCAL_LAUNDRY_SERVICE_OUTLINED,selected_icon=icons.LOCAL_LAUNDRY_SERVICE, label=_("services")),
            NavigationDestination(icon=icons.SHOP_OUTLINED, selected_icon=icons.SHOP, label=_("orders")),
            NavigationDestination(icon=icons.ACCOUNT_CIRCLE_OUTLINED, selected_icon=icons.ACCOUNT_CIRCLE, label=_("acc"))
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

    # user_name = Container(
    #     content=Row(
    #         controls=[
    #             Text(
    #                 value=nombre,
    #                 size=12,
    #                 weight=FontWeight.BOLD,
    #     )
    #     ],
    #     alignment=MainAxisAlignment.CENTER,
    #     )
    
    # )
    
    container_name = Container(
        content=Row(
            controls=[
                Text(
                    value=_("welcome"),
                    weight=FontWeight.BOLD, 
                    size=24,color=colors.WHITE),
                Text(
                    value=nombre,
                    size=24,
                    weight=FontWeight.BOLD,
        )
            ]
        ),
        padding=Padding(15,20,5,15),
        bgcolor=blue_base,
        width=anchura_base,
        height=80
    )



    
    # faq_textbtn = TextButton(
    #     content=Row(
    #         controls=[
    #             Icon(icons.QUESTION_ANSWER, size=24),  
    #             Text("  FAQ", style=TextStyle(size=18)),  
    #         ],
    #         alignment="left",
    #     ),
    #     on_click=lambda e: print("Botón presionado"),  # Reemplaza esto con tu función de callback real
    # )
    

    # terminos_de_uso_textbtn = TextButton(
    #     content=Row(
    #         controls=[
    #             Icon(icons.DESCRIPTION, size=24),  
    #             Text(" Términos de uso", style=TextStyle(size=18)),  
    #         ],
    #         alignment="left",
    #     ),
    #     on_click=lambda e: print("Botón presionado"),  # Reemplaza esto con tu función de callback real
    # )
    
    content = Container(
    
        height=altura_base,
        width=anchura_base,
        bgcolor=color_base,
        clip_behavior=ClipBehavior.ANTI_ALIAS,
        expand=True,
        #border_radius=radio_borde,
        
        content=Column(
            controls=[
                
                #user_name,
                Container(height=10),
                Container(height=10),
                # faq_textbtn,
                # terminos_de_uso_textbtn,

            ],
            horizontal_alignment=CrossAxisAlignment.CENTER
            ),
        
        
    )
    
    return View("/inicio", controls=[container_name, content, dashboard_content])
