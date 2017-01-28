#Monique Contreras
#CPSC 386 Project 5
import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600
gameDisplay= pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('Tanker Turrets')

white = (255,255,255)
black= (0,0,0)
red= (200,0,0)
lred=(255,0,0)
orange=(255,69,0)
yellow=(200,200,0)
lyellow=(255,255,0)
green= (34,177,76)
lgreen= (0,255,0)
blue = (30,144,255)
lblue = (135,206,250)
pink = (255,105,180)
brown= (139,69,19)
purple=(160,32,240)


clock = pygame.time.Clock()

tankWidth = 40
tankHeight = 20

turretWidth = 5
wheelWidth = 5

groundHeight = 35

smallfont = pygame.font.SysFont("comicsansms",25)
medfont = pygame.font.SysFont("comicsansms",50)
largefont = pygame.font.SysFont("comicsansms",85)

def score(score):
    text = smallfont.render("Score: "+ str(score), True, black)
    gameDisplay.blit(text,[0,0])

def text_objects(text, color, size = "small"):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()

def text_button(msg,color,buttonx,buttony, bwidth, bheight, size = "small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = ((buttonx+(bwidth/2)), buttony+(bheight/2))
    gameDisplay.blit(textSurf, textRect)


def message_to_screen(msg, color,y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center=(int(display_width / 2), int(display_height / 2)+y_displace)
    gameDisplay.blit(textSurf, textRect)

def tank(x,y,turPos):
    x = int(x)
    y = int(y)

    turrets = [(x-27,y-2),(x-26,y-5),(x-25,y-8),(x-23,y-12),(x-20,y-14),(x-18,y-15),
               (x-15,y-17),(x-13,y-19),(x-11,y-21)]


    pygame.draw.circle(gameDisplay, black,(x,y),int(tankHeight/2))
    pygame.draw.rect(gameDisplay,black, (x-tankHeight,y,tankWidth,tankHeight))

    pygame.draw.line(gameDisplay,black,(x,y),turrets[turPos],turretWidth)

    pygame.draw.circle(gameDisplay,black,(x-15,y+20),wheelWidth)
    pygame.draw.circle(gameDisplay,black,(x-10,y+20),wheelWidth)
    pygame.draw.circle(gameDisplay,black,(x-5,y+20),wheelWidth)
    pygame.draw.circle(gameDisplay,black,(x,y+20),wheelWidth)
    pygame.draw.circle(gameDisplay,black,(x+5,y+20),wheelWidth)
    pygame.draw.circle(gameDisplay,black,(x+10,y+20),wheelWidth)
    pygame.draw.circle(gameDisplay,black,(x+15,y+20),wheelWidth)
    
    return turrets[turPos]

def enemyTank(x,y,turPos):
    x = int(x)
    y = int(y)

    turrets = [(x+27,y-2),(x+26,y-5),(x+25,y-8),(x+23,y-12),(x+20,y-14),(x+18,y-15),
               (x+15,y-17),(x+13,y-19),(x+11,y-21)]


    pygame.draw.circle(gameDisplay, purple,(x,y),int(tankHeight/2))
    pygame.draw.rect(gameDisplay,purple, (x-tankHeight,y,tankWidth,tankHeight))

    pygame.draw.line(gameDisplay,purple,(x,y),turrets[turPos],turretWidth)

    pygame.draw.circle(gameDisplay,purple,(x-15,y+20),wheelWidth)
    pygame.draw.circle(gameDisplay,purple,(x-10,y+20),wheelWidth)
    pygame.draw.circle(gameDisplay,purple,(x-5,y+20),wheelWidth)
    pygame.draw.circle(gameDisplay,purple,(x,y+20),wheelWidth)
    pygame.draw.circle(gameDisplay,purple,(x+5,y+20),wheelWidth)
    pygame.draw.circle(gameDisplay,purple,(x+10,y+20),wheelWidth)
    pygame.draw.circle(gameDisplay,purple,(x+15,y+20),wheelWidth)
    
    return turrets[turPos]

def menu():
    mmenu = True

    while mmenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        message_to_screen("MENU",red,-100,size = "large")
        message_to_screen("Fire: Spacebar",black,-30)
        message_to_screen("Move Turret: Up and Down Arrows", black,10)
        message_to_screen("Move Tank: Left and Right Arrow",black,50)
        message_to_screen("Power Controls: A and D Keys",black,90)
        message_to_screen("Pause: P",black,130)
        

        button("PLAY",150,500,100,50,green,lgreen,action = "play")
        button("QUIT",550,500,100,50,red,lred,action = "quit")
     

        pygame.display.update()

        clock.tick(15)

def button(text,x,y,width,height,icolor,acolor, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+width > mouse[0] > x and y+height > mouse[1] > y:
        pygame.draw.rect(gameDisplay, acolor, (x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit
            if action == "menu":
                menu()
            if action == "play":
                gameLoop()

    else:
        pygame.draw.rect(gameDisplay, icolor, (x,y,width,height))
    text_button(text,black,x,y,width,height)

def pause():

    pause = True
    message_to_screen("Paused",black,-100,size="large")
    message_to_screen("Press C to continue playing or Q to quit",black,25)
    pygame.display.update()
    
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    pause = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        clock.tick(5)

def block(xlocate,randHeight,blockWidth):

    pygame.draw.rect(gameDisplay,black, [xlocate,(display_height)-randHeight,blockWidth,randHeight])

def explode(x,y,size =50):

    explosion = True

    while explosion:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        startPoint = x,y 

        colorChoice = [red,lred,orange,yellow,lyellow]

        magnitude = 1

        while magnitude < size:
            explodingx = x + random.randrange(-1*magnitude,magnitude)
            explodingy = y + random.randrange(-1*magnitude,magnitude)

            pygame.draw.circle(gameDisplay, colorChoice[random.randrange(0,5)],(explodingx,explodingy),random.randrange(1,5))
            magnitude += 1

            pygame.display.update()
            clock.tick(100)

        explosion = False

def fireGun(xy,tankx,tanky,turPos,tankPower,xlocate,blockWidth,randHeight,enemyTankX,enemyTankY):
    fire = True
    damage = 0
    startingRound = list(xy)

    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.draw.circle(gameDisplay,orange,(startingRound[0],startingRound[1]),5)

        startingRound[0] -= (12-turPos)*2

        #y = x^2 simplest form for arc
        startingRound[1] += int((((startingRound[0]-xy[0])*.015/(tankPower/50))**2)-(turPos+turPos/(12-turPos)))

        if startingRound[1] > display_height-groundHeight:
            hitx = int((startingRound[0]*display_height-groundHeight)/startingRound[1])
            hity = int(display_height-groundHeight)
            if enemyTankX + 10 > hitx > enemyTankX - 10:
                damage = 25
            elif enemyTankX + 15 > hitx > enemyTankX - 15:
                damage = 18
            elif enemyTankX + 25 > hitx > enemyTankX - 25:
                damage = 10
            elif enemyTankX + 35 > hitx > enemyTankX - 35:
                damage = 5
            explode(hitx,hity)
            fire = False

        checkX1 = startingRound[0] <= xlocate + blockWidth
        checkX2 = startingRound[0] >= xlocate 

        checkY1 = startingRound[1] <= display_height
        checkY2 = startingRound[1] >= display_height - randHeight

        if checkX1 and checkX2 and checkY1 and checkY2:
            hitx = int(startingRound[0])
            hity = int(startingRound[1])
            explode(hitx,hity)
            fire = False



        pygame.display.update()
        clock.tick(60)
    return damage

def enemyFireGun(xy,tankx,tanky,turPos,tankPower,xlocate,blockWidth,randHeight,ptankx,ptanky):
    damage = 0
    curPower = 1
    foundPower = False

    while not foundPower:
        curPower += 1
        if curPower >100:
            foundPower = True

        fire = True
        startingRound = list(xy)

        while fire:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            #pygame.draw.circle(gameDisplay,orange,(startingRound[0],startingRound[1]),5)

            startingRound[0] += (12-turPos)*2
      

            #y = x^2 simplest form for arc

            startingRound[1] += int((((startingRound[0]-xy[0])*.015/(curPower/50))**2)-(turPos+turPos/(12-turPos)))

            if startingRound[1] > display_height-groundHeight:
                hitx = int((startingRound[0]*display_height-groundHeight)/startingRound[1])
                hity = int(display_height-groundHeight)
               #explode(hitx,hity)
                if ptankx +15 >hitx >ptankx -15:
                    foundPower = True
                fire = False

            checkX1 = startingRound[0] <= xlocate + blockWidth
            checkX2 = startingRound[0] >= xlocate 

            checkY1 = startingRound[1] <= display_height
            checkY2 = startingRound[1] >= display_height - randHeight

            if checkX1 and checkX2 and checkY1 and checkY2:
                hitx = int(startingRound[0])
                hity = int(startingRound[1])
                #explode(hitx,hity)
                fire = False

    fire = True
    startingRound = list(xy)

    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.draw.circle(gameDisplay,orange,(startingRound[0],startingRound[1]),5)

        startingRound[0] += (12-turPos)*2
      
        tankPower = random.randrange(int(curPower*.9),int(curPower*1.1))

        #y = x^2 simplest form for arc
        startingRound[1] += int((((startingRound[0]-xy[0])*.015/(tankPower/50))**2)-(turPos+turPos/(12-turPos)))

        if startingRound[1] > display_height-groundHeight:
            hitx = int((startingRound[0]*display_height-groundHeight)/startingRound[1])
            hity = int(display_height-groundHeight) 
            if ptankx + 10 > hitx > ptankx - 10:
                damage = 25
            elif ptankx+15 > hitx > ptankx - 15:
                damage = 18
            elif ptankx+25 > hitx > ptankx - 25:
                damage = 10 
            elif ptankx+35 > hitx > ptankx - 35:
                damage = 5
            explode(hitx,hity)
            fire = False

        checkX1 = startingRound[0] <= xlocate + blockWidth
        checkX2 = startingRound[0] >= xlocate 

        checkY1 = startingRound[1] <= display_height
        checkY2 = startingRound[1] >= display_height - randHeight

        if checkX1 and checkX2 and checkY1 and checkY2:
            hitx = int(startingRound[0])
            hity = int(startingRound[1])
            explode(hitx,hity)
            fire = False    
        
            

        pygame.display.update()
        clock.tick(60)
    return damage

def poweredup(amount):
    text = smallfont.render("Power: "+str(amount)+ "%",True,black )
    gameDisplay.blit(text, [display_width/2,0])

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                elif event.key == pygame.K_q:

                    pygame.quit()
                    quit()
        gameDisplay.fill(white)
        message_to_screen("TANKER TURRETS",red,-100,size = "large")
        message_to_screen("Objective: Shoot and destroy",black,-30)
        message_to_screen("the enemy tank until health depletes", black,10)
        message_to_screen("Use turrets to aim and power up", black,50)
        message_to_screen("By Monique Contreras",black,180)
        

        button("PLAY",150,500,100,50,green,lgreen,action = "play")
        button("MENU",350,500,100,50,blue,lblue,action = "menu")
        button("QUIT",550,500,100,50,red,lred,action = "quit")
     

        pygame.display.update()

        clock.tick(15)

def game_over():

    over = True

    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        message_to_screen("GAME OVER",red,-100,size = "large")
        message_to_screen("YOU LOST",black,-30)
        

        button("AGAIN?",150,500,100,50,green,lgreen,action = "play")
        button("MENU",350,500,100,50,blue,lblue,action = "menu")
        button("QUIT",550,500,100,50,red,lred,action = "quit")
     

        pygame.display.update()

        clock.tick(15)
def win():

    win = True

    while win:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        message_to_screen("YOU WIN",red,-100,size = "large")
        message_to_screen("GOOD JOB!!",black,-30)
        

        button("AGAIN?",150,500,100,50,green,lgreen,action = "play")
        button("MENU",350,500,100,50,blue,lblue,action = "menu")
        button("QUIT",550,500,100,50,red,lred,action = "quit")
     

        pygame.display.update()

        clock.tick(15)

def health(playerHealth,enemyHealth):
    if playerHealth > 75:
        playercolor = green
    elif playerHealth >50:
        playercolor = yellow
    else:
        playercolor = red

    if enemyHealth > 75:
        enemycolor = green
    elif enemyHealth > 50:
        enemycolor = yellow
    else:
        enemycolor = red

    pygame.draw.rect(gameDisplay,playercolor,(680,35,playerHealth,25))
    pygame.draw.rect(gameDisplay,enemycolor,(20,35,enemyHealth,25))

def gameLoop():
    gameExit = False
    gameOver = False
    fps = 15

    playerHealth = 100
    enemyHealth = 100

    blockWidth=50

    mainTankX = display_width * .9
    mainTankY = display_height * .9
    tankMove = 0
    curTurPos = 0
    changeTur = 0
     
    enemyTankX = display_width * .1
    enemyTankY = display_height *.9

    gunPower = 50
    power= 0

    xlocate = (display_width/2) + random.randint(-0.1*display_width,.1*display_width)
    randHeight =  random.randrange(display_height*.1,display_height*.6)

    while not gameExit:

        if gameOver == True:
            message_to_screen("Game Over",red,-50,size="large")
            message_to_screen("Press C to play again or Q to exit",black,50)
            pygame.display.update()

            while gameOver == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            gameLoop()
                        elif event.key == pygame.K_q:
                            gameExit = True 
                            gameOver = False

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tankMove=-5
                elif event.key == pygame.K_RIGHT:
                    tankMove=5
                elif event.key == pygame.K_UP:
                    changeTur = 1
                elif event.key == pygame.K_DOWN:
                    changeTur = -1
                elif event.key == pygame.K_p:
                    pause()
                elif event.key == pygame.K_SPACE:
                    damage = fireGun(shoot,mainTankX,mainTankY,curTurPos,gunPower,xlocate,blockWidth,randHeight,enemyTankX,enemyTankY)
                    enemyHealth -= damage
                    
                    movement = ['f','r']
                    moveIndex = random.randrange(0,2)
                    
                    for x in range(random.randrange(0,10)):
                        if display_width*.5 > enemyTankX > display_width*.05:
                            if movement[moveIndex] == "f":
                                enemyTankX += 5
                            elif movement[moveIndex]== "r":
                                enemyTankX -= 5
                            gameDisplay.fill(lblue)
                            health(playerHealth,enemyHealth)
                            shoot = tank(mainTankX,mainTankY, curTurPos)
                            enemyShoot = enemyTank(enemyTankX, enemyTankY, 8)
                            gunPower += power

                            poweredup(gunPower)
       
                            block(xlocate,randHeight,blockWidth)
                            gameDisplay.fill(brown,rect=[0,display_height-groundHeight,display_width,groundHeight])    
                            pygame.display.update()
                                 
                               
                    damage = enemyFireGun(enemyShoot,enemyTankX,enemyTankY,8,50,xlocate,blockWidth,randHeight,mainTankX,mainTankY)
                    playerHealth -= damage

                elif event.key == pygame.K_a:
                    power = -1
                elif event.key == pygame.K_d:
                    power = 1

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame. K_RIGHT:
                    tankMove = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    changeTur = 0
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    power = 0

        mainTankX += tankMove

        curTurPos += changeTur
        
        if curTurPos > 8:
            curTurPos = 8
        elif curTurPos < 0:
            curTurPos = 0

        if mainTankX -(tankWidth/2) < xlocate + blockWidth:
            mainTankX+=5

        gameDisplay.fill(lblue)
        health(playerHealth,enemyHealth)
        shoot = tank(mainTankX,mainTankY, curTurPos)
        enemyShoot = enemyTank(enemyTankX, enemyTankY, 8)
       
        gunPower += power

        if gunPower >100:
            gunPower = 100
        elif gunPower <1:
            gunPower = 1

        poweredup(gunPower)
       
        block(xlocate,randHeight,blockWidth)
        gameDisplay.fill(brown,rect=[0,display_height-groundHeight,display_width,groundHeight])    
        pygame.display.update()
        
        if playerHealth < 1:
            game_over()
        elif enemyHealth < 1:
            win()
        clock.tick(fps)
    pygame.quit()
    quit()
game_intro()
gameLoop()     