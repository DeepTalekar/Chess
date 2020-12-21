import socket
import threading

print("Starting the Chess Server!!")

soc = socket.socket()

host = 'localhost'
port = 8091

clist = []

class Move (threading.Thread):
    def __init__(self, client, address):
        threading.Thread.__init__(self)
        self.client = client
        self.add = address
    
    def run(self):
        global clist
        clist.append(self.client)

        stringDict = self.client.recv(1024)
        stringDict = stringDict.decode()

        while stringDict != 'q':
            [soc.send(stringDict.encode()) for soc in clist]
            print("The data recieved from the Client with address {} is --> {}".format(self.add, stringDict))
            stringDict = self.client.recv(1024)
            stringDict = stringDict.decode()

        print("The Client with the address {} has been Disconnected".format(self.add))
        self.client.send("You just quitted the Game".encode())
        clist.remove(self.client)
        self.client.close()


soc.bind((host, port))

soc.listen(5)

while True:
    print("| Waiting for the Client |")
    client, address = soc.accept()
    print("Established Connection with a Client having the address ~ ", address)
    Move(client, address).start()
    
# Generally we want to keep the Server Running so below statements are useless but its just for the practice
soc.close()
print("Chess Server Shutting Down!!")