class Clients ():
  def __init__(self):
    with open("clients.txt") as clients:
      self.listClients = [clients.replace("\n","")  for clients in clients.readlines() if clients != "\n" ]
      self.listClients = [clients.split("-") for clients in self.listClients]
      self.listClients.pop(0)


  def lookingForUser(self,ID):
    for i in self.listClients:
      if ID == i[1]:
        return i

    