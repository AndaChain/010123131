"""
#######################################
Assignment II demo ส่งวันที่ 17 ก.ค. 2563
ชื่อ: อันดา พัฒนชู
รหัสนักศึกษา: 6201012620276
#######################################
"""

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

"""#create a new surface 
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )"""

#array storage center point of circle and radius
storage = []
storage_for_real = []

#Numbers of circle on the screen
N = 100

#for index in list storage
i = 0

#Clock tick
clock = pygame.time.Clock()

screen.fill((255,255,255))

class Circle:
    def __init__(self,scr_w,scr_h):
        self.scr_w, self.scr_h = scr_w, scr_h
        self.r = randint(10,20)
        self.x, self.y = randint(self.r,scr_w-self.r), randint(self.r,scr_h-self.r)
        self.colour = (randint(0,255), randint(0,255), randint(0,255))
        self.thickness = 1

        self.right, self.left = self.x + self.r, self.x - self.r
        self.bottom, self.top = self.y + self.r, self.y - self.r

        self.speed = [randint(1,2),randint(1,2)]
    def Make(self):
        # draw a circle
        pygame.draw.circle( screen, self.colour, (self.x,self.y), self.r )
        # update the screen display
        pygame.display.update()
            
    def Disappear(self):
        #Disappear a circle
        pygame.draw.circle( screen, (255,255,255), (self.x,self.y), self.r )
        pygame.display.update()
        print(self.x,self.y,self.r)
            
        self.colour = (255,255,255)
        
    def Collision(self, storage):
        self.x += self.speed[0]
        self.y += self.speed[1]

        self.right += self.speed[0]
        self.left += self.speed[0]

        self.bottom += self.speed[1]
        self.top += self.speed[1]

        if(self.right >= self.scr_w  or  self.left <= 0):
            self.speed[0] *= -1
        elif(self.bottom >= self.scr_h  or  self.top <= 0):
            self.speed[1] *= -1

        for orther in storage:
            dist = math.sqrt((orther.x-self.x)**2 + (orther.y-self.y)**2)
            if (dist == int(orther.r+self.r)):

                self.speed[0] *= -1
                self.speed[1] *= -1
                orther.speed[0] *= -1
                orther.speed[1] *= -1
        
        pygame.draw.circle( screen, self.colour, (self.x,self.y), self.r )


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
#move circle
def move_circle(circle,storage) :

        circle.x += circle.speed[0]
        circle.y += circle.speed[1]

        circle.right += circle.speed[0]
        circle.left += circle.speed[0]

        circle.bottom += circle.speed[1]
        circle.top += circle.speed[1]
        
        if(circle.right >= circle.scr_w  or  circle.left <= 0):
            circle.speed[0] *= -1
        elif(circle.bottom >= circle.scr_h  or  circle.top <= 0):
            circle.speed[1] *= -1

        for orther in storage:
            dist = math.sqrt((orther.x-circle.x)**2 + (orther.y-circle.y)**2)
            if (dist == int(orther.r+circle.r)):
                circle.speed[0] *= -1
                circle.speed[1] *= -1
                orther.speed[0] *= -1
                orther.speed[1] *= -1
        
        pygame.draw.circle( screen, circle.colour, (circle.x,circle.y), circle.r )

#Draw the circle
while(N > 0):
    
    storage.append("l")
    storage[i] = Circle(scr_w,scr_h)
    draw = True

    for j in range(len(storage)):
        if i != j:
            dist = math.sqrt(  (storage[i].x - storage[j].x)**2 + (storage[i].y - storage[j].y)**2  )
            if(dist < int(storage[i].r+storage[j].r)):
                draw = False

    if draw:
        storage[i].Make()
        storage_for_real.append(storage[i])
        N -= 1
    i += 1

#section of running program
running = True

while running:
    storage = storage_for_real
    clock.tick(1000)

    #quit from program if you click on [X]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #create list of largest circle
    theLargest = []
    for i in range(len(storage)):
        if(storage[i].r == largest(storage)):
            theLargest.append(storage[i])


    #for delate the largest circle on the screen
    for j in range(len(theLargest)):

        #check output from mouse if is 1 = True, 0 = False 
        if pygame.mouse.get_pressed()[0]:

            #return position of cursor on the screen 
            pos = pygame.mouse.get_pos()

            #check position of cursor on the screen that on the circle yes or not
            #using circle equation for checking position of cursor
            check = (theLargest[j].x-pos[0])**2 + (theLargest[j].y-pos[1])**2 <= largest(storage)**2
            
            if(check):
                theLargest[j].Disappear()

    for circle in storage_for_real:
        move_circle(circle,storage_for_real)

    pygame.display.update()
    screen.fill((255,255,255))

    
    

print("Good job!!!, my teacher")
pygame.quit()
"""print(len(theLargest))
for i in storage:
    print(i.x,i.y,i.r)
    print(storage)"""

"""
#####################################################
ป.ล. เอา Assignment I มาเพิ่ม class circle และแก้การสร้างวงกลมให้ไม่ซ้อนกัน
และทำให้เคลื่อนไหวไปชนกับผนังได้แล้ว มีการดู code ในอินเทอร์เน็ตดังนี้
https://www.youtube.com/watch?v=1_H7InPMjaY&t=925s
และของคนอื่นอีก 2 ถึง 3 คนแต่ผมจำไม่ได้แล้ว

ตัว demo นี้ยังไม่สมบูรณ์ผมจะส่งในเย็นวันนี้ครับ
#####################################################
"""
