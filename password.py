import secrets

dicc_letras_num_carac = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 
'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 
'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '"', '#', '$', '%', 
'&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', 
'\\', ']', '^', '_', '`', '{', '|', '}', '~']

dicc_palabras = ['casa', 'perro', 'gato', 'libro', 'mesa', 'silla', 'sol', 'luna', 'flor', 
'cielo', 'mar', 'tierra', 'árbol', 'viento', 'agua', 'fuego', 'puerta', 'ventana', 'pluma', 
'lápiz', 'mano', 'pie', 'ojo', 'boca', 'nariz', 'oreja', 'pelo', 'cabeza', 'brazo', 'pierna', 
'house', 'dog', 'cat', 'book', 'table', 'chair', 'sun', 'moon', 'flower', 'sky', 'sea', 'earth', 
'tree', 'wind', 'water', 'fire', 'door', 'window', 'feather', 'pencil', 'hand', 'foot', 'eye',
'mouth', 'nose', 'ear', 'hair', 'head', 'arm', 'leg']

dicc_caracteres =['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', 
':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

def passwd_generador(opcion, longitud, separador=None):
    if opcion == 1:
        contra = ''.join(secrets.choice(dicc_letras_num_carac) for _ in range(longitud))
    elif opcion == 2:
        if separador:
            contra = separador.join(secrets.choice(dicc_palabras) for _ in range(longitud))
        else:
            separador = secrets.choice(dicc_caracteres)
            contra = separador.join(secrets.choice(dicc_palabras) for _ in range(longitud))
    return contra

def mostrar_menu():
    print("Bienvenido al generador de contraseñas")
    print("1. Generar contraseña clásica")
    print("2. Generar contraseña alternativa")
    print("3. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            while True:
                longitud = int(input("Ingrese la longitud de la contraseña (mínimo 8 caracteres): "))
                if longitud >= 8:
                    break
                else:
                    print("La longitud mínima es 8. Intente nuevamente.")
            contraseña = passwd_generador(1, longitud)
            print(f"Su contraseña generada es: {contraseña}")
        
        elif opcion == '2':
            print("Esta contraseña se generará usando palabras en inglés y español, separadas por un carácter especial.")
            while True:
                longitud = int(input("Ingrese la cantidad de palabras (mínimo 8 palabras): "))
                if longitud >= 8:
                    break
                else:
                    print("La cantidad mínima de palabras es 8. Intente nuevamente.")
            separador = input("Ingrese un separador (o presione Enter para un separador aleatorio): ")
            if separador == "":
                separador = None
            contraseña = passwd_generador(2, longitud, separador)
            print(f"Su contraseña generada es: {contraseña}")
        
        elif opcion == '3':
            print("Gracias por usar el generador de contraseñas. ¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()