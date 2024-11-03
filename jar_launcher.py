import os
import subprocess
import ctypes

def show_console():
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    if hwnd:
        ctypes.windll.user32.ShowWindow(hwnd, 5)

def get_filtered_files(directory):
    extension = ".jar"
    filtered_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                filtered_files.append(os.path.join(root, file))
    return filtered_files

def main(options):
    if not options:
        print("No se encontraron archivos JAR en el directorio especificado.")
        return

    # Muestra las opciones de JAR
    print("Selecciona un archivo JAR para ejecutar:")
    for idx, option in enumerate(options):
        file_name = os.path.basename(option)  # Obtener solo el nombre del archivo
        print(f"{idx + 1}. {file_name}")  # Muestra el nombre del archivo

    # Solicita la selección del usuario
    choice = input(f"Introduce el número (1-{len(options)}) o 'q' para salir: ")
    
    if choice.lower() == 'q':
        print("Saliendo...")
        return

    # Verifica si la elección es válida
    try:
        choice_index = int(choice) - 1
        if 0 <= choice_index < len(options):
            selected_jar = options[choice_index]
            print(f"Ejecutando {selected_jar}...")
            subprocess.run(["java", "-jar", selected_jar])
        else:
            print("Selección inválida.")
    except ValueError:
        print("Entrada no válida. Debes ingresar un número.")

# Entrada de directorio y ejecución del menú
show_console()
directory = input("Introduce el directorio para buscar archivos JAR: ")
options = get_filtered_files(directory)
main(options)
