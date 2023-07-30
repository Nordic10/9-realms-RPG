import pygame
from network import Network
from player import Player

width = 500 # variables for window size. CHANGE THESE.
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client") # sets window caption. Game name goes here.

"""
This function draws everything on the client's screen acording to the object's draw function
"""
def redrawWindow(win, player, player2):
    win.fill((255,255,255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()

"""
Starts the client, and maintains the server conection within the while loop
"""
def main():
    run = True
    n = Network()
    p = n.getP() # network.p is equal to what network.connect() returns
    """
    network.connect is a function that is only meant to be called once. It establishes a connection with the server and it
    returns the player that the client is.
    """
    clock = pygame.time.Clock()

    while run:
        clock.tick(60) #I think this creates a delay, but I'm not sure
        p2 = n.send(p) # network.send() sends an object p to the server, and returns whatever the server sends back(the other player)

        p.move() # moves the client's player
        redrawWindow(win, p, p2) # draws all players on the client's screen

        for event in pygame.event.get(): # makes the exit button work
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            

main()