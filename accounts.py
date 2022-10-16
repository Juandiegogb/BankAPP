import time


class Accounts():
    def __init__(self):
        with open("accounts.txt") as file:
            self.listAccounts = [Accounts.replace("\n","").split(",") for Accounts in file.readlines()]
            self.listAccounts.pop(0)
            self.dictAccounts = {Account[0]:[(Account[1],Account[2])] for Account in self.listAccounts }
            print(self.dictAccounts)
            time.sleep(4)

            
        