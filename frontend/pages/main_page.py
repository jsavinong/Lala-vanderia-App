from flet import *
from flet_route import Params, Basket
from utils.extras import *
from navigation import navigate_to

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

    def on_continue_clicked(page: Page, email_input: TextField):
        email = email_input.value
        # Aquí deberías verificar si el correo ya está registrado.
        # Para este ejemplo, asumiremos una lógica condicional simple.
        if email == "usuario_registrado@example.com":  # Este correo simula uno ya registrado.
            page.go("/login")  # Redirige a la página de Login
        else:
            page.go("/signup")  # Redirige a la página de Sign Up

    


    main_content = Column(
        controls=[
            email_input,
            # Agrega aquí el resto de tus controles
            Container(
                on_click=lambda e: navigate_to(page, "/login") if email_text_field.value =="usuario_registrado@example.com" else navigate_to(page, "/signup"),
                height=altura_btn,
                width=anchura_btn,
                bgcolor=blue_base,
                border_radius=10,
                alignment=alignment.center,
                content=Text(
                    value="Continuar",
                    size=18,
                ),
                
            ),
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
