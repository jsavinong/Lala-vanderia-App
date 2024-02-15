import httpx
from flet import Page
import threading
import requests
from navigation import navigate_to


def signup_user(page: Page, nombre: str, correo_electronico: str, contraseña: str, direccion: str = None, telefono: str = None):
    def do_signup():
        url = "http://127.0.0.1:8000/users/sign_up/"  # Asegúrate de ajustar la URL a tu configuración
        data = {"nombre": nombre, 
                "correo_electronico": correo_electronico, 
                "contraseña": contraseña,
                "direccion": direccion,
                "telefono": telefono,
        }
        
        # Usar httpx.Client en lugar de httpx.AsyncClient
        with httpx.Client() as client:
            response = client.post(url, json=data)
            if response.status_code == 200:
                # Este código se ejecuta en el hilo secundario.
                # Asegúrate de que cualquier actualización de la UI se ejecute en el hilo principal.
                # Puedes usar page.update() para enviar actualizaciones de UI seguras desde un hilo secundario
                #page.update()
                # Navegar al dashboard después de actualizar la página
                navigate_to(page, "/dashboard")
                print("Registro exitoso", "El usuario ha sido registrado correctamente.")
            else:
                # Manejo de error
                error_message = response.json().get("detail", "Error durante el registro")
                print("Error de Registro", error_message)

    # Iniciar la operación de registro en un hilo secundario
    threading.Thread(target=do_signup).start()

def check_email_registered_sync(correo_electronico: str) -> bool:
    try:
        response = requests.get(f"http://127.0.0.1:8000/users/verify_email/{correo_electronico}")
        if response.status_code == 200:
            return response.json()["is_registered"]
    except Exception as e:
        print(f"Error al verificar el correo: {e}")
    return False

def check_email_registered(email: str, callback):
    def run():
        is_registered = check_email_registered_sync(email)
        callback(is_registered)
        
    threading.Thread(target=run).start()

def fetch_user_info(correo_electronico: str, update_ui_callback):
    def run():
        try:
            response = httpx.get(f"http://127.0.0.1:8000/users/{correo_electronico}/name")
            if response.status_code == 200:
                user_data = response.json()
                update_ui_callback(user_data["nombre"])
            else:
                print("No se pudo obtener la información del usuario.")
        except Exception as e:
            print(f"Error al obtener la información del usuario: {e}")
    
    threading.Thread(target=run).start()

def login_user(page: Page, correo_electronico: str, contraseña: str, on_result):
    def do_login():
        url = "http://127.0.0.1:8000/login"  # Asegúrate de que esta URL es correcta
        data = {
            "correo_electronico": correo_electronico,
            "contraseña": contraseña,
        }
        
        with httpx.Client() as client:
            response = client.post(url, json=data)
            if response.status_code == 200:
                # Extrae el token de la respuesta
                token_data = response.json()
                access_token = token_data.get("access_token")
                # Aquí deberías almacenar el access_token para uso futuro en solicitudes autenticadas
                navigate_to(page, "/dashboard")
                #print("Inicio de sesión exitoso, token:", access_token)
                # Navegar al dashboard o actualizar el estado del usuario como "logueado"
                on_result(True, "Inicio de sesión exitoso")
            else:
                # En caso de error, pasar un mensaje de error
                on_result(False, "Error de Inicio de Sesión: Verifica tus credenciales.")

    threading.Thread(target=do_login).start()

