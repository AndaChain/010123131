import pygame

import datetime

import time

import math


pygame.init()

screen=pygame.display.set_mode([660,660])
pygame.display.set_caption("Analog Clock")
screen.fill([255,255,255])
#bg=pygame.image.load("C:/Users/s6201012620279/Software development/100763/picture/picture2.jpg")
#screen.blit(bg,[0,0])

radius_s=220
radius_m=220
radius_h=180

hour_position=[]
minute_position=[]
seconds_position=[]

def get_second():

    current_sec= datetime.datetime.now().strftime("%S")
    return int(current_sec)

def get_minute():

    current_min= datetime.datetime.now().strftime("%M")
    return int(current_min)

def get_hour():

    current_h= datetime.datetime.now().strftime("%I")       
    return int(current_h)


def get_am_or_pm():

    get_am_or_pm= datetime.datetime.now().strftime("%p")
    return get_am_or_pm

def run():
    running = True
    while running:

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running = False
                pygame.quit()

        s=get_second()
        position_s=[math.cos(math.radians(s*6+270))*radius_s+330,math.sin(math.radians(s*6+270))*radius_s+330]
        m=get_minute()
        position_m=[math.cos(math.radians(m*6+270))*radius_m+330,math.sin(math.radians(m*6+270))*radius_m+330]
        h=get_hour()
        position_h=[math.cos(math.radians(h*6+270))*radius_h+330,math.sin(math.radians(h*6+270))*radius_h+330]

        screen.fill([0,0,0]) 

        pygame.draw.circle(screen,[255,255,0],(330,330),300,0)
        
        pygame.draw.line(screen,[0,0,0],(330,330),position_h,20)
        pygame.draw.line(screen,[0,0,0],(330,330),position_m,10)
        pygame.draw.line(screen,[255,0,0],(330,330),position_s,10)

        pygame.draw.circle(screen,[255,0,0],(330,330),15,0)
        font=pygame.font.Font(None,25)
        time_stamp=font.render(str(h)+":"+str(m)+":"+str(s)+" "+get_am_or_pm(),1,(0,255,255))
        pygame.draw.rect(screen,[0,0,0],(10,10,110,40))
        screen.blit(time_stamp,[20,20])

        pygame.display.flip()

        time.sleep(1)
    
run()

#edit from https://www.youtube.com/watch?v=k_JTkGIUtcU, https://github.com/sayed43/analog_clock_pygame
