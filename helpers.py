from colorama import Fore, Style

def pedir_numero(mensaje, tipo=int):
    try:
        return tipo(input(mensaje))
    except ValueError:
        print(f"{Fore.RED}Dato inválido. Debe ingresar un número válido.{Style.RESET_ALL}")
        return None
