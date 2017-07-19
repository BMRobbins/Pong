# Pong
# By Brian Robbins
import pygame, sys, random, time
from pygame.locals import *

#Constants
WINDOWWIDTH = 1350
WINDOWHEIGHT = 650
FPS = 30

#                 R    G    B
BLACK =         (  0,   0,   0)
WHITE =         (255, 255, 255)
GREEN =         (  0, 204,   0)
RED   =         (255,   0,   0)

UP = 'up'
DOWN = 'down'
SPEED = 10

def load_main_menu_logos():
    global PONGLOGO, SINGLELOGO, MULTILOGO, SINGLELOGOR, MULTILOGOR, MLOGO, SLOGO
    PONGLOGO = pygame.image.load('ponglogo.png')
    SINGLELOGO = pygame.image.load('singleplayerbutton.png')
    MULTILOGO =  pygame.image.load('multiplayerbutton.png')
    SINGLELOGOR = pygame.image.load('singleplayerbuttonR.png')
    MULTILOGOR =  pygame.image.load('multiplayerbuttonR.png')
    MLOGO = MULTILOGO
    SLOGO = SINGLELOGO

def load_main_menu_sound():
    pygame.mixer.music.load('introsong.wav')
    pygame.mixer.music.play(loops = 1000)

def load_end_game_images():
    global PLAYER1WINS, PLAYER2WINS, MAINMENU, MAINMENUR, MainLOGO, QUITBUTTON, QUITBUTTONR, QuitLOGO, GAMEOVERSOUND
    PLAYER1WINS = pygame.image.load('player1wins.png')
    PLAYER2WINS = pygame.image.load('player2wins.png')
    MAINMENU = pygame.image.load('mainmenu.png')
    MAINMENUR = pygame.image.load('mainmenuR.png')
    MainLOGO = MAINMENU
    QUITBUTTON = pygame.image.load('quit.png')
    QUITBUTTONR = pygame.image.load('quitR.png')
    QuitLOGO = QUITBUTTON
    GAMEOVERSOUND = pygame.mixer.Sound('gameover.wav')

def set_up_display():
    global CHOICE, FPSCLOCK,DISPLAYSURF,BALL,GAMESTATE,pause
    CHOICE = None
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    pygame.display.set_caption('Pong')
    BALL = ball()
    GAMESTATE = gamestate()
    pause = False

def select_single_player_or_multiplayer():
    global PLAYER1, CHOICE, PLAYER2
    PLAYER1 = Paddle(10,GREEN)
    if CHOICE == 'singleplayer':
            PLAYER2 = ComPaddle((WINDOWWIDTH - 10) - 15, GREEN)

    elif CHOICE == 'multiplayer':
        PLAYER2 = Paddle((WINDOWWIDTH - 10) - 15, GREEN)

def handle_game_events():
    global FPSCLOCK, DISPLAYSURF, PLAYER1, PLAYER2, BALL, GAMESTATE, PONGLOGO, SINGLELOGO,MULTILOGO, SINGLELOGOR,MULTILOGOR,\
           MLOGO, SLOGO, MainMenuMusic,CHOICE, PLAYER1WINS, PLAYER2WINS, MAINMENU, MAINMENUR, QUITBUTTON, QUITBUTTONR, MainLOGO, QuitLOGO, GAMEOVERSOUND, pause

    while CHOICE == 'multiplayer' or CHOICE == 'singleplayer':
        
        if pause:
            time.sleep(1)
        drawboard()
        for event in pygame.event.get():
            if event.type == QUIT or event.type == K_ESCAPE:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                if event.key == K_w:
                    PLAYER1.set_speed(SPEED)
                    PLAYER1.set_move(UP)

                elif event.key == K_s:
                    PLAYER1.set_speed(SPEED)
                    PLAYER1.set_move(DOWN)

                elif event.key == K_UP:
                    PLAYER2.set_speed(SPEED)
                    PLAYER2.set_move(UP)

                elif event.key == K_DOWN:
                    PLAYER2.set_speed(SPEED)
                    PLAYER2.set_move(DOWN)

                elif event.key == K_p:
                    playerPause = True
                    pauseButton = pygame.image.load('pause.png')
                    DISPLAYSURF.blit(pauseButton,((WINDOWWIDTH / 2) - 50, (WINDOWHEIGHT / 2) - 50))
                    pygame.display.update()
                    while playerPause:
                        for event in pygame.event.get():
                            if event.type == KEYDOWN:
                                if event.key == K_p:
                                    playerPause = False
                                    
                            elif event.type == QUIT or event.type == K_ESCAPE:
                                pygame.quit()
                                sys.exit()
                            
            elif event.type == KEYUP:
                if event.key == K_w:
                    PLAYER1.set_speed(0)
                    PLAYER1.set_move(UP)

                elif event.key == K_s:
                    PLAYER1.set_speed(0)
                    PLAYER1.set_move(DOWN)

                elif event.key == K_UP:
                    if CHOICE == 'multiplayer':
                        PLAYER2.set_speed(0)
                        PLAYER2.set_move(UP)

                elif event.key == K_DOWN:
                    if CHOICE == 'multiplayer':
                        PLAYER2.set_speed(0)
                        PLAYER2.set_move(DOWN)
                    
        PLAYER1.update()
        PLAYER2.update()
        BALL.update()
        pause = checkforgoal()
        CHOICE = check_for_game_over()
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        
def main():
    global FPSCLOCK, DISPLAYSURF, PLAYER1, PLAYER2, BALL, GAMESTATE, PONGLOGO, SINGLELOGO,MULTILOGO, SINGLELOGOR,MULTILOGOR,\
           MLOGO, SLOGO, MainMenuMusic,CHOICE, PLAYER1WINS, PLAYER2WINS, MAINMENU, MAINMENUR, QUITBUTTON, QUITBUTTONR, MainLOGO, QuitLOGO, GAMEOVERSOUND, pause
    

    pygame.init()

    #load main menu images and sound for main menu
    load_main_menu_logos()
    load_main_menu_sound()

    #EndGame Logos and sound
    load_end_game_images()   
    
    #Set up display
    set_up_display()
    
    #IntroScreen
    while CHOICE == None:
        draw_main_menu()

    select_single_player_or_multiplayer()
        
    #actual game
    handle_game_events()

    #check for end of game
    check_for_end_of_game()

