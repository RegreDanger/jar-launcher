import re

def display_menu():
    letters = [chr(i).lower() for i in range(65, 91)]  # Letras A-Z
    special_keys = ["Ctrl", "Shift", "Alt"]

    box_width = 60  # Ancho fijo de la caja
    keys_per_row = 5  # Número de teclas por fila

    # Imprimir la parte superior de la caja
    print("+" + "-" * (box_width - 2) + "+")
    print("| Opciones de teclas disponibles:".ljust(box_width - 1) + "|")
    print("+" + "-" * (box_width - 2) + "+")

    # Imprimir teclas en filas (letras) con enumeración
    for i in range(0, len(letters), keys_per_row):
        row = letters[i:i + keys_per_row]
        enumerated_row = [f"{j + i + 1}. {row[j]}" for j in range(len(row))]
        row_display = ' | '.join(enumerated_row)
        print(f"| {row_display.ljust(box_width - 4)} |")

    print("+" + "-" * (box_width - 2) + "+")
    print("| Teclas Especiales".ljust(box_width - 1) + "|")
    print("+" + "-" * (box_width - 2) + "+")

    # Imprimir teclas especiales con enumeración
    for i in range(0, len(special_keys), keys_per_row):
        row = special_keys[i:i + keys_per_row]
        enumerated_row = [f"{j + i + 1 + len(letters)}. {row[j]}" for j in range(len(row))]
        row_display = ' | '.join(enumerated_row)
        print(f"| {row_display.ljust(box_width - 4)} |")

    print("+" + "-" * (box_width - 2) + "+")
    return letters + special_keys
    
def is_valid_hotkey(hotkey):
    pattern = r'^(Ctrl|Alt)(\+Shift)?\+?[a-z]$|^(Shift|Alt\+)?((?<=Alt)Shift\+)[a-z]$'
    return re.match(pattern, hotkey) is not None

def set_hotkey():
    keys = display_menu()
    selected_keys = []
    
    while True:
        choice = input("\nSelecciona una tecla (1-{}) o 'q' para terminar: ".format(len(keys)))
        
        if choice == 'q':
            if is_valid_hotkey('+'.join(selected_keys)): 
                print("Hotkey válida. Finalizando selección.")
                break
            else:
                print("Combinación inválida. Vaciando el hotkey.")
                selected_keys = []
                break

        try:
            choice = int(choice)
            if 1 <= choice <= len(keys):
                selected_key = keys[choice - 1]
                
                # Verificar si la tecla ya ha sido seleccionada
                if selected_key in selected_keys:
                    print(f"La tecla '{selected_key}' ya fue seleccionada. Elige otra.")
                else:
                    selected_keys.append(selected_key)
                    print(f"Tecla '{selected_key}' añadida a la combinación actual: {'+'.join(selected_keys)}")
                    
            else:
                print("Opción no válida. Inténtalo de nuevo.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
    
    if selected_keys:
        new_hotkey = '+'.join(selected_keys)
        with open("config.txt", "w") as file:
            file.write(new_hotkey.strip())
        print(f"La combinación de teclas ha sido actualizada a: {new_hotkey.strip()}")
    else:
        print("No se seleccionó ninguna tecla.")

if __name__ == "__main__":
    set_hotkey()
