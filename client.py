from  account import Account

class Client():
  def __init__(self,name,id,password):
    self.name = name
    self.id = id
    self.password = password
    self.accountID = []
    
  def newAccount(self):
    with open("accounts.txt") as accounts:
      accountID = len(accounts.readlines()) + 742313521
      self.accountID.append(accountID)
      a = Account(str(accountID),self.id)

    with open("clients.txt","a") as clients:
      clients.write(f" \n{self.name}-{self.id}-{self.password}-{self.accountID}")
    

  def showInfo(self):
    print(self.name, self.id, self.password , self.accountID)

   
      
    