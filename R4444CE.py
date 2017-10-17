import pygame
import time
import random
import cx_Freeze


pygame.init()

display_width = 800
display_height = 600


black = (0,0,0)
white = (255,255,255)

red   = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)

block_color = (15,25,255)


car_width = 73

pause = False
#crash = True

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('R4444CE')
clock = pygame.time.Clock()

carImg = pygame.image.load('car1.png')
gameIcon = pygame.image.load('icon1.png')

pygame.display.set_icon(gameIcon)

def quit_game():
    pygame.quit()
    quit()
    
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
            
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("Verdana",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def things_dodged(count):
    font = pygame.font.SysFont("Verdana", 25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.SysFont("Verdana",115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()


def crash():
    
    largeText = pygame.font.SysFont("Verdana", 115)
    TextSurf, TextRect = text_objects("PRZEGRALES", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    
    while True:
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                pygame.quit()
                quit()

       # gameDisplay.fill(white)
        
        button("PLAY AGAIN!", 150, 450, 100, 50, green, bright_green,game_loop)
        button("WYJSCIE", 550, 450, 100, 50, red, bright_red,quit_game)

        pygame.display.update()
        clock.tick(15)


def unpouse():
    global pause
    pause = False

def paused():

    largeText = pygame.font.SysFont("Verdana", 115)
    TextSurf, TextRect = text_objects("PAUSED", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    
    while pause:
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                pygame.quit()
                quit()

       # gameDisplay.fill(white)
        
        button("KONTYNUUJ!", 150, 450, 100, 50, green, bright_green,unpouse)
        button("WYJSCIE", 550, 450, 100, 50, red, bright_red,quit_game)

        pygame.display.update()
        clock.tick(15)

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)      
        largeText = pygame.font.SysFont("Verdana", 115)
        TextSurf, TextRect = text_objects("R4444CE", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)
        
        button("START", 150, 450, 100, 50, green, bright_green,game_loop )
        button("WYJSCIE", 550, 450, 100, 50, red, bright_red, quit_game)

        pygame.display.update()
        clock.tick(15)


def game_loop():
    global pause
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100

    gameExit = False
    dodged = 0
    
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    # ------------- INMPUTS ----------------- #
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_DOWN]: y += 4.5
        if pressed[pygame.K_UP]: y -= 4.5
        if pressed[pygame.K_LEFT]: x -= 4.5
        if pressed[pygame.K_RIGHT]: x += 4.5
        if pressed[pygame.K_p]:
            pause = True
            paused()
        if pressed[pygame.K_m]:
               game_loop
    # ------------- INMPUTS ----------------- #
        x += x_change
        gameDisplay.fill(white)

        

        things(thing_startx, thing_starty, thing_width, thing_height, block_color)

        thing_starty += thing_speed
        car(x, y)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)

        if y < thing_starty + thing_height:
            print('y crossover')

            if x > thing_startx and x < thing_startx + thing_width or x + car_width > \
                    thing_startx and x + car_width < thing_startx + thing_width:
                print('x crossover')
                crash()

        pygame.display.update()
        clock.tick(60)


game_intro()
game_loop()
pygame.quit()

quit()
