from flet import *
from state import update_state, get_state
from utils.extras import *
from navigation import navigate_to
from flet_route import Params, Basket
from services import check_email_registered_sync
from threading import Thread

def main_page_view(page: Page, params: Params, basket: Basket):
    # Construcción de la UI de MainPage
    
    # Crear directamente el TextField y mantener una referencia a él
    email_text_field = TextField(
        hint_text="E-mail",
        hint_style=TextStyle(size=16, color=input_hint_color),
        text_style=TextStyle(size=16, color=input_hint_color),
        border=InputBorder.NONE,
        content_padding=content_padding,
    )

    email_input = Container(
        height=altura_btn,
        bgcolor="white",
        border_radius=10,
        content=email_text_field,  # Usar la referencia aquí
        )
    
    continue_button = ElevatedButton(
        content=Text(value="Continuar", size=18),
        width=anchura_btn,
        height=altura_btn,  # Opcional: Añade un ícono al botón
        on_click=lambda e: on_click_handler(page, email_text_field),  # Reemplaza esto con tu función de manejo de clics real
        style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=10), bgcolor=blue_base)
)

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
        # Almacenar el email en el estado global antes de verificar si está registrado
        update_state("email", email)
        check_email_and_navigate(page, email)


    main_content = Column(
        controls=[
            email_input,
            continue_button,
            Row(
                alignment="center",
                controls=[
                    Text(
                        value="o",
                        size=16,
                    )
                ],
            ),
            Container(
                height=altura_btn,
                width=anchura_btn,
                bgcolor=gray_light,
                border_radius=10,
                alignment=alignment.center,
                padding=10,
                content=Row(
                    controls=[
                        Image(src="assets/icons/facebook.png", scale=0.7),
                        Text(
                            value="Continuar con Facebook",
                            size=18,
                            color=color_base,
                        ),
                    ]
                ),
            ),
            Container(height=0),
            Container(
                height=altura_btn,
                width=anchura_btn,
                bgcolor=gray_light,
                border_radius=10,
                alignment=alignment.center,
                padding=10,
                content=Row(
                    controls=[
                        Image(src="assets/icons/google.png", scale=0.7),
                        Text(
                            value="Continuar con Google",
                            size=18,
                            color=color_base,
                        ),
                    ]
                ),
            ),
            Container(height=0),
            Container(
                height=altura_btn,
                width=anchura_btn,
                bgcolor=gray_light,
                border_radius=10,
                alignment=alignment.center,
                padding=10,
                content=Row(
                    controls=[
                        Image(src="assets/icons/apple.png", scale=0.7),
                        Text(
                            value="Continuar con Apple",
                            size=18,
                            color=color_base,
                        ),
                    ]
                ),
            ),
            Container(height=20),
            Text(
                value="Olvidaste tu contraseña?",
                color=gray_base,
                size=16,
            ),
        ]
    )

    content = Container(
        height=altura_base,
        width=anchura_base,
        bgcolor="color_base",
        border_radius=radio_borde,
        clip_behavior=ClipBehavior.ANTI_ALIAS,
        expand=True,
        content=Stack(
            controls=[
                Container(
                    height=altura_base,
                    width=anchura_base,
                    bgcolor=colors.BLACK,
                    content=Image(
                        src="assets\images\gianluca-d-intino-vl4QuDMyeyY-unsplash (1).jpg",
                        # scale=1.5,
                        fit=ImageFit.COVER,
                        opacity=0.5,
                    ),
                ),
                Container(
                    height=altura_base,
                    width=anchura_base,
                    padding=padding.only(top=30, left=10, right=10),
                    content=Column(
                        controls=[
                            Container(height=160),
                            Container(
                                margin=margin.only(left=20),
                                content=Text(
                                    value="Hola!",
                                    weight=FontWeight.BOLD,
                                    size=30,
                                ),
                            ),
                            Container(height=2),
                            Container(
                                padding=20,
                                bgcolor="#cc2d2b2c",
                                border_radius=10,
                                content=main_content,
                            ),
                        ]
                    ),
                ),
            # Agrega aquí los controles para tu fondo y contenido principal
            ]
        ),
    )

    return View("/", controls=[content])
