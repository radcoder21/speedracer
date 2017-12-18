import pygame, time, random

pygame.init()

display_width = 800
display_height = 600

white = (255, 255, 255)
black = (0,0,0)

red = (200, 0, 0)
green = (0, 200, 0)

bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

block_color = (53, 115, 255)

car_width = 89
gameDisplay = pygame.display.set_mode([display_width, display_height])
pygame.display.set_caption('Dodger Pro')
clock = pygame.time.Clock()

pause = False

carImg = pygame.image.load('Car.png')

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text, (0, 0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, block_color, [thingx, thingy, thingw, thingh])

def car(x, y):
    gameDisplay.blit(carImg, (x, y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (display_width/2), (display_height/2)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

def crash():
    message_display('You Crashed')

def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), y + (h / 2))
    gameDisplay.blit(textSurf, textRect)

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            gameDisplay.fill(white)
            largeText = pygame.font.Font('freesansbold.ttf', 115)
            TextSurf, TextRect = text_objects("Car Game", largeText)
            TextRect.center = (display_width / 2), (display_height / 2)
            gameDisplay.blit(TextSurf, TextRect)

            button("GO!!!", 150, 450, 100, 50, green, bright_green, game_loop)
            button("QUIT!!!", 550, 450, 100, 50, red, bright_red, quit)


            pygame.display.update()
            clock.tick(15)

def unpause():
    global pause
    pause = False

def paused():
    global pause
    pause = True

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            #gameDisplay.fill(white)
            largeText = pygame.font.Font('freesansbold.ttf', 115)
            TextSurf, TextRect = text_objects("Paused", largeText)
            TextRect.center = (display_width / 2), (display_height / 2)
            gameDisplay.blit(TextSurf, TextRect)

            button("Continue", 150, 450, 100, 50, green, bright_green, unpause)
            button("QUIT!!!", 550, 450, 100, 50, red, bright_red, quit)


            pygame.display.update()


def game_loop():
    global pause

    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    thing_startx = random.randrange(0, (display_width - car_width))
    thing_startx2 = random.randrange(0, (display_width - car_width))
    thing_starty = -600
    thing_starty2 = -600
    thing_speed = 7
    thing_speed2 = 7
    thing_width = 100
    thing_width2 = 100
    thing_height = 100
    thing_height2 = 100

    dodged = 0

    gameexit = False

    while not gameexit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -10
                if event.key == pygame.K_RIGHT:
                    x_change = 10
                if event.key == pygame.K_p:
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

##Logic
        x += x_change

        gameDisplay.fill(white)

        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
        things(thing_startx2, thing_starty2, thing_width2, thing_height2, block_color)
        thing_starty += thing_speed
        thing_starty2 += thing_speed

        car(x, y)
        things_dodged(dodged)


        if x > display_width - car_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, (display_width - car_width))
            dodged += 1

            thing_speed += 1
            #thing_width += (dodged * 1.2)

        if y < thing_starty+thing_height:
            print('y crossover')

            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                print('x crossover')
                crash()

        if thing_starty2 > display_height:
            thing_starty2 = 0 - thing_height2
            thing_startx2 = random.randrange(0, (display_width - car_width))
            dodged += 1

            thing_speed += 1
            #thing_width += (dodged * 1.2)

        if y < thing_starty2+thing_height2:
            print('y crossover')

            if x > thing_startx2 and x < thing_startx2 + thing_width2 or x + car_width > thing_startx2 and x + car_width < thing_startx2 + thing_width2:
                print('x crossover')
                crash()


        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()
