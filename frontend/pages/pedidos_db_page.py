from flet import *
from utils.extras import *
from flet_route import Params, Basket
from state import update_state, get_state
from navigation import navigate_to
from translations import gettext as _


def pedidos_db_page_view(page: Page, params: Params=None, basket: Basket=None):
    
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
    
    def on_click_hacer_pedidos(e):
        update_state("selected_nav_index", 1)
        navigate_to(page, "/servicios")
        page.update()


    navigation_bar = NavigationBar(
        destinations=[
            NavigationDestination(icon=icons.HOME_OUTLINED, selected_icon=icons.HOME, label=_("home")),
            NavigationDestination(icon=icons.LOCAL_LAUNDRY_SERVICE_OUTLINED,selected_icon=icons.LOCAL_LAUNDRY_SERVICE, label=_("services")),
            NavigationDestination(icon=icons.SHOP_OUTLINED, selected_icon=icons.SHOP, label=_("orders")),
            NavigationDestination(icon=icons.ACCOUNT_CIRCLE_OUTLINED, selected_icon=icons.ACCOUNT_CIRCLE, label=_("acc"))
        ],
        selected_index=selected_index,
        on_change=on_navigation_changed,
        width=anchura_base,
        shadow_color="#042f2e",
        bgcolor="#042f2e",
        indicator_color="#134e4a",
        adaptive=True,
    )
    dashboard_content = Container(
        #height=720,
        alignment=alignment.center,
        content=Column(
            alignment="end",
            controls=[
                navigation_bar
            ]
        )
    )
    
    img_contenedor = Container( # TODO Agregar funcionalidad para que desaparezca al crear pedido
        content=Column(
            controls=[
                Row(
                    controls=[
                        Image(
                            src="https://jsavinong.github.io/Lala-vanderia-App/frontend/assets/images/noPedidos.png",
                            width=250,
                            height=250,
                            fit=ImageFit.CONTAIN,
                        )
                    ],
                    alignment=MainAxisAlignment.CENTER
                ),
                Text(value=_("no_orders"),weight=FontWeight.W_500, 
                    size=24,color=colors.BLACK) 
            ],horizontal_alignment=CrossAxisAlignment.CENTER
        ),
        bgcolor=colors.WHITE60,
        border_radius=10,
        width=anchura_btn
        #alignment=CrossAxisAlignment.CENTER,
        #alignment=MainAxisAlignment.CENTER  # This centers the Column within the Container
    )

    hacer_pedido_btn = FilledButton(
        content=Text(value=_("make_order"), size=20, weight=FontWeight.BOLD),
        width=250,
        height=altura_btn,  
        on_click= on_click_hacer_pedidos, 
        style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=10), bgcolor=colors.WHITE60)
                
)
    
    container_name = Container(
        content=Column(
            controls=[
                Text(
                    value=_("orders"), 
                    weight=FontWeight.BOLD, 
                    size=24,color="#f0fdfa")
            ]
        ),
        padding=Padding(15,20,5,15),
        bgcolor="#042f2e",
        width=anchura_base,
        height=80
    )
    
    content = Container(
    
        width=anchura_base,
        bgcolor="#3309252a",
        #clip_behavior=ClipBehavior.ANTI_ALIAS,
        expand=True,
        #border_radius=radio_borde,
        alignment=alignment.center,
        content=Column(
            controls=[
                
                Container(height=10,
                        width=anchura_base),
                img_contenedor,
                Container(height=10,
                        width=anchura_base),
                hacer_pedido_btn,
                # faq_textbtn,
                # terminos_de_uso_textbtn,

            ],
            horizontal_alignment=CrossAxisAlignment.CENTER,
            scroll="auto"
            ),

    )
    
    main_contianer = Container(
        expand=True,
        content=Stack(
            [
                Container(
                    gradient=LinearGradient(
                        rotation=30,
                        begin=alignment.center_left,
                        end=alignment.bottom_right,
                        colors=["#CC09252a", "#CCd2f5f4"],
                    ),
                ),
                Container(
                    alignment=alignment.center,
                    content=Column(
                        controls=[
                            Container(
                                width=anchura_base,
                                height=700,
                                content=Column(
                                    controls=[
                                        container_name,
                                        content,
                                        
                                        dashboard_content,
                                        
                                    ]
                                ),
                            )
                        ]
                    ),
                ),
                # Row(
                #     controls=[
                #         Column(
                #             controls=[
                #                 ver_pedido_btn,
                #             ],
                #             alignment=MainAxisAlignment.END,
                #         ),
                #     ],
                #     # left=100,
                #     # top=470,
                # ),
            ],
        ),
    )
    
    return View("/pedidos", controls=[main_contianer])
