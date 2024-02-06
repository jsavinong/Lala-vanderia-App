from flet import *


# Lista vacía del historial de navegación de la app
navigation_history = []

def navigate_to(page: Page, route: str):
    # Añade la ruta al historial solo si es diferente a la última añadida
    if not navigation_history or (navigation_history and navigation_history[-1] != route):
        navigation_history.append(route)
    # Realiza la navegación
    page.go(route)


def go_back(page: Page):
    if len(navigation_history) > 1:
        # Elimina la ruta actual
        navigation_history.pop()
        # Obtén la última ruta como la nueva ruta actual
        previous_route = navigation_history[-1]
        # Navega a la ruta anterior sin añadirla nuevamente al historial
        page.go(previous_route)
    elif len(navigation_history) == 1:
        # Opcional: manejar el caso de volver a la página de inicio o raíz
        navigation_history.pop()
        page.go("/")  # Asume "/" como tu ruta raíz o de inicio

