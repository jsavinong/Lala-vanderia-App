import flet as ft
from flet import UserControl, TextField, ElevatedButton, Column

class ServicioCard(UserControl):
    def __init__(self, servicio_id, nombre, descripcion, precio):
        # Es crucial llamar al constructor de la clase base en UserControl.
        # Si la clase base no tiene un constructor explícito, esta llamada no es necesaria.
        super().__init__()
        self.servicio_id = servicio_id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio

    def build(self):
        # Este método debe retornar los controles que componen la UI de ServicioCard.
        return Column([
            TextField(value=self.nombre, label="Nombre del servicio"),
            TextField(value=self.descripcion, label="Descripción"),
            TextField(value=f"${self.precio}", label="Precio"),
            ElevatedButton(text="Ordenar", on_click=self.ordenar_servicio)
        ])

    def ordenar_servicio(self, e):
        # Este es el manejador del evento cuando se hace clic en el botón de ordenar.
        print(f"Ordenando servicio con ID: {self.servicio_id}")

def main(page: ft.Page):
    page.title = "Lavandería a Domicilio - Servicios"
    
    # Creamos una instancia de ServicioCard y la añadimos a la página.
    servicio_card = ServicioCard(
        servicio_id=1,
        nombre="Lavado Completo",
        descripcion="Incluye lavado, secado y doblado de ropa.",
        precio=10.00
    )

    # El método build() se llama automáticamente cuando se añade el control a la página.
    page.add(servicio_card)

if __name__ == "__main__":
    ft.app(target=main)