def check_for_end_of_game():      
    global GAMEOVERSOUND, CHOICE
    GAMEOVERSOUND.play()
    while CHOICE == 'PLAYER1'or CHOICE =='PLAYER2':
        end_game_menu()

def end_game_menu():
    global MainLOGO, QuitLOGO, CHOICE
    DISPLAYSURF.fill(BLACK)
    if CHOICE == 'PLAYER1':
        winner = PLAYER1WINS
    elif CHOICE =='PLAYER2':
        winner = PLAYER2WINS
    DISPLAYSURF.blit(winner, ((WINDOWWIDTH / 2) - 450 , (WINDOWHEIGHT / 2) - 200))


    for event in pygame.event.get():
            if event.type == QUIT or event.type == K_ESCAPE:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEMOTION:
                cord = event.pos
                if cord[0] >= 513 and cord[0] <= 820 and cord[1] >= 340 and cord[1] <= 364:
                    if MainLOGO != MAINMENUR:
                        buttonclick =  pygame.mixer.Sound('laser.wav')
                        buttonclick.play()
                    MainLOGO = MAINMENUR
                   
                else:
                    MainLOGO = MAINMENU


                if cord[0] >= 589 and cord[0] <= 699 and cord[1] >= 439 and cord[1] <= 460:
                    if QuitLOGO != QUITBUTTONR:
                        buttonclick =  pygame.mixer.Sound('laser.wav')
                        buttonclick.play()
                    QuitLOGO = QUITBUTTONR

                else:
                    QuitLOGO = QUITBUTTON
            
            if event.type == MOUSEBUTTONUP:
                cord = event.pos
                if cord[0] >= 513 and cord[0] <= 820 and cord[1] >= 340 and cord[1] <= 364:
                    main()
                   
                elif cord[0] >= 589 and cord[0] <= 669 and cord[1] >= 439 and cord[1] <= 460:
                    pygame.quit()
                    sys.exit()
                    

                
    
    DISPLAYSURF.blit(MainLOGO, ((WINDOWWIDTH / 2) - 166, (WINDOWHEIGHT / 2)))
    DISPLAYSURF.blit(QuitLOGO, ((WINDOWWIDTH / 2) - 181, (WINDOWHEIGHT / 2) + 100))
       
    pygame.display.update()
    FPSCLOCK.tick(FPS)

def check_for_game_over():
    if GAMESTATE.get_score()[0] >= 7:
        return 'PLAYER1'
    elif GAMESTATE.get_score()[1] >=7:
        return 'PLAYER2'
    else:
        return CHOICE
        
    
