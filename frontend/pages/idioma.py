from flet import *
from utils.extras import *
from flet_route import Params, Basket
from state import update_state, get_state
from navigation import navigate_to
from config.translations import gettext as _
from flet import *
from config.translations import load_translations, gettext as _
from utils.extras import *

# Esta función podría estar en otro módulo, como parte de tu lógica de navegación o estado global
def on_language_change(e, page):
    # Actualizar las traducciones basadas en el idioma seleccionado
    language_code = e.control.value
    load_translations(language_code)
    
    # Actualizar el estado global o almacenamiento local con el nuevo idioma seleccionado
    update_state("user_language", language_code)
    print("llega aquí")
    # Navegar a la página principal o la siguiente vista después de la selección del idioma
    navigate_to(page, "/")  # Asumiendo que "/" es tu página principal

def idioma_page_view(page: Page, params: Params=None, basket: Basket=None):
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
        height=altura_base,
        width=anchura_base,
        bgcolor=color_base,
        clip_behavior=ClipBehavior.ANTI_ALIAS,
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

    return View("/idioma", controls=[content])
