class Account():
  def __init__(self,accountID,ownerID):
    self.balance = 0
    self.accountID = accountID
    self.ownerID = ownerID

    with open("accounts.txt","a") as accounts:
      accounts.write(f"\n{self.ownerID},{self.accountID},{self.balance}")
    
    