def draw_main_menu():
    global MLOGO, SLOGO, MainMenuMusic, CHOICE
    
    DISPLAYSURF.fill(BLACK)
    DISPLAYSURF.blit(PONGLOGO, ((WINDOWWIDTH / 2) - 316 , (WINDOWHEIGHT / 2) - 200))
    

    for event in pygame.event.get():
        if event.type == QUIT or event.type == K_ESCAPE:
            pygame.quit()
            sys.exit()
            
        elif event.type == MOUSEMOTION:
            cord = event.pos
            if cord[0] >= 462 and cord[0] <= 888 and cord[1] >= 447 and cord[1] <= 472:
                if SLOGO != SINGLELOGOR:
                    buttonclick =  pygame.mixer.Sound('laser.wav')
                    buttonclick.play()
                SLOGO = SINGLELOGOR 

            else:
                SLOGO = SINGLELOGO


            if cord[0] >= 495 and cord[0] <= 866 and cord[1] >= 540 and cord[1] <= 565:
                if MLOGO != MULTILOGOR:
                    buttonclick =  pygame.mixer.Sound('laser.wav')
                    buttonclick.play()
                MLOGO = MULTILOGOR

            else:
                MLOGO = MULTILOGO

        elif event.type == MOUSEBUTTONUP:
            cord = event.pos
            if cord[0] >= 462 and cord[0] <= 888 and cord[1] >= 447 and cord[1] <= 472:
                CHOICE = 'singleplayer'


            elif cord[0] >= 495 and cord[0] <= 866 and cord[1] >= 540 and cord[1] <= 565:
                CHOICE = 'multiplayer'
                    

            else:
                CHOICE = None

    DISPLAYSURF.blit(SLOGO, ((WINDOWWIDTH / 2) - 216, (WINDOWHEIGHT / 2) + 100))
    DISPLAYSURF.blit(MLOGO, ((WINDOWWIDTH / 2) - 181, (WINDOWHEIGHT / 2) + 200))
       
    pygame.display.update()
    FPSCLOCK.tick(FPS)
    
def checkforgoal():
    if BALL.get_ball_x() < 0:
        BALL.reset()
        PLAYER1.reset()
        PLAYER2.reset()
        GAMESTATE.inc_p2()
        return True
    
        
        
    elif BALL.get_ball_x() >= WINDOWWIDTH:
        BALL.reset()
        PLAYER1.reset()
        PLAYER2.reset()
        GAMESTATE.inc_p1()
        return True
    return False

        
def drawboard():
    DISPLAYSURF.fill(BLACK)
    scoreboard()
    PLAYER1.redraw()
    PLAYER2.redraw()
    BALL.redraw()

def scoreboard():
    pygame.draw.line(DISPLAYSURF, GREEN,(0,50),(WINDOWWIDTH,50), 2)
    pygame.draw.line(DISPLAYSURF, GREEN, (WINDOWWIDTH / 2, 0), (WINDOWWIDTH/2, 50), 2)

    fontobj = pygame.font.Font('freesansbold.ttf', 32)
    textSurfaceObj1 = fontobj.render('PLAYER1: '+ str(GAMESTATE.get_score()[0]),True,GREEN, BLACK)
    textSurfaceObj2 = fontobj.render('PLAYER2: '+ str(GAMESTATE.get_score()[1]),True,GREEN, BLACK)
    textRectObj1 = textSurfaceObj1.get_rect()
    textRectObj2 = textSurfaceObj2.get_rect()
    textRectObj1.center = ((WINDOWWIDTH /2) /2,25)
    textRectObj2.center = ((WINDOWWIDTH /2) / 2 + WINDOWWIDTH / 2, 25)

    DISPLAYSURF.blit(textSurfaceObj1, textRectObj1)
    DISPLAYSURF.blit(textSurfaceObj2, textRectObj2)
                
    
    
def randomdirection():
    dlist = [-1,1]
    x  = random.choice(dlist)
    dlist.pop(x)
    y = random.choice(dlist)
    return (x,y)
#======================= Classes ==============================================

#Paddle
    
class Paddle():
    def __init__(self, x, color):
        self.origx, self.origy = x , (WINDOWHEIGHT / 2) - 20
        self.x = x
        self.y = (WINDOWHEIGHT / 2) - 20 

        self.color = color
        self.speed = 10
        self.move = None
        self.rect = pygame.draw.rect(DISPLAYSURF,self.color,(self.x, self.y, 15, 100))

    def redraw(self):
        self.rect = pygame.draw.rect(DISPLAYSURF,self.color,(self.x, self.y, 15, 100))

    def update(self):
        if self.move == 'up':
            if self.y >= 0:
                self.y -= self.speed
        elif self.move == 'down':
            if self.y <= WINDOWHEIGHT- 100:
                self.y += self.speed
            
    def set_speed(self,speed):
        self.speed = speed

    def set_move(self,move):
        self.move = move

    def reset(self):
        self.x, self.y = self.origx, self.origy

