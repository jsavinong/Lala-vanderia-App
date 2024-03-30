from flet import *
from utils.extras import *
from flet_route import Params, Basket
from navigation import go_back, navigate_to
from state import get_state, update_state
from services import fetch_user_info, login_user
from translations import gettext as _

def login_page_view(page: Page, params: Params, basket: Basket):

    email = get_state("email")  # Obtiene el correo electrónico del estado global.
    
    def mostrar_snackbar(page: Page, mensaje: str):
        snackbar = SnackBar(content=Text(mensaje), open=True, duration=4000)
        page.snack_bar = snackbar
        page.update()
    

    def show_hide_password(e):
        det = password_text_field.password
        if det == True:
            password_text_field.password = False
            view_text.value = _("hide")
        else:
            password_text_field.password = True
            view_text.value = _("show")
        password_text_field.update()
        view_text.update()
    
    view_text = Text(value=_("show"), color=color_base)

    password_text_field = TextField(
            password=True,
            suffix=Container(on_click=show_hide_password, content=view_text),
            hint_text=_("pwd"),
            hint_style=TextStyle(size=16, color="#09252a"),
            text_style=TextStyle(size=16, color="#09252a"),
            border=InputBorder.NONE,
            content_padding=content_padding,
            selection_color=blue_base,
            cursor_color=color_base,
        )
    pwd_input = Container(
        height=altura_btn,
        bgcolor="#f2fbfb",
        border_radius=10,
        content=password_text_field
    )
    email_text = Text(value=email, size=14)
    username_text = Text(value="", size=14, weight="bold")  # Inicialmente vacío
    page.add(username_text)

    continue_button = ElevatedButton(
        content=Text(value=_("continue"), size=18, color="#f2fbfb", style=TextStyle(weight=FontWeight.BOLD)),
        width=anchura_btn,
        height=altura_btn,  # Opcional: Añade un ícono al botón
        on_click=lambda e: on_continuar_clicked(page, email_text.value, password_text_field.value),  # Reemplaza esto con tu función de manejo de clics real
        style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=10), bgcolor="#0f766e")
)
    
    forgot_pwd_link = Text(
            
            spans=[
                TextSpan(
                    _("forgot_pwd"),
                    
                    on_click=lambda e: mostrar_snackbar(page,_("not_ready")),
                ),
                ])
    
    def on_continuar_clicked(page: Page, correo_electronico: str, contraseña: str):
        # Extrae los valores directamente de los campos de texto
        # correo_electronico= email_text.value
        # contraseña = password_text_field.value
        # print(password_text_field.value, email_text.value, username_text.value)
        update_state("nombre", username_text.value)
        def on_login_result(success, message):
            if success:
                # Navegar al dashboard o realizar acciones de éxito
                #navigate_to(page, "/dashboard")
                navigate_to(page, "/inicio")
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
            ResponsiveRow(
                controls=[
                    CircleAvatar(
                    foreground_image_url="https://jsavinong.github.io/Lala-vanderia-App/frontend/assets/icons/neutral acc img.png",
                    col=2, min_radius=20, max_radius=30, radius=30, 
                    
                    ),
                    Container(
                        col=10,
                        content=(Column(controls=[
                            username_text, email_text   
                ])),height=50,clip_behavior=ClipBehavior.ANTI_ALIAS
                    ),
                ]
            ),
            pwd_input,
            continue_button,
            Container(height=20),
            forgot_pwd_link
            
        ]
    )
    content = Container(
        expand=True,
        content=Stack(
            controls=[
                Container(
                    gradient=LinearGradient(
                        rotation=30,
                        begin=alignment.center_left,
                        end=alignment.bottom_right,
                        colors=["#09252a", "#d2f5f4"],
                    ),
                ),
                Container(
                    alignment=alignment.center,
                    padding=padding.only(top=30, left=10, right=10),
                    content=Column(
                        controls=[
                            Container(
                                #data="main_page", # !pa qué sirve?
                                on_click = lambda e: go_back(page),
                                width = anchura_base,
                                alignment=alignment.top_left,
                                content=Icon(
                                    icons.ARROW_BACK_IOS_OUTLINED, size=28, color="#09252a"
                                ),
                            ),
                            Container(height=160, 
                                    width=anchura_base),
                            Container(
                                margin=margin.only(left=20),
                                content=Text(
                                    value=_("login"),
                                    weight=FontWeight.BOLD,
                                    size=30,
                                    width=anchura_base
                                ),
                            ),
                            Container(height=2,
                                    width=anchura_base),
                            Container(
                                padding=20,
                                bgcolor="#661b4d54",
                                border_radius=10,
                                width=anchura_base,
                                content=login_box,
                            ),
                        ]
                    ),
                ),
            ]
        ),
    )
    return View("/login", controls=[content])
