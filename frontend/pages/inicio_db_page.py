from flet import *
from utils.extras import *
from flet_route import Params, Basket
from state import update_state, get_state
from navigation import navigate_to
from translations import gettext as _


def inicio_db_page_view(page: Page, params: Params=None, basket: Basket=None):
    

    selected_index = get_state("selected_nav_index", default=0)
    
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
    
    container_name = Container(
        content=ResponsiveRow(
            controls=[
                Text(
                    value=_("welcome"),
                    weight=FontWeight.BOLD, 
                    size=24,color="#f0fdfa",
                    col=6
                    ),
                Text(
                    value=nombre,
                    size=24,
                    weight=FontWeight.BOLD,
                    color="#f0fdfa",
                    col = 6
                    )
            ]
        ),
        padding=Padding(15,20,5,15),
        bgcolor="#042f2e",
        width=anchura_base,
        height=80, 
        #alignment=alignment.center
    )

    content = Container(
    
        #height=altura_base,
        width=anchura_base,
        bgcolor="#3309252a",
        #clip_behavior=ClipBehavior.ANTI_ALIAS,
        expand=True,
        #border_radius=radio_borde,
        alignment=alignment.center,
        content=Stack(
            controls=[
                
                #Container(height=10,
                        #width=anchura_base),
                #Container(height=10,
                        #width=anchura_base),
                

            ],
            #horizontal_alignment=CrossAxisAlignment.CENTER
            ),
    
    )

    main_container = Container(
        expand=True,
        content = Stack([
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
                            height= 700,
                            #bgcolor="#0009252a",
                            content=Column(
                                controls=[
                                    container_name,
                                    content,
                                    dashboard_content,
                                ]
                            )
                    )
        ])),
        ])
    )
    
    return View("/inicio", controls=[main_container])
