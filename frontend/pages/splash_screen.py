from flet import *
from flet_route import Params, Basket
from utils.extras import *
import threading

def splash_screen_view(page: Page, params: Params=None, basket: Basket=None):
    logo = Image(src="https://jsavinong.github.io/Lala-vanderia-App/frontend/assets/images/flet.png")
    
    content = Container(
        #height=altura_base,
        width=anchura_base,
        #bgcolor=color_base,
        #clip_behavior=ClipBehavior.ANTI_ALIAS,
        expand=True,
        content=Column(
            controls=[
                logo
                
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
                    bgcolor="white"
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

        # Función para cambiar de vista
    def change_view():
        page.go("/idioma")  # Cambia a la página de selección de idioma o la página principal

        # Configurar y empezar el temporizador
    timer = threading.Timer(2.0, change_view)  # Temporizador de 2 segundos
    timer.start()

    return View("/splash", controls=[main_contianer])
