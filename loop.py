import os
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
  a = Accounts()
  while True:
    data = c.lookingForUser(id)
    if id != "" and  data != None:
      password = input("\nIngresa tu contraseña( * para salir): ")
      if password == data[1]:
        break
      elif password== "*":
        exit()
    else:
      id = input("\nIngresa tu número de identificación: ").strip()
   
  while True:   
    selection = input(f"{l}\nHola {data[0]}\n\n1. Ver saldo\n2. Depositar\n3. Retirar\n4. Enviar dinero{l}\n")
    if selection == "1":
      a.showBalance(id)
      time.sleep(3)
    elif selection == "2":
      qFound = int(input("\n¿Cuanto dinero quieres depositar?"))
      a.found(id,qFound)
    elif selection == "3":
      qWithdrawal = int(input(f"\n¿Cuanto dinero quieres retirar?  "))
      a.withdrawal(id,qWithdrawal)
    
    elif selection == "4":
      receiverID = input("\nIngresa tu número de identificación del destinatario: ").strip()
      inClients = c.lookingForUser(receiverID)
      if inClients == None:
        print("\nNO SE ENCONTRARON USER CON ESE ID")
      else:
        qWithdrawal = int(input(f"\n¿Cuanto dinero quieres enviar?  "))
        withdrawal = a.withdrawal(id,qWithdrawal)
        if withdrawal == True:
          qFound = qWithdrawal
          a.found(receiverID,qFound)
          os.system("cls")
          print("ENVIO DE DINERO EXITOSO")
          break

    else:
      exit()
    