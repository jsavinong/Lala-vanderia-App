from flet import *
from utils.extras import *
from flet_route import Params, Basket
from state import update_state, get_state
from navigation import navigate_to
from translations import gettext as _

def servicios_db_page_view(page: Page, params: Params=None, basket: Basket=None):
    
    selected_index = get_state("selected_nav_index", default=0)
    
    #content = Column(controls=[Text("Página de Cuenta")])

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
    
    def agregar_servicio(e):
        contador_servicios = get_state("contador_servicios", default=0) + 1  # Obtiene el contador actual y lo incrementa
        update_state("contador_servicios", contador_servicios)  # Actualiza el contador en el estado global
        ver_pedido_btn.text = f"Ver pedido ({contador_servicios})"  # Actualiza el texto del botón
        ver_pedido_btn.visible = True  # Asegura que el botón sea visible
        page.update()  # Actualiza la UI

    def ver_pedido(e):
        pass

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

    servicio_text_title = Text(
        value=_("pick_service"), style=TextStyle(size=24, weight=FontWeight.BOLD)
    )

    servicio_lavado_img = Container(
        content=Column(
            controls=[
                Image(src="https://jsavinong.github.io/Lala-vanderia-App/frontend/assets/images/lavado.jpg", 
                    border_radius=10,),
                Text(value=_("washing_service"), size=20, style=TextStyle(weight="bold")),
                FilledTonalButton(_("add"), icon="add", on_click=agregar_servicio, style=ButtonStyle(shape=RoundedRectangleBorder(radius=10)))
            ],
            #height=200, width=200
            horizontal_alignment=CrossAxisAlignment.CENTER,
        ), 
        height=200,
        width=200,
        #ink=True,
        on_click=lambda e: print("clicked")
    )

    servicio_planchado_img = Container(
        content=Column(
            controls=[
                Image(src="https://jsavinong.github.io/Lala-vanderia-App/frontend/assets/images/planchado.jpg", border_radius=10),
                Text(value=_("drying_service"), size=20, style=TextStyle(weight="bold")),
                FilledTonalButton(_("add"), icon="add", style=ButtonStyle(shape=RoundedRectangleBorder(radius=10)))
            ],
            horizontal_alignment=CrossAxisAlignment.CENTER,
        ),
        height=200,
        width=200,
        on_click=lambda e: print("clicked")
    )

    ver_pedido_btn = Container(content= 
        FilledButton(content=Text(value=_("view_order")+" (0)", size=20), visible=True, on_click=ver_pedido, 
            style=ButtonStyle(shape=RoundedRectangleBorder(radius=10)),), width=300)

    

    # test = Container(
    #                 content=Text("Clickable transparent with Ink"),
    #                 margin=10,
    #                 padding=10,
    #                 alignment=alignment.center,
    #                 width=150,
    #                 height=150,
    #                 border_radius=10,
    #                 ink=True,
    #                 on_click=lambda e: print("Clickable transparent with Ink clicked!")
    # )
    container_name = Container(
        content=Column(
            controls=[
                Text(
                    value=_("services"), 
                    weight=FontWeight.BOLD, 
                    size=24,color=colors.WHITE)
            ]
        ),
        padding=Padding(15,20,5,15),
        bgcolor=blue_base,
        width=anchura_base,
        height=80,
    )

    content = Container(
    
        bgcolor=colors.BLUE_GREY_900,
        #border_radius=radio_borde,
        
        content=Column(
            controls=[
                Container(height=10),
                servicio_text_title,
                Divider(),
                #Container(height=10),
                servicio_lavado_img,
                Divider(),
                servicio_planchado_img,
                Divider(),
                #test
                # faq_textbtn,
                # terminos_de_uso_textbtn,

            ],
            horizontal_alignment=CrossAxisAlignment.CENTER,
            scroll="auto"
            ),
        
    )

    content_stack = Stack(
        [
            content
            ,
            Row(controls=[
                Column(
                    controls=[
                        ver_pedido_btn,
                    ],
                    alignment=MainAxisAlignment.END,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    
                    
                ),
                
        ], 
        #left=100,
        #top=470,
        )

            
        ],
        height=altura_base,
        width=anchura_base,
        
        clip_behavior=ClipBehavior.ANTI_ALIAS,
        expand=True,
    )
    
    return View("/servicios", controls=[container_name, content_stack, dashboard_content])
