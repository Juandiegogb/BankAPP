class Clients ():
  def __init__(self):
    with open("clients.txt") as clients:
      self.listClients = [clients.replace("\n","")  for clients in clients.readlines() if clients != "\n" ]
      self.listClients = [clients.split("-") for clients in self.listClients]
      self.listClients.pop(0)
      self.dictClients = {clients[1]:(clients[0],clients[2],clients[3]) for clients in self.listClients}


  def lookingForUser(self,id):
    return self.dictClients.get(id)

    
    
    