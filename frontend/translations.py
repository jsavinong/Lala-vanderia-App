import json
import os

translations = {}

def load_translations(language_code):
    try:
        # Construir la ruta al directorio locales de manera relativa a la ubicación de este script
        dir_path = os.path.dirname(os.path.abspath(__file__))
        locales_path = os.path.join(dir_path, '..', 'locales', f"{language_code}.json")

        # Imprimir la ruta del archivo para verificación
        print("Cargando traducciones desde:", locales_path)

        with open(locales_path, "r", encoding='utf-8') as file:
            global translations
            translations = json.load(file)
            
            # Imprime el contenido del archivo JSON
            #print(translations)

    except Exception as e:
        # Imprimir el error para diagnóstico
        print(f"Error cargando las traducciones: {e}")

def gettext(text):
    # Retorna la traducción si existe, de lo contrario el texto original
    return translations.get(text, text)