#Computer Paddle
class ComPaddle():
    def __init__(self, x, color):
        self.origx, self.origy = x , (WINDOWHEIGHT / 2) - 20
        self.x = x
        self.y = (WINDOWHEIGHT / 2) - 20 

        self.color = color
        self.speed = 10
        self.move = None
        self.rect = pygame.draw.rect(DISPLAYSURF,self.color,(self.x, self.y, 15, 100))

    def redraw(self):
        self.rect = pygame.draw.rect(DISPLAYSURF,self.color,(self.x, self.y, 15, 100))

    def update(self):
        cordy = BALL.get_ball_y()
        cordx = BALL.get_ball_x()
        cordxd = BALL.get_ball_xd()
        if cordxd > 0 and cordx > 200:
            if cordy < self.y + 40:
                if self.y >= 0:
                    self.y -= self.speed           
            elif cordy > self.y - 40:
                if self.y <= WINDOWHEIGHT- 100:
                    self.y += self.speed
        elif (WINDOWHEIGHT/ 2)  < self.y:
            self.y -= self.speed
        
        elif (WINDOWHEIGHT/ 2)  > self.y:
            self.y += self.speed
            
    def set_speed(self,speed):
        self.speed = speed

    def set_move(self,move):
        self.move = move

    def reset(self):
        self.x, self.y = self.origx, self.origy
        

# ball

class ball():
    def __init__(self):
        self.radius = 10
        self.speed = 5
        self.origx, self.origy = int(WINDOWWIDTH / 2), int(WINDOWHEIGHT /2)
        self.x, self.y =  int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2)
        self.xd ,self.yd = randomdirection()
        self.circle = pygame.draw.circle(DISPLAYSURF, RED, (self.x, self.y ), self.radius, 0)
        self.buffer = 25
        self.counter = 0
        self.sound1 = pygame.mixer.Sound('bliphigh.wav')
        self.sound2 = pygame.mixer.Sound('bliplow.wav')
        
    def redraw(self):
        self.circle = pygame.draw.circle(DISPLAYSURF, RED, (self.x, self.y ), self.radius, 0)
        
    def update(self):
        self.x += self.xd * self.speed
        self.y += self.yd * self.speed
        if self.y <= 0:
            self.yd = self.yd * -1
        elif self.y >= WINDOWHEIGHT:
            self.yd = self.yd * -1
                
        if PLAYER1.rect.collidepoint(self.circle.center):
            self.sound1.play()
            self.increase_speed()
            topRect = PLAYER1.rect.top
            circCenter = self.circle.centery
            if circCenter - topRect < 20:
                self.xd = 1
                self.yd = -2
                self.x += self.buffer

            elif circCenter - topRect < 40:
                self.xd = 1
                self.yd = -1
                self.x += self.buffer

            elif circCenter - topRect <= 60:
                self.xd = 1
                self.yd = 0
                self.x += self.buffer

            elif circCenter - topRect < 80:
                self.xd = 1
                self.yd = 1
                self.x += self.buffer

            elif circCenter - topRect <= 100:
                self.xd = 1
                self.yd = 2
                self.x += self.buffer

            self.counter +=1

            if self.counter >= 2:
                self.counter = 0
                if self.speed < 15:
                    self.buffer += 20
            

        elif PLAYER2.rect.collidepoint(self.circle.center):
            self.sound2.play()
            self.increase_speed()
            topRect = PLAYER2.rect.top
            circCenter = self.circle.centery
            if circCenter - topRect < 20:
                self.xd = -1
                self.yd = -2
                self.x += self.buffer * -1

            elif circCenter - topRect < 40:
                self.xd = -1
                self.yd = -1
                self.x += self.buffer * -1

            elif circCenter - topRect <= 60:
                self.xd = -1
                self.yd = 0
                self.x += self.buffer * -1

            elif circCenter - topRect < 80:
                self.xd = -1
                self.yd = 1
                self.x += self.buffer * -1

            elif circCenter - topRect <= 100:
                self.xd = -1
                self.yd = -2
                self.x += self.buffer * -1

            self.counter +=1

            if self.counter >= 2:
                self.counter = 0
                if self.speed < 15:
                    self.buffer += 20

            

    def increase_speed(self):
        if self.speed < 15:
            self.speed += 1

    def reset(self):
        self.x, self.y = self.origx, self.origy
        self.xd ,self.yd = randomdirection()
        self.speed = 5
        self.buffer = 25
        self.counter = 0

    def get_ball_x(self):
        return self.x

    def get_ball_y(self):
        return self.y
    def get_ball_xd(self):
        return self.xd
        
        
        

#gamestate
class gamestate():
    def __init__(self):
        self.player1 = 0
        self.player2 = 0

    def inc_p1(self):
        self.player1 += 1

    def inc_p2(self):
        self.player2 += 1
                                        
    def get_score(self):
        return (self.player1, self.player2)
                                        
            
if __name__ == '__main__':
    main()
