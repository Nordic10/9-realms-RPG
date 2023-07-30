import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.0.25"
        self.port = 5555 # figure out a more personalized port
        self.addr = (self.server, self.port)
        self.p = self.connect() # this holds the player object that is assigned to the client

    """
    Getter Function for p
    """
    def getP(self):
        return self.p

    """
    connect() is only meant to be run once. It recieves the player object that has been assigned to the client from the server
    """
    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048))
        except:
            pass
    
    """
    send() is meant to be run constantly throughout the run of the client code. It deals with %100 percent of the data sending
    and recieving on the client side. It sends the client's version of it's own player, and returns the server's version of
    the other player.
    """
    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)