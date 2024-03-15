from flet import Page
from state import app_state

# Lista vacía del historial de navegación de la app
navigation_history = []

def navigate_to(page: Page, route: str, data=None):
    # Actualizar el estado con cualquier dato nuevo
    if data:
        for key, value in data.items():
            app_state["data"][key] = value
    
    # Añadir la ruta actual al historial de navegación
    app_state["navigation_history"].append(route)
    
    # Realizar la navegación
    page.go(route)



def go_back(page: Page):
    if len(app_state["navigation_history"]) > 1:
        # Eliminar la última ruta (actual) y obtener la anterior
        app_state["navigation_history"].pop()  # Elimina la ruta actual
        previous_route = app_state["navigation_history"][-1]  # Obtiene y elimina la ruta anterior
        # Navegar a la ruta anterior
        page.go(previous_route)
    elif len(app_state["navigation_history"]) == 1:
        # Si solo queda la ruta inicial, navegar a ella y luego limpiar el historial
        page.go("/")
        app_state["navigation_history"] = []


