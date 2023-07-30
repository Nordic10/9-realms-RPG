import socket
from _thread import *
from player import Player
import pickle

hostname = socket.gethostname()
server = socket.gethostbyname(hostname)
print("Server side IP: " + server)
port = 5555 # figure out a more personalized port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2) # figure out how to get rid of this line
print("Wating for a connection, Server Started")


players = [Player(0,0,50,50,(255,0,0)), Player(100,100, 50,50, (0,0,255))] #this is a list holding all the player objects, must add to(can only add 2 right now because of s.listen(2))

"""
This function takes in a connection and a player number and runs a continuous game loop.
Each player runs a version of this function simultaneously
"""
def threaded_client(conn, player_num): 
    conn.send(pickle.dumps(players[player_num])) #sends a player object to the client
    reply = "" #creates reply variable
    while True:
        try:
            data = pickle.loads(conn.recv(2048)) # data takes in and decodes a player object, of maximum size 2048bits(I think)
            players[player_num] = data # reassigns the server's player variable to what the client says it is

            if not data: # if the client sends no player class, that means it has disconnected
                print("Disconnected")
                break
            else: # sends the opposite player to the client to be drawn
                if player_num == 1:
                    reply = players[0]
                else:
                    reply = players[1]

                print("Received : ", data)
                print("Sending : ", reply)

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1