import os
import subprocess
import ctypes
import sys

def hide_console():
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    if hwnd:
        ctypes.windll.user32.ShowWindow(hwnd, 0)

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

def exit_with_message(message="Presione una tecla para continuar . . ."):
    input(message)
    hide_console()
    sys.exit()

def main(options):
    if not options:
        print("No se encontraron archivos JAR en el directorio especificado.")
        exit_with_message()

    print("Selecciona un archivo JAR para ejecutar:")
    for idx, option in enumerate(options):
        file_name = os.path.basename(option)
        print(f"{idx + 1}. {file_name}")

    while True:
        choice = input(f"Introduce el número (1-{len(options)}) o 'q' para salir: ")
        if choice.lower() == 'q':
            exit_with_message("Saliendo...")
        try:
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(options):
                selected_jar = options[choice_index]
                print(f"Ejecutando {selected_jar}...")
                subprocess.run(["java", "-jar", selected_jar])
                exit_with_message()
            else:
                print("Selección inválida. Intenta nuevamente.")
        except ValueError:
            print("Entrada no válida. Debes ingresar un número.")

show_console()
while True:
    directory = input("Introduce el directorio para buscar archivos JAR (o 'q' para salir): ")
    if directory.lower() == 'q':
        exit_with_message("Saliendo del programa...")
    if os.path.isdir(directory):
        options = get_filtered_files(directory)
        if options:
            main(options)
            break
        else:
            print("No se encontraron archivos JAR. Intenta con otro directorio.")
    else:
        print("El directorio especificado no es válido. Intenta nuevamente.")
