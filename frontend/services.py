import httpx
from flet import Page
import threading
import requests


async def signup_user(page: Page, email: str, password: str):
    url = "http://127.0.0.1:8000/users/sign_up/"  # Asegúrate de ajustar la URL a tu configuración
    data = {"email": email, "password": password}
    
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=data)
        if response.status_code == 200:
            # Aquí asumimos que el registro fue exitoso
            
            page.dialog("Registro exitoso", "El usuario ha sido registrado correctamente.")
        else:
            # Manejo de error
            error_message = response.json().get("detail", "Error durante el registro")
            page.dialog("Error de Registro", error_message)

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