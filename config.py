class Store:
  def __init__(self, id, gpsx, gpsy, tag):
    self.id = id
    self.gpsx = gpsx
    self.gpsy = gpsy
    self.tag = tag

class person:
    wallet = 0
    def __init__(self, id, name, wallet, tags):
        self.id = id
        self.name = name
        self.wallet = wallet
        self.tags = tags
    def remit(self,amount):
        self.wallet = self.wallet-int(amount)

s1 = Store('DEL121', 10, 10, "Big Bazaar")
s2 = Store('GUR101', 12, 10, "NEC Store")
stList = [s1,s2]

p1 = person(122001, 'John Doe', 1500, ['snacks', 'stationery', 'magzine'])
p2 = person(101101, 'Mary Jane', 1800, ['cosmetics', 'laundry', 'grocery'])
prList = [p1,p2]  

swarm = []


def addswarm(usrid,gpsx,gpsy):
    if(p1.id == int(usrid) and s1.gpsx==int(gpsx) and s1.gpsy == int(gpsy)):
        swarm.append((p1,s1))
        return "User Checked in at Big Bazaar"

    elif(p1.id == int(usrid) and s2.gpsx==int(gpsx) and s2.gpsy == int(gpsy)):
        swarm.append((p1,s2))
        return "User Checked in at NEC Store"

    elif(p2.id == int(usrid) and s1.gpsx==int(gpsx) and s1.gpsy == int(gpsy)):
        swarm.append((p2,s1))
        return "User Checked in at Big Bazaar"

    elif(p2.id == int(usrid) and s2.gpsx==int(gpsx) and s2.gpsy == int(gpsy)):
        swarm.append((p2,s2))
        return "User Checked in at NEC Store"

    else :
        print("Cannot detect Check In")
        return "Cannot check you InN"

def delswarm(p,s):
    swarm.remove((p,s))

def flushswarm():
    swarm.clear()

def remittence(person,amt):
    person.remit(amt)