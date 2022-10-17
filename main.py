import time
from loop import Asking, Existing
from clients import Clients
import os

while True:
  os.system("cls")
  l = "\n_____________________________\n"
  selection = input(f"{l}\nBIENVENIDO AL BANCO NACIONAL\n\n¿Qué quieres hacer ?\n\n1. Abrir una nueva cuenta\n2. Ver cuenta existente\n3. Salir{l}\n")
  if selection == "1":
    print("\nHola, a continuación te pediremos unos datos para crear tu cuenta.\n")
    Asking()
  elif selection == "2":
    id = input("\nIngresa tu número de identificación: ")
    Existing(id = id.strip())
  elif selection == "3":
    exit()
    
