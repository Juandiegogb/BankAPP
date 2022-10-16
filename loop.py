from time import sleep
import time
from client import Client
from clients import Clients
from accounts import Accounts


def Asking():
  c = Clients()
  id = input("Número de identificación: ")
  looking = c.lookingForUser(id)

  if looking != None:
    print(f"\nHola {looking[0]}")
    Existing(id = id)

  else:
    name = input("Nombre completo(solo letras): ")
    password = input("Contraseña(Solo números): ")

    if (name.isalpha() == True and id.isdigit() == True and password.isdigit() == True):
      c = Client(name.upper().strip(), id.strip(), password.strip())
      c.newAccount()
      print("\nCUENTA CREADA CON ÉXITO")
      time.sleep(3)

    else:
      print("\nDatos incorrectos, vuelve a intentar")
      time.sleep(2)
      
def Existing(id=""):
  c = Clients()
  while True:
    if id == "":
        id = input("\nIngresa tu número de identificación: ")
    else:
      looking = c.lookingForUser(id)      
      if looking == None:
        print("\nCuenta no encontrada, crea una \n")
        time.sleep(2)
        Asking()
      else:
        password = input("\nIngresa tu contraseña: ").strip()
        if looking != None and looking[2] == password:
          selection = input(
              f"""
_____________________________   

Hola {looking[0]}
1. Ver saldo en cuenta.
2. Depositar
3. Retirar
_____________________________

""")
          if selection == "1":
            a = Accounts()
            break
        else:
          print("\nContraseña incorrecta")
          time.sleep(1)
