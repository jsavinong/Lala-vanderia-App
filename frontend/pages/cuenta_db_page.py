from flet import *
from utils.extras import *
from flet_route import Params, Basket
from state import update_state, get_state, actualizar_indice_navegacion
from navigation import navigate_to


def cuenta_db_page_view(page: Page, params: Params=None, basket: Basket=None):
    
    selected_index = get_state("selected_nav_index", default=0)
    
    content = Column(controls=[Text("Página de Cuenta")])

    nombre = get_state("nombre")  # Obtiene el nombre  del estado global.
    

    def on_logout_clicked(e):
        actualizar_indice_navegacion(0)
        navigate_to(page, "/")
    
    logout_btn = TextButton(
        content=Row(
            controls=[
                Text(" Cerrar sesión", style=TextStyle(size=18, color=colors.WHITE))  
            ],
            alignment="left",
        ),
        on_click=on_logout_clicked
    )
    
    def on_click_suscribir(e):
        navigate_to(page, "/planes")

        
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

    plan_name = Container(
        content=Row(
            controls=[
                Text(
                    value=f'No Plan', # TODO: Configurar Nombre del Plan  
                    size=12,
                    weight=FontWeight.BOLD,
        )
        ],
        alignment=MainAxisAlignment.CENTER,
        )
    
    )
    
    container_name = Container(
        content=Column(
            controls=[
                Text(
                    value=nombre, 
                    weight=FontWeight.BOLD, 
                    size=24,color=colors.WHITE),
                plan_name
            ]
        ),
        padding=15,
        bgcolor=blue_base,
        width=anchura_base,
        height=80
    )


    suscribir_btn = FilledButton(
        content=Text(value="SUSCRIBIR", size=24, weight=FontWeight.BOLD),
        width=anchura_btn,
        height=altura_btn,  
        on_click=on_click_suscribir,
        style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=10), bgcolor=colors.BLUE_100)
                
)
    
    faq_textbtn = TextButton(
        content=Row(
            controls=[
                Icon(icons.QUESTION_ANSWER, size=24),  
                Text("  FAQ", style=TextStyle(size=18)),  
            ],
            alignment="left",
        ),
        on_click=lambda e: print("Botón presionado"),  # Reemplaza esto con tu función de callback real
    )
    

    terminos_de_uso_textbtn = TextButton(
        content=Row(
            controls=[
                Icon(icons.DESCRIPTION, size=24),  
                Text(" Términos de uso", style=TextStyle(size=18)),  
            ],
            alignment="left",
        ),
        on_click=lambda e: print("Botón presionado"),  # Reemplaza esto con tu función de callback real
    )
    
    content = Container(
    
        height=altura_base,
        width=anchura_base,
        bgcolor=color_base,
        clip_behavior=ClipBehavior.ANTI_ALIAS,
        expand=True,
        #border_radius=radio_borde,
        
        content=Column(
            controls=[
                container_name,
                Container(height=10),
                suscribir_btn,
                Container(height=10),
                faq_textbtn,
                Divider(),
                terminos_de_uso_textbtn,
                Divider(),
                logout_btn

            ],
            horizontal_alignment=CrossAxisAlignment.CENTER
            ),
        
        
    )
    
    return View("/cuenta", controls=[content, dashboard_content])
