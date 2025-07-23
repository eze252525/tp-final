from colorama import init, Fore, Style
from db import crear_tabla
from ui import (
    mostrar_menu,
    opcion_agregar,
    opcion_mostrar,
    opcion_buscar,
    opcion_eliminar,
    opcion_actualizar
)

init(autoreset=True)
crear_tabla()

print(f"{Fore.CYAN}{Style.BRIGHT} BIENVENIDOS A LA TIENDA DE PRODUCTOS EL BIGUA")

while True:
    mostrar_menu()
    opcion = input("Ingrese opción: ")

    if opcion == "1":
        opcion_agregar()
    elif opcion == "2":
        opcion_mostrar()
    elif opcion == "3":
        opcion_buscar()
    elif opcion == "4":
        opcion_eliminar()
    elif opcion == "5":
        opcion_actualizar()
    elif opcion == "6":
        print(f"{Fore.BLUE}{Style.BRIGHT}Gracias por usar la tienda de EL BIGUA. ¡Hasta pronto!{Style.RESET_ALL}")
        break
    else:
        print(f"{Fore.RED}Opción inválida. Intente nuevamente.{Style.RESET_ALL}")
