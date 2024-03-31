from flet import *
from state import update_state, get_state
from utils.extras import *
from navigation import navigate_to
from flet_route import Params, Basket
from services import check_email_registered_sync
from threading import Thread
import re
from translations import gettext as _


def main_page_view(page: Page, params: Params, basket: Basket):

    # Construcción de la UI de MainPage
    
    # Crear directamente el TextField y mantener una referencia a él
    email_text_field = TextField(
        hint_text=_("e_mail"),
        hint_style=TextStyle(size=16, color="#09252a"),
        text_style=TextStyle(size=16, color="#09252a"),
        border=InputBorder.NONE,
        content_padding=content_padding,
        width=anchura_btn,
    )

    email_input = Container(
        height=altura_btn,
        width=anchura_btn,
        bgcolor="#f2fbfb",
        border_radius=10,
        content=email_text_field,  # Usar la referencia aquí
    )

    continue_button = ElevatedButton(
        content=Text(value=_("continue"), size=18, color="#f2fbfb", style=TextStyle(weight=FontWeight.BOLD)),
        width=anchura_btn,
        height=altura_btn,  
        on_click=lambda e: on_click_handler(
            page, email_text_field
        ),  
        style=ButtonStyle(shape=RoundedRectangleBorder(radius=10), bgcolor="#0f766e"),
    )

    def mostrar_snackbar(page: Page, mensaje: str):
        snackbar = SnackBar(content=Text(mensaje), open=True, duration=4000)
        page.snack_bar = snackbar
        page.update()

    def es_correo_valido(correo):
        # Esta es una expresión regular muy básica para validación de correo
        patron_correo = r"^\S+@\S+\.\S+$"
        return re.match(patron_correo, correo) is not None

    def on_email_checked(page: Page, is_registered: bool):
        if is_registered:
            # Navega a la página de inicio de sesión si el correo está registrado
            navigate_to(page, "/login")
        else:
            # Navega a la página de registro si el correo no está registrado
            navigate_to(page, "/signup")

    def check_email_and_navigate(page: Page, email: str):
        # Esta es la función que se ejecutará en el hilo
        def run():
            is_registered = check_email_registered_sync(email)
            # Necesitas asegurarte de que la actualización de la UI se ejecute en el hilo principal
            # La implementación específica dependerá de Flet y cómo gestiona las actualizaciones de la UI desde hilos
            on_email_checked(page, is_registered)

        Thread(target=run).start()

    def on_click_handler(page: Page, email_text_field: TextField):
        email = email_text_field.value
        if not email:
            mostrar_snackbar(page, _("type_mail"))
            return
        elif not es_correo_valido(email):
            mostrar_snackbar(page, _("type_valid_mail"))
            return
        # Almacenar el email en el estado global antes de verificar si está registrado
        update_state("email", email)
        check_email_and_navigate(page, email)

    forgot_pwd_link = Text(
        spans=[
            TextSpan(
                _("forgot_pwd"),
                on_click=lambda e: mostrar_snackbar(page, _("not_ready")),
            ),
        ]
    )

    o_txt = Row(
        alignment="center",
        width=350,
        controls=[
            Text(
                value=_("or"),
                size=16,
            )
        ],
    )

    continuar_google_btn = Container(
        # Altura fija para el botón, la anchura se ajusta al contenido o contenedor padre
        height=altura_btn,
        width=anchura_btn,
        bgcolor="#0f766e",
        border_radius=10,
        alignment=alignment.center,
        padding=10,
        
        on_click=lambda e: mostrar_snackbar(page, _("not_ready")),
        content=ResponsiveRow(
            controls=[
                Image(
                    src="https://jsavinong.github.io/Lala-vanderia-App/frontend/assets/icons/google.png",
                    width=30,
                    height=30,
                    col=2,
                    
                ),  
                Text(
                    value=_("continue_google"),
                    # color=color_base,
                    size=18,
                    text_align="center",
                    col=10,
                    style=TextStyle(weight=FontWeight.BOLD)
                ),
            ],
            alignment=MainAxisAlignment.SPACE_EVENLY,
            
        ),
    )

    main_container = Container(
        content=Column(
            controls=[
                email_input,
                continue_button,
                o_txt,
                Container(height=0),
                continuar_google_btn,
                Container(height=0),
                Container(height=20),
                #forgot_pwd_link,
            ],
        ),
    )
    
    # Importante fijar el ancho de los componentes para poder tener el centralizado correctamente

    content = Container(
        expand=True, # ! OJO
        bgcolor="#ccfbf1", 
        content=Stack(
            controls=[
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
                    
                    padding=padding.only(top=30, left=10, right=10),
                    content=Column(
                        controls=[
                            Container(height=160,
                                width=anchura_base),
                            Container(
                                margin=margin.only(left=20),
                                content=Text(
                                    value=_("greetings"),
                                    weight=FontWeight.BOLD,
                                    size=30,
                                    width=anchura_base
                                ),
                            ),
                            Container(height=2,
                                width=anchura_base),
                            Container(
                                padding=20,
                                width=anchura_base,
                                bgcolor="#661b4d54",
                                border_radius=10,
                                content=main_container,
                            ),
                        ]
                    ),
                ),
            ],
        ),
    )

    return View("/", controls=[content])
