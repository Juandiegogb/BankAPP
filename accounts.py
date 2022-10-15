import time


class Accounts():
    def __init__(self):
        with open("accounts.txt") as file:
            self.listAccounts = [Accounts.replace("\n","").split(",") for Accounts in file.readlines()]
            self.listAccounts.pop(0)
            print(self.listAccounts)
            self.dictAccounts = {Accounts[0]:(Accounts[1],Accounts[2]) for Accounts in self.listAccounts}
            print(self.dictAccounts)
            time.sleep(898)
            
        