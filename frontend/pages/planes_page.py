from flet import *
from utils.extras import *
from flet_route import Params, Basket
from state import update_state, get_state
from navigation import navigate_to, go_back
from translations import load_translations, gettext as _


def planes_page_view(page: Page, params: Params=None, basket: Basket=None):
    
    selected_index = get_state("selected_nav_index", default=0)
    
    

    nombre = get_state("nombre")  # Obtiene el nombre  del estado global.
    




        
    # def on_navigation_changed(e):
    #     update_state("selected_nav_index", e.control.selected_index)
    #     if e.control.selected_index == 0:
    #         navigate_to(page, "/inicio")
    #     elif e.control.selected_index == 1:
    #         navigate_to(page, "/servicios")
    #     elif e.control.selected_index == 2:
    #         navigate_to(page, "/pedidos")
    #     elif e.control.selected_index == 3:
    #         navigate_to(page, "/cuenta")
    
    # navigation_bar = NavigationBar(
    #     destinations=[
    #         NavigationDestination(icon=icons.HOME_OUTLINED, selected_icon=icons.HOME, label="Inicio"),
    #         NavigationDestination(icon=icons.LOCAL_LAUNDRY_SERVICE_OUTLINED,selected_icon=icons.LOCAL_LAUNDRY_SERVICE, label="Servicios"),
    #         NavigationDestination(icon=icons.SHOP_OUTLINED, selected_icon=icons.SHOP, label="Pedidos"),
    #         NavigationDestination(icon=icons.ACCOUNT_CIRCLE_OUTLINED, selected_icon=icons.ACCOUNT_CIRCLE, label="Cuenta")
    #     ],
    #     selected_index=selected_index,
    #     on_change=on_navigation_changed
    # )
    #dashboard_content = Container(
        #height=720,
    #     content=Column(
    #         alignment="end",
    #         controls=[
    #             #navigation_bar
    #         ]
    #     )
    # )

    # plan_name = Container(
    #     content=Row(
    #         controls=[
    #             Text(
    #                 value=f'No Plan', # TODO: Configurar Nombre del Plan  
    #                 size=12,
    #                 weight=FontWeight.BOLD,
    #     )
    #     ],
    #     alignment=MainAxisAlignment.CENTER,
    #     )
    
    # )
    container_go_back = Container(
                                on_click = lambda e: go_back(page),
                                content=Icon(
                                    icons.ARROW_BACK_IOS_OUTLINED, size=28
                                ),
                            )
    
    container_name = Container(
        content=Row(
            controls=[
                container_go_back,
                Text(
                    value=_("plans"), 
                    weight=FontWeight.BOLD, 
                    size=24,color=colors.WHITE),
                
            ]
        ),
        padding=Padding(15,20,5,15),
        bgcolor=blue_base,
        width=anchura_base,
        height=80
    )


    planes_text_title = Text(
        value=_("pick_plan"), style=TextStyle(size=24, weight=FontWeight.BOLD)
    )

    plan_small__text_name = Text(value=_("plan_small"),weight=FontWeight.W_500, 
        size=24,color=colors.BLACK) 
    
    plan_small_btn = FilledButton(
        content=Text(value=_("subscribe").upper(), size=24, weight=FontWeight.BOLD),
        width=200,
        height=altura_btn,  
        on_click=print("suscribiendo"),
        style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=10), bgcolor=colors.BLUE_200)
                
)
    plan_small_container = Container(
        content=Column(
            controls=[
            
                plan_small__text_name,
                plan_small_btn
            ],horizontal_alignment=CrossAxisAlignment.CENTER, 
            alignment=MainAxisAlignment.CENTER
        ),
        
        image_src="https://jsavinong.github.io/Lala-vanderia-App/frontend/assets/images/Plan Small.jpg",
        image_fit=ImageFit.COVER,
        height=400,
        width= 250,
        border_radius=50,
        bgcolor=colors.WHITE60
        
        
    )

    plan_medium__text_name = Text(value=_("plan_medium"),weight=FontWeight.W_500, 
        size=24,color=colors.BLACK) 
    
    plan_medium_btn = FilledButton(
        content=Text(value=_("subscribe").upper(), size=24, weight=FontWeight.BOLD),
        width=200,
        height=altura_btn,  
        on_click=print("suscribiendo"),
        style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=10), bgcolor=colors.BLUE_200)
                
)
    plan_medium_container = Container(
        content=Column(
            controls=[
            
                plan_medium__text_name,
                plan_medium_btn
            ],horizontal_alignment=CrossAxisAlignment.CENTER, 
            alignment=MainAxisAlignment.CENTER
        ),
        
        image_src="https://jsavinong.github.io/Lala-vanderia-App/frontend/assets/images/Plan Medium.jpg",
        image_fit=ImageFit.COVER,
        height=400,
        width= 250,
        border_radius=50,
        bgcolor=colors.WHITE60
        
        
    )

    plan_large__text_name = Text(value=_("plan_large"),weight=FontWeight.W_500, 
        size=24,color=colors.BLACK) 
    
    plan_large_btn = FilledButton(
        content=Text(value=_("subscribe").upper(), size=24, weight=FontWeight.BOLD),
        width=200,
        height=altura_btn,  
        on_click=print("suscribiendo"),
        style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=10), bgcolor=colors.BLUE_200)
                
)
    plan_large_container = Container(
        content=Column(
            controls=[
            
                plan_large__text_name,
                plan_large_btn
            ],horizontal_alignment=CrossAxisAlignment.CENTER, 
            alignment=MainAxisAlignment.CENTER
        ),
        
        image_src="https://jsavinong.github.io/Lala-vanderia-App/frontend/assets/images/Plan Large.jpg",
        image_fit=ImageFit.COVER,
        height=400,
        width= 250,
        border_radius=50,
        bgcolor=colors.WHITE60
        
        
    )

    planes_row = Row(
        controls=[
                Container(width=10),
                plan_small_container,
                Container(width=10),
                plan_medium_container,
                Container(width=10),
                plan_large_container,
                Container(width=10),

        ],scroll="auto",
        vertical_alignment=CrossAxisAlignment.CENTER,
        alignment=MainAxisAlignment.SPACE_EVENLY,
        spacing=50,
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
        bgcolor=colors.BLUE_GREY_900,
        clip_behavior=ClipBehavior.ANTI_ALIAS,
        expand=True,
        #border_radius=radio_borde,
        
        content=Column(
            controls=[
                Container(height=10),
                planes_text_title,
                Container(height=10),
                planes_row,
                Container(height=10),
                # faq_textbtn,
                # terminos_de_uso_textbtn,
                

            ],
            horizontal_alignment=CrossAxisAlignment.CENTER
            ),
        
        
    )
    
    return View("/planes", controls=[container_name, content, ])
