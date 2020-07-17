"""
###########################################################################################################
Assignment II ส่งวันที่ 17 ก.ค. 2563
ชื่อ: อันดา พัฒนชู
รหัสนักศึกษา: 6201012620279
###########################################################################################################
"""

#note this Python script requires PyGame.
import pygame 
from random import randint
import math

#initialize PyGame
pygame.init()

#show PyGame version
print( 'This code using pygame {}.'.format( pygame.version.ver ) ) 

#set window caption
pygame.display.set_caption('Who is Bigger!!!') 

#Set up the drawing window (800 x 600 pixels)
scr_w, scr_h = 800, 600
screen  = pygame.display.set_mode((scr_w, scr_h))

#array storage circle
storage = []

#array storage circle for using in another function
storage_for_real = []

#array storage Largest circle for using in another function
theLargest = []

#for index in list storage
i = 0

#Clock tick for generate display
clock = pygame.time.Clock()

#Numbers of circle on the screen AND fps for this game.
N = 50
fps = 100

screen.fill((255,255,255))

class Circle:
    def __init__(self,scr_w,scr_h):
        #implement variable initialize of circle
        self.scr_w, self.scr_h = scr_w, scr_h
        self.r = randint(10,20)
        self.x, self.y = randint(self.r,scr_w-self.r), randint(self.r,scr_h-self.r)
        self.colour = (randint(0,255), randint(0,255), randint(0,255))

        #using right, left, bottom and top for check condition to collision
        self.right, self.left = self.x + self.r, self.x - self.r
        self.bottom, self.top = self.y + self.r, self.y - self.r

        #speed of the circle implement by random speed
        self.speed = [randint(1,2),randint(1,2)]
    def Make(self):
        # draw a circle
        pygame.draw.circle(  screen, self.colour, (self.x,self.y), self.r  )
        # update the screen display
        pygame.display.update()
            
    def Disappear(self):
        #Disappear a circle
        pygame.draw.circle(  screen, (255,255,255), (int(self.x),int(self.y)), self.r  )
        pygame.display.update()
        print(self.x,self.y,self.r)
            
        self.colour = (255,255,255)
        
    def Collision(self, storage):
        
        #Increase all initialize values of circle for move to position depends on what values is.
        self.x += self.speed[0]
        self.y += self.speed[1]

        self.right += self.speed[0]
        self.left += self.speed[0]

        self.bottom += self.speed[1]
        self.top += self.speed[1]

        #checking circle that hit the frame or not
        if(self.right >= self.scr_w  or  self.left <= 0):
            self.speed[0] *= -1
        elif(self.bottom >= self.scr_h  or  self.top <= 0):
            self.speed[1] *= -1
        
        #checking circle that hit the orther circle or not
        for orther in storage:
            if( self != orther):
                if int(math.hypot(  self.x - orther.x, self.y - orther.y)  ) <= self.r + orther.r:
                    C1Speed = math.sqrt((self.speed[0])**2 + (self.speed[1])**2)
                    XDiff = -(self.x-orther.x)
                    YDiff = -(self.y-orther.y)

                    #sinario of x and y can make speed and angle change
                    if XDiff > 0:
                        if YDiff > 0:
                            Angle = math.degrees(math.atan(YDiff/XDiff))
                            self.speed[0] = -C1Speed*math.cos(math.radians(Angle))
                            self.speed[1] = -C1Speed*math.sin(math.radians(Angle))
                        elif YDiff < 0:
                            Angle = math.degrees(math.atan(YDiff/XDiff))
                            self.speed[0] = -C1Speed*math.cos(math.radians(Angle))
                            self.speed[1] = -C1Speed*math.sin(math.radians(Angle))
                    elif XDiff < 0:
                        if YDiff > 0:
                            Angle = 180 + math.degrees(math.atan(YDiff/XDiff))
                            self.speed[0] = -C1Speed*math.cos(math.radians(Angle))
                            self.speed[1] = -C1Speed*math.sin(math.radians(Angle))
                        elif YDiff < 0:
                            Angle = -180 + math.degrees(math.atan(YDiff/XDiff))
                            self.speed[0] = -C1Speed*math.cos(math.radians(Angle))
                            self.speed[1] = -C1Speed*math.sin(math.radians(Angle))
                    elif YDiff == 0:
                        if YDiff > 0:
                            Angle = -90
                        else:
                            Angle = 90
                        self.speed[0] = C1Speed*math.cos(math.radians(Angle))
                        self.speed[1] = C1Speed*math.sin(math.radians(Angle))
                    elif YDiff == 0:
                        if XDiff < 0:
                            Angle = -90
                        else:
                            Angle = 180
                        self.speed[0] = C1Speed*math.cos(math.radians(Angle))
                        self.speed[1] = C1Speed*math.sin(math.radians(Angle))

        pygame.draw.circle( screen, self.colour, (int(self.x), int(self.y)), self.r )


