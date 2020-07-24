"""
#######################################
Assignment I ส่งวันที่ 15 ก.ค. 2563
ชื่อ: อันดา พัฒนชู
รหัสนักศึกษา: 6201012620276
#######################################
"""

#find largest radius of circle
def largest(storage):
    n = 0
    ma = storage[n][2]
    for i in range(len(storage)-1):
        if(ma < storage[i+1][2]):
            ma =  storage[i+1][2]
        else:
            ma = ma
    return ma

#note this Python script requires PyGame.
import pygame 
from random import randint
import math

#initialize PyGame
pygame.init()

#show PyGame version
print( 'Work_3: {}'.format( pygame.version.ver ) ) 


#set window caption
pygame.display.set_caption('Work_3') 

#Set up the drawing window (800 x 600 pixels)
scr_w, scr_h = 800, 600
screen  = pygame.display.set_mode((scr_w, scr_h))

#create a new surface 
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

#array storage center point of circle and radius
storage = []

for a in range(10):
     # randomize an integer value between 10..20 for the radius
    r1 = randint(10,20)

    # randomize a position (x,y)
    x1,y1 = randint(r1,scr_w-r1), randint(r1,scr_h-1)
    #storage value of x, y and r for using
    storage.append([x1,y1,r1])

    # create (RGBA) by random
    R, G, B = randint(0,255), randint(0,255), randint(0,255)
    color = (R,G,B)

    for i in storage:
        if(len(storage) > 1):

            #Equation of distance between point to point
            d = math.sqrt((x1-i[0])**2 + (y1-i[1])**2)

            if(d >= r1+i[2]):
                # draw a circle
                pygame.draw.circle( surface, color, (x1,y1), r1 )
                # fill the screen with the white color
                screen.fill((255,255,255))
                # draw the surface on the screen
                screen.blit(surface, (0,0))
                # update the screen display
                pygame.display.update()
            else:
                break
        else:
            # draw a circle
            pygame.draw.circle( surface, color, (x1,y1), r1 )
            # fill the screen with the white color
            screen.fill((255,255,255))
            # draw the surface on the screen
            screen.blit(surface, (0,0))
            # update the screen display
            pygame.display.update()

#section of running program
running = True

while running:

    #quit from program if you click on [X]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #quit from program if you click on [X]
    theLargest = []
    for i in range(len(storage)):
        if(storage[i][2] == largest(storage)):
            theLargest.append([storage[i][0], storage[i][1], storage[i][2]])


    #for delate the largest circle on the screen
    for j in range(len(theLargest)):

        #check output from mouse if is 1 = True, 0 = False 
        if pygame.mouse.get_pressed()[0]:

            #return position of cursor on the screen 
            pos = pygame.mouse.get_pos()

            #check position of cursor on the screen that on the circle yes or not
            #using circle equation for checking position of cursor
            check = (theLargest[j][0]-pos[0])**2 + (theLargest[j][1]-pos[1])**2 <= largest(storage)**2
            
            if(check):
                # draw a circle
                pygame.draw.circle( surface, (255,255,255), (theLargest[j][0],theLargest[j][1]), theLargest[j][2] )
                screen.blit(surface, (0,0))
                pygame.display.update()

print("Good job!!!, my teacher")
pygame.quit()

"""
#####################################################
ป.ล. เอา demo1 ของอาจารย์เรวัตมาปรับปรุงครับ ขอบคุณครับ
#####################################################
"""
