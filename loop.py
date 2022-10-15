from time import sleep
import time
from client import Client
from clients import Clients
from accounts import Accounts

def Asking():
    c = Clients()
    id = input("Número de identificación:")
    looking = c.lookingForUser(id)

    if  looking != None:
      print(f"Hola {looking[0]}")
      time.sleep(2)
    else:
      name = input("Nombre completo(solo letras): ")
      password = input("Contraseña(Solo números): ")
      
      if name.isalpha() == True and id.isdigit() == True and password.isdigit() == True:
        c = Client(name.upper().strip(),id.strip(),password.strip())
        c.newAccount()
        print("\nCUENTA CREADA CON ÉXITO")
        time.sleep(3)
        
      else:
        print("\nDatos incorrectos, vuelve a intentar")
        time.sleep(2)

def Existing():
  c = Clients()
  id = input("Ingresa tu número de identificación: ")
  looking = c.lookingForUser(id)
  if  looking != None:
    selection = input(f"""
_____________________________   
                   
Hola {looking[0]}
1. Ver saldo en cuenta.
2. Depositar
3. Retirar
_____________________________

""")
  if selection == "1":
    a = Accounts()  
  
      
    