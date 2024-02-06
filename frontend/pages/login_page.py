from flet import *
from utils.extras import *
from flet_route import Params, Basket
from navigation import go_back

def login_page_view(page: Page, params: Params, basket: Basket):
    offset = transform.Offset(
        0,
        0,
    )
    expand = True

    pwd_input = Container(
        height=altura_btn,
        bgcolor="white",
        border_radius=10,
        content=TextField(
            hint_text="Contraseña",
            hint_style=TextStyle(size=16, color=input_hint_color),
            text_style=TextStyle(size=16, color=input_hint_color),
            border=InputBorder.NONE,
            content_padding=content_padding,
        ),
    )

    # def on_back_clicked(page: Page):
        # page.go("/ruta-anterior")
    login_box = Column(
        controls=[
            Row(
                controls=[
                    Container(
                        height=50,
                        width=50,
                        border_radius=25,
                        image_fit=ImageFit.COVER,
                        image_src=img_src,
                    ),
                    Column(
                        spacing=0,
                        controls=[
                            Text(
                                value="Prueba",
                                weight=FontWeight.BOLD,
                                size=14,
                            ),
                            Text(
                                value="test@gmail.com",
                                size=14,
                            ),
                        ],
                    ),
                ]
            ),
            pwd_input,
            Container(
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
