from time import sleep
import time
from accounts import Accounts
from client import Client
from clients import Clients


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
      
def Existing( id = ""):
  l = "\n_____________________________\n"
  c = Clients()
  while True:
    data = c.lookingForUser(id)
    if id != "" and  data != None:
      password = input("\nIngresa tu contraseña( * para salir): ")
      if password == data[1]:
        print(f"\n\nHola {data[0]}")
        break
      elif password== "*":
        exit()
    else:
      id = input("\nIngresa tu número de identificación: ").strip()
      
  selection = input(f"{l} \n1. Ver saldo\n2. Depositar\n3. Retirar\n4. Salir{l}\n")
  if selection == "1":
    a = Accounts()
    a.showAccountsByID(id)
  elif selection == "4":
    exit()
    