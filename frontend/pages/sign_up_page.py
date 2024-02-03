from flet import *
from utils.extras import *


class SignupPage(Container):
    def __init__(self):
        super().__init__()
        # self.email = email
        # self.dp_url = dp
        self.offset = transform.Offset(
            0,
            0,
        )
        self.expand = True

        self.name_box = TextField(
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

        self.view_text = Text(value="Ver", color=color_base)
        self.password_box = TextField(
            password=True,
            suffix=Container(on_click=self.show_hide_password, content=self.view_text),
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

        self.signup_box = Column(
            controls=[
                Column(
                    spacing=0,
                    controls=[
                        Text(
                            value="Al parecer no tienes una cuenta con nosotros.\nAsí que vamos a crear una para",
                            size=14,
                            color="#ccffffff",
                        ),
                        Text(value="test@gmail.com", size=14, color="#ccffffff"),
                    ],
                ),
                Container(
                    height=altura_btn,
                    border_radius=10,
                    bgcolor="white",
                    content=self.name_box,
                ),
                Container(
                    height=altura_btn,
                    border_radius=10,
                    bgcolor="white",
                    content=self.password_box,
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
                Container(
                    height=altura_btn,
                    width=anchura_btn,
                    bgcolor=blue_base,
                    border_radius=10,
                    alignment=alignment.center,
                    content=Text(
                        value="Aceptar y Continuar",
                        size=18,
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
        self.content = Container(
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
                                    content=self.signup_box,
                                ),
                            ]
                        ),
                    ),
                ]
            ),
        )

    def show_hide_password(self, e):
        det = self.password_box.password
        if det == True:
            self.password_box.password = False
            self.view_text.value = "Ocultar"
        else:
            self.password_box.password = True
            self.view_text.value = "Ver"
        self.password_box.update()
        self.view_text.update()
