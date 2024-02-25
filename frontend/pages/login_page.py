from flet import *
from utils.extras import *
from flet_route import Params, Basket
from navigation import go_back, navigate_to
from state import get_state, update_state
from services import fetch_user_info, login_user

def login_page_view(page: Page, params: Params, basket: Basket):
    offset = transform.Offset(
        0,
        0,
    )
    expand = True

    email = get_state("email")  # Obtiene el correo electrónico del estado global.
    
    def mostrar_snackbar(page: Page, mensaje: str):
        snackbar = SnackBar(content=Text(mensaje), open=True, duration=4000)
        page.snack_bar = snackbar
        page.update()
    

    def show_hide_password(e):
        det = password_text_field.password
        if det == True:
            password_text_field.password = False
            view_text.value = "Ocultar"
        else:
            password_text_field.password = True
            view_text.value = "Ver"
        password_text_field.update()
        view_text.update()
    
    view_text = Text(value="Ver", color=color_base)

    password_text_field = TextField(
            password=True,
            suffix=Container(on_click=show_hide_password, content=view_text),
            hint_text="Contraseña",
            hint_style=TextStyle(size=16, color=input_hint_color),
            text_style=TextStyle(size=16, color=input_hint_color),
            border=InputBorder.NONE,
            content_padding=content_padding,
            selection_color=blue_base,
            cursor_color=color_base,
        )
    pwd_input = Container(
        height=altura_btn,
        bgcolor="white",
        border_radius=10,
        content=password_text_field
    )
    email_text = Text(value=email, size=14)
    username_text = Text(value="", size=14, weight="bold")  # Inicialmente vacío
    page.add(username_text)

    continue_button = ElevatedButton(
        content=Text(value="Continuar", size=18),
        width=anchura_btn,
        height=altura_btn,  # Opcional: Añade un ícono al botón
        on_click=lambda e: on_continuar_clicked(page, email_text.value, password_text_field.value),  # Reemplaza esto con tu función de manejo de clics real
        style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=10), bgcolor=blue_base)
)
    def on_continuar_clicked(page: Page, correo_electronico: str, contraseña: str):
        # Extrae los valores directamente de los campos de texto
        # correo_electronico= email_text.value
        # contraseña = password_text_field.value
        # print(password_text_field.value, email_text.value, username_text.value)
        update_state("nombre", username_text.value)
        def on_login_result(success, message):
            if success:
                # Navegar al dashboard o realizar acciones de éxito
                navigate_to(page, "/dashboard")
            else:# Llama a la función de inicio de sesión con el callback
                # Mostrar mensaje de error
                mostrar_snackbar(page, message)
        login_user(page, correo_electronico, contraseña, on_login_result)

    def update_username_ui(username):
        print(username)
        username_text.value = username
        page.update() 
        

    # Llama a fetch_user_info pasando el email y el callback
    fetch_user_info(email, lambda username: update_username_ui(username))

    login_box = Column(
        controls=[
            Row(
                controls=[
                    Container(
                        height=50,
                        width=50,
                        border_radius=25,
                        image_fit=ImageFit.COVER,
                        image_src="http://10.0.0.20:5000/icons/neutral acc img.png",
                    ),
                    Column(
                        spacing=0,
                        controls=[
                            username_text, email_text
                            
                        ],
                    ),
                ]
            ),
            pwd_input,
            continue_button,
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
                        src="http://10.0.0.20:5000/images/gianluca-d-intino-vl4QuDMyeyY-unsplash (1).jpg",
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
                                data="main_page", # !pa qué sirve?
                                on_click = lambda e: go_back(page),
                                content=Icon(
                                    icons.ARROW_BACK_IOS_OUTLINED, size=28
                                ),
                            ),
                            Container(height=160),
                            Container(
                                margin=margin.only(left=20),
                                content=Text(
                                    value="Login",
                                    weight=FontWeight.BOLD,
                                    size=30,
                                ),
                            ),
                            Container(height=2),
                            Container(
                                padding=20,
                                bgcolor="#cc2d2b2c",
                                border_radius=10,
                                content=login_box,
                            ),
                        ]
                    ),
                ),
            ]
        ),
    )
    return View("/login", controls=[content])
