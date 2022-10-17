import time

class Accounts():
  def __init__(self):
    with open("accounts.txt") as file:
      self.listAccounts = [Accounts.replace("\n","").split(",") for Accounts in file.readlines()]
      self.listAccounts.pop(0)
      self.dictAccounts = {Account[1]:[Account[0],Account[2]] for Account in self.listAccounts }

  def showAccountsByID(self,id):
    account = {self.dictAccounts.get(account) for account in self.dictAccounts}
    print(account,id)
    time.sleep(50)
            
        