from flet import *
from utils.extras import *
from flet_route import Params, Basket
from state import update_state, get_state
from navigation import navigate_to
from translations import gettext as _


def servicios_db_page_view(page: Page, params: Params = None, basket: Basket = None):

    selected_index = get_state("selected_nav_index", default=0)

    # content = Column(controls=[Text("Página de Cuenta")])

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
        contador_servicios = (
            get_state("contador_servicios", default=0) + 1
        )  # Obtiene el contador actual y lo incrementa
        update_state(
            "contador_servicios", contador_servicios
        )  # Actualiza el contador en el estado global
        ver_pedido_btn.content.text = (
            _("view_order") + f" ({contador_servicios})"
        )  # Actualiza el texto del botón
        ver_pedido_btn.content.visible = True  # Asegura que el botón sea visible
        print("btn clicked")
        page.update()  # Actualiza la UI

    def ver_pedido(e):
        pass

    def mostrar_snackbar(page: Page, mensaje: str):
        snackbar = SnackBar(content=Text(mensaje), open=True, duration=4000)
        page.snack_bar = snackbar
        page.update()

    navigation_bar = NavigationBar(
        destinations=[
            NavigationDestination(
                icon=icons.HOME_OUTLINED, selected_icon=icons.HOME, label=_("home")
            ),
            NavigationDestination(
                icon=icons.LOCAL_LAUNDRY_SERVICE_OUTLINED,
                selected_icon=icons.LOCAL_LAUNDRY_SERVICE,
                label=_("services"),
            ),
            NavigationDestination(
                icon=icons.SHOP_OUTLINED, selected_icon=icons.SHOP, label=_("orders")
            ),
            NavigationDestination(
                icon=icons.ACCOUNT_CIRCLE_OUTLINED,
                selected_icon=icons.ACCOUNT_CIRCLE,
                label=_("acc"),
            ),
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
        # height=720,
        alignment=alignment.center,
        content=Column(alignment="end", controls=[navigation_bar]),
    )

    servicio_text_title = Text(
        value=_("pick_service"),
        style=TextStyle(size=24, weight=FontWeight.BOLD, color="#f0fdfa"),
        width=anchura_base,
        text_align=TextAlign.CENTER,
    )

    servicio_lavado_img = Container(
        content=Column(
            controls=[
                Image(
                    src="https://jsavinong.github.io/Lala-vanderia-App/frontend/assets/images/lavado.jpg",
                    border_radius=10,
                ),
                Text(
                    value=_("washing_service"), size=20, style=TextStyle(weight="bold")
                ),
                FilledTonalButton(
                    _("add"),
                    icon="add",
                    on_click=agregar_servicio,
                    style=ButtonStyle(shape=RoundedRectangleBorder(radius=10)),
                ),
            ],
            # height=200, width=200
            horizontal_alignment=CrossAxisAlignment.CENTER,
        ),
        height=200,
        width=200,
        # ink=True,
        on_click=lambda e: print("clicked"),
    )

    servicio_planchado_img = Container(
        content=Column(
            controls=[
                Image(
                    src="https://jsavinong.github.io/Lala-vanderia-App/frontend/assets/images/planchado.jpg",
                    border_radius=10,
                ),
                Text(
                    value=_("drying_service"), size=20, style=TextStyle(weight="bold")
                ),
                FilledTonalButton(
                    _("add"),
                    icon="add",
                    on_click=agregar_servicio,
                    style=ButtonStyle(shape=RoundedRectangleBorder(radius=10)),
                ),
            ],
            horizontal_alignment=CrossAxisAlignment.CENTER,
        ),
        height=200,
        width=200,
        on_click=lambda e: print("clicked"),
    )

    servicio_planchado_img2 = Container(
        content=Column(
            controls=[
                Image(
                    src="https://jsavinong.github.io/Lala-vanderia-App/frontend/assets/images/planchado.jpg",
                    border_radius=10,
                ),
                Text(
                    value=_("drying_service"), size=20, style=TextStyle(weight="bold")
                ),
                FilledTonalButton(
                    _("add"),
                    icon="add",
                    on_click=agregar_servicio,
                    style=ButtonStyle(shape=RoundedRectangleBorder(radius=10)),
                ),
            ],
            horizontal_alignment=CrossAxisAlignment.CENTER,
        ),
        height=200,
        width=200,
        on_click=lambda e: print("clicked"),
    )

    ver_pedido_btn = Container(
        content=FilledButton(
            Text(
                value=_("view_order") + " (0)",
            ),
            visible=False,
            on_click=lambda e: mostrar_snackbar(page,_("not_ready")),
            style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=10),
                color="#f0fdfa",
                bgcolor="#0f766e",
            ),
        ),
        height=30,
        width=300,
    )

    # ver_container = Container(
    #     content=(ver_pedido_btn),
    #     # height=altura_base,
    #     width=300,
    # )

    container_name = Container(
        content=Column(
            controls=[
                Text(
                    value=_("services"),
                    weight=FontWeight.BOLD,
                    size=24,
                    color="#f0fdfa",
                )
            ]
        ),
        padding=Padding(15, 20, 5, 15),
        width=anchura_base,
        height=80,
        bgcolor="#042f2e",
    )

    content = Container(
        width=anchura_base,
        bgcolor="#3309252a",
        # clip_behavior=ClipBehavior.ANTI_ALIAS,
        expand=True,
        # border_radius=radio_borde,
        alignment=alignment.center,
        content=Column(
            controls=[
                Container(height=10, width=anchura_base),
                servicio_text_title,
                Divider(),
                # Container(height=10),
                servicio_lavado_img,
                Divider(),
                servicio_planchado_img,
                Divider(),
                servicio_planchado_img2,
                Divider(),
                # ver_pedido_btn,
                # ver_container
                # test
                # faq_textbtn,
                # terminos_de_uso_textbtn,
            ],
            horizontal_alignment=CrossAxisAlignment.CENTER,
            scroll="auto",
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
                                        Row(controls=[
                                            Column(controls=[
                                                ver_pedido_btn])],
                                            alignment="center"),
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

    return View("/servicios", controls=[main_contianer])
