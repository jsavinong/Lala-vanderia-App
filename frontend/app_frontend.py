# import flet as ft
# from flet import Checkbox, TextField, ElevatedButton, Column, Row, Text
# from flet_core.control_event import ControlEvent

# def main(page: ft.Page) -> None:
#     page.title = "Sign Up"
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER
#     page.theme_mode = ft.ThemeMode.LIGHT
#     page.window_width = 400
#     page.window_height = 800
#     page.window_resizable = False

#     # Crea campos de texto para el nombre de usuario y la contraseña
#     text_username: TextField = TextField(label = "Username", text_align = ft.TextAlign.LEFT, width = 200)
#     text_password: TextField = TextField(label = "Password", text_align = ft.TextAlign.LEFT, width = 200, password = True)


#     # Crea Checkbox 
#     checkbox_signup: Checkbox = Checkbox(label = "Estoy de acuerdo con estos términos", value = False)

#     # Crea Botón "Sign Up"
#     button_signup: ElevatedButton = ElevatedButton(text = "Sign Up", width = 200, disabled = True)

#     def validate_fields(e: ControlEvent) -> None:
#         if all([text_username.value, text_password.value, checkbox_signup.value]):
#             button_signup.disabled = False
#         else:
#             button_signup.disabled = True

#         page.update()

#     def submit(e: ControlEvent) -> None:
#         print("Username: ", text_username.value)
#         print("Password: ", text_password.value)

#         page.clean()
#         page.add(
#             Row(
#                 controls=[Text(value = f'Welcome: {text_username.value}', size=20)],
#                 alignment=ft.MainAxisAlignment.CENTER
#             )
#         )

# # Enlazar funciones a la interfaz gráfica
#     checkbox_signup.on_change = validate_fields
#     text_username.on_change = validate_fields
#     text_password.on_change = validate_fields
#     button_signup.on_click = submit

# # Dibujar la Sign Up page
#     page.add(
#         Row(
#             controls=[
#                 Column(
#                     [text_username,
#                      text_password,
#                      checkbox_signup,
#                      button_signup]
#                 )
#             ],
#             alignment=ft.MainAxisAlignment.CENTER
#         )
#     )


# # Ejecutar la aplicación
# if __name__ == "__main__":
#      ft.app(target=main)
