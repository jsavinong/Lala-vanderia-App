from flet import *
from utils.extras import *
from flet_route import Params, Basket
from state import update_state, get_state
from navigation import navigate_to
from flet import *
from translations import load_translations, gettext as _
from utils.extras import *

def first_page_view(page: Page, params: Params=None, basket: Basket=None):
    language_txt = Text(value="Selecciona un idioma:", weight=FontWeight.BOLD, size=18)
    
    language_dropdown = Dropdown(
                options=[
                    dropdown.Option("es", "Español"),
                    dropdown.Option("en", "English"),
                ],
                on_change=lambda e: on_language_change(e, page),  # Asignar el manejador del evento aquí
                width=200, prefix_icon="language",
                
            )
    
    content = Container(
        #height=altura_base,
        width=anchura_base,
        #bgcolor=color_base,
        #clip_behavior=ClipBehavior.ANTI_ALIAS,
        expand=True,
        content=Column(
            controls=[
                language_txt,
                language_dropdown,
                
            ],
            horizontal_alignment=CrossAxisAlignment.CENTER,
            alignment=MainAxisAlignment.CENTER
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
                                        content     
                                    ]
                                ),
                            )
                        ]
                    ),
                ),
            ],
        ),
    )
    return View("/first", controls=[main_contianer])
