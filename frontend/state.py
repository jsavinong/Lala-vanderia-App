# Definición del estado global de la aplicación
# Este diccionario actúa como almacenamiento centralizado para todos los datos globales y el historial de navegación
app_state = {
    "data": {},  # Diccionario para almacenar datos globales como configuraciones de usuario, datos de sesión, etc.
    "navigation_history": [],  # Lista para mantener un registro de todas las rutas visitadas para la navegación hacia atrás+
    "selected_nav_index": 0,
}

# Función para actualizar datos dentro del estado global
# Esta función abstrae la lógica de actualizar el diccionario de datos, permitiendo una fácil modificación de los datos globales
def update_state(key, value):
    global app_state  # Referencia al estado global
    app_state["data"][key] = value  # Actualiza el diccionario de datos con el nuevo valor para la clave dada

# Función para obtener datos del estado global
# Proporciona una forma segura de acceder a los datos globales, devolviendo un valor predeterminado si la clave no existe
def get_state(key, default=None):
    return app_state["data"].get(key, default)  # Retorna el valor para la clave dada desde el diccionario de datos, o un valor predeterminado

