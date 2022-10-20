import time
import os

class Accounts():
  def __init__(self):
    with open("accounts.txt","r") as file:
      self.listAccounts = [Accounts.replace("\n","").split(",") for Accounts in file.readlines()]
      self.listAccounts.pop(0)
      self.dictAccounts = {Account[0]:[Account[1],Account[2]] for Account in self.listAccounts }

  def showBalance(self,id):
    accountData = self.dictAccounts.get(id)
    print(f"\nLa cuenta {accountData[0]} tiene un saldo de {accountData[1]}")
    
  def found(self,id,qFound):
    accountData = self.dictAccounts.get(id)
    qFound = qFound + int(accountData[1])
    accountData[1] = qFound
    self.dictAccounts[id] = accountData
    os.remove("accounts.txt")
    
    with open("accounts.txt","a") as file:
      for i in self.dictAccounts:
        x = self.dictAccounts.get(i)
        file.write(f"\n{i},{x[0]},{x[1]}")
    print(f"DEPOSITO REALIZADO CON ÉXITO, NUEVO SALDO : {qFound}")
    time.sleep(4)
    
    
  def withdrawal(self,id,qWithdrawal):
    try:
      accountData = self.dictAccounts.get(id)
      balance = int(accountData[1])
      
      if qWithdrawal <= balance:
        accountData[1] = balance - qWithdrawal
        self.dictAccounts[id] = accountData
        os.remove("accounts.txt")
        balance = int(accountData[1])
        with open("accounts.txt","a") as file:
          for i in self.dictAccounts:
            x = self.dictAccounts.get(i)
            file.write(f"\n{i},{x[0]},{x[1]}")
        print(f"RETIRO REALIZADO CON ÉXITO, NUEVO SALDO : {balance}")
        time.sleep(4)
        return True
      else:
        print("MONTO NO DISPONIBLE")
        time.sleep(2) 
    except ValueError :
      print("Solo números")
      time.sleep(3)
  
  