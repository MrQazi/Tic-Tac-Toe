import pygame
import time
import mylib

pygame.init()

game_display = pygame.display.set_mode((600,800))
pygame.display.set_caption("Tic Tac Toe")

def calculate(array):
    array[1][4] = array[1][1]+array[1][2]+array[1][3]
    array[2][4] = array[2][1]+array[2][2]+array[2][3]
    array[3][4] = array[3][1]+array[3][2]+array[3][3]
    array[4][1] = array[1][1]+array[2][1]+array[3][1]
    array[4][2] = array[1][2]+array[2][2]+array[3][2]
    array[4][3] = array[1][3]+array[2][3]+array[3][3]
    array[4][4] = array[1][1]+array[2][2]+array[3][3]
    array[0][4] = array[1][3]+array[2][2]+array[3][1]
    return array

def home(msg,color):
    game_display.fill(color)
    surf,body = mylib.game.message(msg,(300,400),50,(255,255,255))
    game_display.blit(surf,body)
    pygame.display.update()
    time.sleep(3)
    exit()

def design():
        game_display.blit(pygame.image.load("back.png"),(0,0))
        pygame.draw.rect(game_display,(0,0,0),(0,600,600,200))

def main():
    
    player = -1
    sketch = [[0 for i in range(5)] for i in range(5)]
    used = 0
    color = ((155,0,0),(0,155,0),(0,0,155))
    
    while True:
        
        msg = "Player "+str(mylib.physics.my_bool(player)+1)+"'s Turn"
        design()

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()[0]

        if mouse_click == 1 and 0 < mouse_pos[0] < 600 and 0 < mouse_pos[1] < 600 :
            x = int(mouse_pos[0]/200)
            y = int(mouse_pos[1]/200)
        
            if sketch[y+1][x+1] == 0:
                sketch[y+1][x+1] = player
                used += 1
                player *= -1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        sketch = calculate(sketch)
        for y in range(3):
            for x in range(3):
                if sketch[y+1][x+1] == -1:
                    game_display.blit(pygame.image.load("ring.png"),(x*200+10,y*200+10))
                if sketch[y+1][x+1] == 1:
                    game_display.blit(pygame.image.load("cross.png"),(x*200+10,y*200+10))
                if sketch[y+2][x+2] == -3*player  or sketch[y][x+2] == -3*player:
                    time.sleep(2)
                    home("Player "+str((not mylib.physics.my_bool(player))+1)+" Wins !!!",color[1-player])
        if used == 9:
            home("Oops! Draw !!!",(155,155,155))

        surf , body = mylib.game.message(msg,(300,700),50,(255,255,255))
        game_display.blit(surf,body)

        pygame.display.update()

main()
