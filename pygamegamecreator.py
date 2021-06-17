import pygame
import random
import colorsys
from time import sleep

pygame.init()

white = (255,255,255)
black = (0,0,0)

red = (200,0,0)
light_red = (255,0,0)

orange = (255,104,45)
light_orange = (255,155,45)

yellow = (155,155,0)
light_yellow = (255,255,0)

green = (0,155,0)
light_green = (0,255,0)

blue = (0,0,155)
light_blue = (0,0,255)

clock = pygame.time.Clock()

smallfont = pygame.font.SysFont("comicsanms", 25)
medfont = pygame.font.SysFont("comicsanms", 50)
largefont = pygame.font.SysFont("comicsanms", 80)

gDisplay = None

def setDisplay(title, width, height):
    global gDisplay
    gameDisplay = pygame.display.set_mode((width, height))
    gDisplay = gameDisplay
    pygame.display.set_caption(title)

def fillScreen(color):
    global gDisplay
    gDisplay.fill(color)

def update():
    pygame.display.update()

def wait(sec):
    sleep(sec)

def text_objects(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()

def allow_closing():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

def message_to_screen(msg,color, x_displace=0, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (pygame.Surface.get_width() / 2)+x_displace, (pygame.Surface.get_height() / 2)+y_displace
    gameDisplay.blit(textSurf, textRect)
    
def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = ((buttonx+(buttonwidth/2)), buttony+(buttonheight/2))
    gameDisplay.blit(textSurf, textRect)
    
def button(text, text_color, x, y, width, height, inactive_color, active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit
                quit()
                
            if action == "controls":
                game_controls()

            if action == "play":
                gameLoop()

            if action == "main":
                game_intro()

    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x,y,width,height))
        
    text_to_button(text,text_color,x,y,width,height)