import keyboard
import threading
import time
import os
import logging
import ctypes
import subprocess

ctypes.windll.kernel32.SetConsoleTitleW("Listener de Hotkeys")

def is_running():
    try:
        with open("process_id.txt", "r") as file:
            pid = int(file.read().strip())
            os.kill(pid, 0)
            return True
    except (FileNotFoundError, OSError):
        return False

def save_process_id():
    process_id = os.getpid()
    subprocess.run(['attrib', '-h', 'process_id.txt'], check=True)
    with open("process_id.txt", "w") as pid_file:
        pid_file.write(str(process_id))
    
    logging.info(f"ID del proceso guardado en 'process_id.txt': {process_id}")
    subprocess.run(['attrib', '+h', 'process_id.txt'], check=True)
    logging.info("El archivo 'process_id.txt' ha sido oculto.")


def hide_console():
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    if hwnd:
        ctypes.windll.user32.ShowWindow(hwnd, 0)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("hotkey_listener.log")
    ]
)

def load_hotkey():
    try:
        with open("config.txt", "r") as file:
            hotkey = file.read().strip()
            return hotkey
    except FileNotFoundError:
        return None

def hotkey_listener():
    while True:
        hotkey = load_hotkey()
        if hotkey:
            logging.info(f"Escuchando la combinación: {hotkey}")
            keyboard.add_hotkey(hotkey, lambda: execute_jar_laucher(hotkey))
            keyboard.wait("esc")
            break
        else:
            logging.warning("Archivo config.txt no encontrado. Por favor, configúralo y reinicia el listener.")
            time.sleep(5)
            continue

def execute_jar_laucher(hotkey):
    logging.info(f"¡Hotkey '{hotkey}' detectada! Ejecutando jar_laucher.py...")
    try:
        subprocess.run(["python", "jar_launcher.py"], check=True)
    except Exception as e:
        logging.error(f"Error al ejecutar jar_laucher.py: {e}")

def start_listener_in_background():
    confirm = input("¿Deseas iniciar el listener de hotkeys en segundo plano? (S/N): ").strip().upper()
    if confirm == 'S':
        is_running()
        save_process_id()
        hide_console()
        listener_thread = threading.Thread(target=hotkey_listener)
        listener_thread.daemon = True
        listener_thread.start()

        logging.info("Listener iniciado en segundo plano. Presiona 'Esc' para salir del programa principal.")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            logging.info("\nPrograma finalizado.")
    else:
        print("El listener no se ha iniciado. Saliendo del programa.")

if __name__ == "__main__":
    start_listener_in_background()