#find largest radius of circle
def largest(storage):
    n = 0
    ma = storage[n].r
    for i in range(len(storage)-1):
        if(ma < storage[i+1].r):
            ma =  storage[i+1].r
        else:
            ma = ma
    return ma

#Draw the circle
while(N > 0):
    
    storage.append("l")
    storage[i] = Circle(scr_w,scr_h)
    draw = True

    for j in range(len(storage)):
        if i != j:
            #check distance between point to point by equation like this.
            dist = math.sqrt(  (storage[i].x - storage[j].x)**2 + (storage[i].y - storage[j].y)**2  )
            
            #if distance less than A radius + B radius give draw is False it mean circle has overlaped
            #otherwise draw is True
            if(dist < int(storage[i].r+storage[j].r)):
                draw = False

    if draw:
        #storage use only in this loop
        #I will use storage_for_real for after this loop end to access to whole circles on the screen
        storage[j].Make()
        storage_for_real.append(storage[j])
        # i and j is same alway in this if...

        N -= 1
    i += 1

    #print(len(storage_for_real))

#set storage be default array for using in this code
storage = storage_for_real

#section of running program
running = True
while running:
    #quit from program if you click on [X]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #create list of largest circle
    if(len(theLargest) <= 0):
        for i in range(len(storage)):
            if(storage[i].r == largest(storage)):
                theLargest.append(storage[i])


    #for delate the largest circle on the screen
    for j in range(len(theLargest)-1,-1,-1):

        #check output from mouse if is 1 = True, 0 = False 
        if pygame.mouse.get_pressed()[0]:

            #return position of cursor on the screen 
            pos = pygame.mouse.get_pos()

            #check position of cursor on the screen that on the circle yes or not
            #using circle equation for checking position of cursor
            check = (theLargest[j].x-pos[0])**2 + (theLargest[j].y-pos[1])**2 <= largest(storage)**2
            
            #check is True it's mean a that circle is largest one
            if(check):
                #call method Disappear() for remove circle by create white circle x, y, r value as same as themself
                #and remove data of object in storage list and theLargest list
                theLargest[j].Disappear()
                storage.remove(theLargest[j])
                theLargest.remove(theLargest[j])

    #fps of this game is here.
    clock.tick(fps)

    #loop for collision of circle
    for circle in storage_for_real:
        circle.Collision(storage_for_real)

    #update screen first and then fill the screen by white colour
    pygame.display.update()
    screen.fill((255,255,255))

    
    

print("Good job!!!, Player")
pygame.quit()

"""
###########################################################################################################
ป.ล. เอา Assignment I มาเพิ่ม class circle และแก้การสร้างวงกลมให้ไม่ซ้อนกัน
และทำให้เคลื่อนไหวไปชนกับผนังได้แล้ว มีการดู code ในอินเทอร์เน็ตดังนี้

1) https://www.youtube.com/watch?v=1_H7InPMjaY&t=925s
2) http://www.geometrian.com/programming/projects/index.php?project=Circle%20Collisions

และของคนอื่นอีก 2 ถึง 3 คนแต่ผมจำไม่ได้แล้วรวมถึงได้ระดมความคิดกับเพื่อนจึงได้รับรูปแบบการเขียนจากของเพื่อนมาด้วย
ในหลายๆเรื่องคือ การเขียนให้วงกลมสามารถสร้างได้โดยไม้ซ้อนกัน การทำให้วงกลมมันชนกันไปมา
###########################################################################################################
"""