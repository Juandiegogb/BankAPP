import time
from loop import Asking, Existing
from clients import Clients
import os


while True:
    os.system("exit")
    os.system("cls")
    C = Clients()
    selection = input(
        """

_____________________________________

BIENVENIDO AL BANCO NACIONAL

¿Qué quieres hacer ?
1. Abrir una nueva cuenta
2. Ver cuenta existente
3. Salir
_____________________________________

"""
    )
    if selection == "1":
        print("\nHola, a continuación te pediremos unos datos para crear tu cuenta.\n")
        Asking()
    elif selection == "2":
        try:
            Existing()
        except UnboundLocalError:
            print("\nCuenta no encontrada, crea una \n")
            time.sleep(2)
            Asking()
    elif selection == "3":
        exit()
