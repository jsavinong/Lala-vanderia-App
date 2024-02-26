from flet import *
from utils.extras import *
from flet_route import Params, Basket
from navigation import go_back
from state import update_state, get_state
from services import signup_user
from threading import Thread
import re

#from services.services import signup_user

def signup_page_view(page: Page, params: Params, basket: Basket):
    email = get_state("email")  # Obtiene el correo electrónico del estado global.
    
    # self.email = email
    # self.dp_url = dp
    offset = transform.Offset(0,0,)
    expand = True
    aceptar_continuar_btn = ElevatedButton(
        content=Text(value="Aceptar y Continuar", size=18),
        width=anchura_btn,
        height=altura_btn,  # Opcional: Añade un ícono al botón
        on_click=lambda e: on_aceptar_continuar_clicked(page, email, name_box.value, password_box.value),  # Reemplaza esto con tu función de manejo de clics real
        style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=10), bgcolor=blue_base)
    )

    def mostrar_snackbar(page: Page, mensaje: str):
        snackbar = SnackBar(content=Text(mensaje), open=True, duration=4000)
        page.snack_bar = snackbar
        page.update()


    def on_aceptar_continuar_clicked(page: Page, correo_electronico: str, nombre: str, contraseña: str):

        def do_signup():
            mensaje_error = ""
            # Verificar que los campos no estén vacíos
            if not nombre:
                mensaje_error = "El campo de nombre está vacío."
            elif not contraseña or len(contraseña) < 8:
                mensaje_error = "La contraseña debe tener al menos 8 caracteres."
            elif not re.search("[a-z]", contraseña) or not re.search("[A-Z]", contraseña) or not re.search("[0-9]", contraseña) or not re.search("[\W_]", contraseña):
                mensaje_error = "La contraseña debe contener mayúsculas, minúsculas, números y caracteres especiales."
            
            # Si hay un mensaje de error, mostrarlo y detener el registro
            if mensaje_error:
                mostrar_snackbar(page, mensaje_error)
                return
            update_state("nombre", nombre)
            # Aquí llamas a signup_user, que ahora debería estar adaptada para trabajar con threads
            signup_user(page, nombre, correo_electronico, contraseña)

        # Iniciar el proceso de registro en un hilo secundario
        Thread(target=do_signup).start()

    name_box = TextField(
        hint_text="Nombre",
        hint_style=TextStyle(
            size=16,
            color=input_hint_color,
        ),
        text_style=TextStyle(
            size=16,
            color=input_hint_color,
        ),
        border=InputBorder.NONE,
        content_padding=content_padding,
    )
    
    def show_hide_password(e):
        det = password_box.password
        if det == True:
            password_box.password = False
            view_text.value = "Ocultar"
        else:
            password_box.password = True
            view_text.value = "Ver"
        password_box.update()
        view_text.update()

    view_text = Text(value="Ver", color=color_base)

    password_box = TextField(
        password=True,
        suffix=Container(on_click=show_hide_password, content=view_text),
        hint_text="Contraseña",
        hint_style=TextStyle(
            size=16,
            color=input_hint_color,
        ),
        text_style=TextStyle(
            size=16,
            color=input_hint_color,
        ),
        border=InputBorder.NONE,
        content_padding=content_padding,
        selection_color=blue_base,
        cursor_color=color_base,
    )



    signup_box = Column(
        controls=[
            Column(
                spacing=0,
                controls=[
                    Text(
                        value="Al parecer no tienes una cuenta con nosotros.\nAsí que vamos a crear una para",
                        size=14,
                        color="#ccffffff",
                    ),
                    Text(value=email, size=14, color="#ccffffff", weight="bold"),
                ],
            ),
            Container(
                height=altura_btn,
                border_radius=10,
                bgcolor="white",
                content=name_box,
            ),
            Container(
                height=altura_btn,
                border_radius=10,
                bgcolor="white",
                content=password_box,
            ),
            Container(height=1),
            Container(
                content=Column(
                    spacing=0,
                    controls=[
                        Text(
                            value="Al presionar 'Aceptar y Continuar' debajo, aceptas",
                            size=14,
                            color="#ccffffff",
                        ),
                        Row(
                            spacing=0,
                            controls=[
                                # Text(
                                # value="Acepto",
                                # size=14,
                                # color='#ccffffff'
                                # ),
                                Text(
                                    value="Términos de servicio y Políticas de privacidad",
                                    size=14,
                                    weight=FontWeight.BOLD,
                                    color=blue_base,
                                ),
                            ],
                        ),
                    ],
                )
            ),
            aceptar_continuar_btn,
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
                        src="https://jsavinong.github.io/Lala-vanderia-App/frontend/assets/images/gianluca-d-intino-vl4QuDMyeyY-unsplash (1).jpg",
                        # bgcolor="#cc2d2b2c",
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
                            Container(
                                data="main_page",
                                on_click = lambda e: go_back(page),
                                content=Icon(
                                    icons.ARROW_BACK_IOS_OUTLINED, size=28
                                ),
                            ),
                            Container(height=160),
                            Container(
                                margin=margin.only(left=20),
                                content=Text(
                                    value="Sign Up",
                                    weight=FontWeight.BOLD,
                                    size=30,
                                ),
                            ),
                            Container(height=2),
                            Container(
                                padding=20,
                                bgcolor="#cc2d2b2c",
                                border_radius=10,
                                content=signup_box,
                            ),
                        ]
                    ),
                ),
            ]
        ),
    )
    return View("/signup", controls=[content])


