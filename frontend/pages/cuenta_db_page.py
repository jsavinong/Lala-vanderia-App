from flet import *
from utils.extras import *
from flet_route import Params, Basket
from state import update_state, get_state, actualizar_indice_navegacion
from navigation import navigate_to
from translations import load_translations, gettext as _

def cuenta_db_page_view(page: Page, params: Params=None, basket: Basket=None):
    
    selected_index = get_state("selected_nav_index", default=0)
    
    #content = Column(controls=[Text("Página de Cuenta")])

    nombre = get_state("nombre")  # Obtiene el nombre  del estado global.
    
    current_language = get_state("user_language", default="es")
    
    def on_language_change(e):
        selected_language = e.control.value
        # Cargar las nuevas traducciones
        load_translations(selected_language)
        # Actualizar el estado global con el nuevo idioma seleccionado
        update_state("user_language", selected_language)
        # Refrescar la página para que se muestren las traducciones actualizadas
        page.update()
        # Si tienes una estructura de navegación, podrías redirigir a la página actual para forzar un refresco completo

    language_dropdown = Dropdown(
        value=current_language,
        options=[
            dropdown.Option("es", "Español"),
            dropdown.Option("en", "English"),
        ],
        on_change=on_language_change,
        width=200, label=_("language"), label_style=TextStyle(weight=FontWeight.BOLD, color="#9ecaff"), 
        prefix_icon="language", border_color="#9ecaff"
        
        
    )

    dropdown_container = Container(
        content=Row(
            controls=[
                language_dropdown
            ]
        )
    )

    def on_logout_clicked(e):
        actualizar_indice_navegacion(0)
        navigate_to(page, "/")
    
    logout_btn = TextButton(
        content=Row(
            controls=[
                Text(_("logout"), style=TextStyle(size=18, color=colors.WHITE))  
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

    plan_name = Container(
        content=Row(
            controls=[
                Text(
                    value=f'No Plan', # TODO: Configurar Nombre del Plan (código y margen) 
                    size=12,
                    weight=FontWeight.BOLD,
        )
        ],
        alignment=MainAxisAlignment.CENTER,
        ),
        #padding=Padding(0,0,0,50),
        #height=50
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
        padding=Padding(15,20,5,15),
        bgcolor="#042f2e",
        width=anchura_base,
        height=80
    )


    suscribir_btn = FilledButton(
        content=Text(value=_("subscribe").upper(), size=24, weight=FontWeight.BOLD),
        width=300,
        height=altura_btn,  
        on_click=on_click_suscribir,
        style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=10), bgcolor=colors.BLUE_100)
                
)
    
    faq_textbtn = TextButton(
        content=Row(
            controls=[
                Icon(icons.QUESTION_ANSWER, size=24),  
                Text("FAQ", style=TextStyle(size=18)),  
            ],
            alignment="left",
        ),
        on_click=lambda e: print("Botón presionado"),  # Reemplaza esto con tu función de callback real
    )
    

    terminos_de_uso_textbtn = TextButton(
        content=Row(
            controls=[
                Icon(icons.DESCRIPTION, size=24),  
                Text(_("use_terms"), style=TextStyle(size=18)),  
            ],
            alignment="left",
        ),
        on_click=lambda e: print("Botón presionado"),  # Reemplaza esto con tu función de callback real
    )
    
    content = Container(
    
        #height=altura_base,
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
                suscribir_btn,
                Container(height=10,
                        width=anchura_base),
                faq_textbtn,
                Divider(),
                terminos_de_uso_textbtn,
                Divider(),
                dropdown_container,
                Divider(),
                logout_btn

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

    return View("/cuenta", controls=[main_contianer])
