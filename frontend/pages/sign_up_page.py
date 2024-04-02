from flet import *
from utils.extras import *
from flet_route import Params, Basket
from navigation import go_back
from state import update_state, get_state
from services import signup_user
from threading import Thread
import re
from translations import gettext as _

#from services.services import signup_user

def signup_page_view(page: Page, params: Params, basket: Basket):
    email = get_state("email")  # Obtiene el correo electrónico del estado global.
    
    aceptar_continuar_btn = ElevatedButton(
        content=Text(value=_("accept_continue"), size=18, color="#f2fbfb", style=TextStyle(weight=FontWeight.BOLD)),
        width=anchura_btn,
        height=altura_btn,  # Opcional: Añade un ícono al botón
        on_click=lambda e: on_aceptar_continuar_clicked(page, email, name_box.value, password_box.value),  # Reemplaza esto con tu función de manejo de clics real
        style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=10), bgcolor="#0f766e")
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
                mensaje_error = _("empty_name_field")
            elif not contraseña or len(contraseña) < 8:
                mensaje_error = _("pwd_8_chars")
            elif not re.search("[a-z]", contraseña) or not re.search("[A-Z]", contraseña) or not re.search("[0-9]", contraseña) or not re.search("[\W_]", contraseña):
                mensaje_error = _("pwd_caps_nums_specialchars")
            
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
        hint_text=_("name"),
        hint_style=TextStyle(
            size=16,
            color="#09252a",
        ),
        text_style=TextStyle(
            size=16,
            color="#09252a",
        ),
        border=InputBorder.NONE,
        content_padding=content_padding,
        width=anchura_btn
    )
    
    def show_hide_password(e):
        det = password_box.password
        if det == True:
            password_box.password = False
            view_text.value = _("hide")
        else:
            password_box.password = True
            view_text.value = _("show")
        password_box.update()
        view_text.update()

    view_text = Text(value=_("show"), color=color_base)

    password_box = TextField(
        password=True,
        suffix=Container(on_click=show_hide_password, content=view_text),
        hint_text=_("pwd"),
        hint_style=TextStyle(
            size=16,
            color="#09252a",
        ),
        text_style=TextStyle(
            size=16,
            color="#09252a",
        ),
        border=InputBorder.NONE,
        content_padding=content_padding,
        selection_color=blue_base,
        cursor_color=color_base,
        width=anchura_btn
    )

    terms_conditions_link = Text(
            
            spans=[
                TextSpan(
                    _("terms_policy"), TextStyle(weight=FontWeight.BOLD),
                    
                    on_click=lambda e: mostrar_snackbar(page,_("not_ready"), )
                ),
                ],)

    signup_box = Column(
        controls=[
            Column(
                spacing=0,
                controls=[
                    Text(
                        value=_("sign_up_misc_text1"),
                        size=14,
                        color="#ccffffff",
                    ),
                    Text(value=email, size=14, color="#ccffffff", weight="bold"),
                ],
            ),
            Container(
                height=altura_btn,
                border_radius=10,
                bgcolor="#f2fbfb",
                content=name_box,
            ),
            Container(
                height=altura_btn,
                border_radius=10,
                bgcolor="#f2fbfb",
                content=password_box,
            ),
            Container(height=1),
            Container(
                content=Column(
                    spacing=0,
                    controls=[
                        Text(
                            value=_("sign_up_text_accept_continue"),
                            size=14,
                            color="#ccffffff",
                        ),
                        ResponsiveRow(
                            #spacing=0,
                            controls=[
                                # Text(
                                # value="Acepto",
                                # size=14,
                                # color='#ccffffff'
                                # ),
                            terms_conditions_link
                            ],
                        ),
                    ],
                )
            ),
            aceptar_continuar_btn,
            Container(height=20),
        
        ]
    )
    content = Container(
        #height=altura_base,
        #width=anchura_base,
        bgcolor="ccfbf1",
        #border_radius=radio_borde,
        #clip_behavior=ClipBehavior.ANTI_ALIAS,
        expand=True,
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
                            Container(
                                data="main_page",
                                on_click = lambda e: go_back(page),
                                content=Icon(
                                    icons.ARROW_BACK_IOS_OUTLINED, size=28, color="#09252a"
                                ),
                                width=30, 
                                alignment=alignment.top_left
                            ),
                            Container(height=100,
                                    width=anchura_base),
                            Container(
                                margin=margin.only(left=20),
                                content=Text(
                                    value=_("signup"),
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
                                content=signup_box,
                                width=anchura_base
                            ),
                        ]
                    ),
                ),
            ]
        ),
    )
    return View("/signup", controls=[content])


