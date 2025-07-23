from colorama import Fore, Style
from db import (
    agregar_producto,
    obtener_productos,
    buscar_producto_por_nombre,
    eliminar_producto,
    obtener_producto_por_id,
    actualizar_producto,
)
from helpers import pedir_numero

def mostrar_menu():
    print(f"\n{Fore.YELLOW}----- Menú de Productos -----{Style.RESET_ALL}")
    print("1. Agregar Productos")
    print("2. Mostrar Productos")
    print("3. Buscar Productos")
    print("4. Eliminar Producto")
    print("5. Actualizar Producto")
    print("6. Salir")

def opcion_agregar():
    nombre = input("Nombre del producto: ").title().strip()
    descripcion = input("Descripción: ").strip()
    
    cantidad = pedir_numero("Cantidad disponible: ", int)
    precio = pedir_numero("Precio: ", float)
    if cantidad is None or precio is None:
        return

    categoria = input("Categoría: ").title().strip()
    agregar_producto(nombre, descripcion, cantidad, precio, categoria)
    print(f"{Fore.GREEN}Producto agregado con éxito.{Style.RESET_ALL}")

def opcion_mostrar():
    productos = obtener_productos()
    if not productos:
        print(f"{Fore.YELLOW}No hay productos registrados.{Style.RESET_ALL}")
    else:
        print(f"{Fore.GREEN}--- Lista de Productos ---{Style.RESET_ALL}")
        for p in productos:
            print(f"ID: {p[0]}, Nombre: {p[1]}, Categoría: {p[2]}, Precio: ${p[3]:.2f}")

def opcion_buscar():
    nombre = input("Nombre del producto a buscar: ").title().strip()
    producto = buscar_producto_por_nombre(nombre)
    if producto:
        print(f"{Fore.GREEN}Producto encontrado: {producto[0]}, Categoría: {producto[1]}, Precio: ${producto[2]:.2f}{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Producto no encontrado.{Style.RESET_ALL}")

def opcion_eliminar():
    productos = obtener_productos()
    if not productos:
        print(f"{Fore.YELLOW}No hay productos para eliminar.{Style.RESET_ALL}")
        return
    
    for p in productos:
        print(f"ID: {p[0]} - {p[1]}")
    id_eliminar = pedir_numero("Ingrese el ID del producto a eliminar: ", int)
    if id_eliminar is not None:
        eliminar_producto(id_eliminar)
        print(f"{Fore.GREEN}Producto eliminado con éxito.{Style.RESET_ALL}")

def opcion_actualizar():
    id_producto = pedir_numero("Ingrese el ID del producto a actualizar: ", int)
    if id_producto is None:
        return

    producto = obtener_producto_por_id(id_producto)
    if not producto:
        print(f"{Fore.RED}No existe un producto con ese ID.{Style.RESET_ALL}")
        return

    print(f"{Fore.CYAN}Producto actual:{Style.RESET_ALL}")
    print(f"Nombre: {producto[1]}, Descripción: {producto[2]}, Cantidad: {producto[3]}, Precio: {producto[4]}, Categoría: {producto[5]}")

    nombre = input("Nuevo nombre: ").title().strip()
    descripcion = input("Nueva descripción: ").strip()
    cantidad = pedir_numero("Nueva cantidad: ", int)
    precio = pedir_numero("Nuevo precio: ", float)
    categoria = input("Nueva categoría: ").title().strip()

    if cantidad is not None and precio is not None:
        actualizar_producto(id_producto, nombre, descripcion, cantidad, precio, categoria)
        print(f"{Fore.GREEN}Producto actualizado correctamente.{Style.RESET_ALL}")
