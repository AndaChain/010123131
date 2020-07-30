###################################################################
# File: pygame_camera-1.py
# Date: 2020-07-30
###################################################################
import pygame
import pygame.camera
import time

pygame.init()
scr_w, scr_h = 640, 480
screen = pygame.display.set_mode( (scr_w,scr_h) )

surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

class Rectangle:
    def __init__(self, left, top, rw, rh):
        self.left = left
        self.top = top
        self.rw = rw
        self.rh = rh
        self.pos = (left, top, rw, rh)

    def draw(self):
        surface.blit( img, (self.left, self.top, self.rw, self.rh), self.pos )
    
    def set_new_pos(self, pos):
        self.left = pos.left
        self.top = pos.top
        self.rw = pos.rw
        self.rh = pos.rh
        return (self.left, self.top, self.rw, self.rh)
        
def open_camera():
    pygame.camera.init()
    list_cameras = pygame.camera.list_cameras()
    
    if(list_cameras):
        # use camera that found in your machine 
        camera = pygame.camera.Camera( list_cameras[0], (scr_w, scr_h), "RGB" )
        return camera
    
    return None

# create list of purple background obj.
list_rect = []
theCamera = []

W, H = 3, 3
rw, rh = scr_w//W, scr_h//H
for w in range(W):
    for h in range(H):
        rect = Rectangle(w*rw, h*rh, rw, rh)
        list_rect.append(rect)

camera = open_camera()
camera.start()

running = True
while(running):
    img = camera.get_image()
    
    # for close program
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False

    # draw purple rectangle
    #for pos in list_rect:
        #pos.draw()

    # draw camera on the screen
    #if(len(theCamera) > 0):
    for pos in list_rect:
        pos.draw()
            
    # take position input from mouse
    if(event.type == pygame.MOUSEBUTTONUP):
        #global pos_start
        global pos_start_rect

        pos_click = pygame.mouse.get_pos()
        if(event.button == 1):
            for pos in list_rect:
                if(  (pos.left < pos_click[0] < pos.left+pos.rw) and (pos.top < pos_click[1] < pos.top+pos.rh)  ):
                    if(pos_start_rect.pos == pos.pos):
                        # append which position of rectangle to show camera
                        #if(pos not in theCamera):
                        print("Pop!!")
                        #theCamera.append(pos)
                    else:
                        #pos_start_rect
                        #pos

                        print((pos_start_rect.left, pos_start_rect.top, pos_start_rect.rw, pos_start_rect.rh),end='')
                        print(pos.pos,"OLD")
                        list_rect.remove(pos_start_rect)
                        list_rect.remove(pos)

                        pos.pos, pos_start_rect.pos = pos_start_rect.pos, pos.pos
                        
                        list_rect.append(pos)
                        list_rect.append(pos_start_rect)
                        print( (pos_start_rect.left, pos_start_rect.top, pos_start_rect.rw, pos_start_rect.rh),end='' )
                        print( (pos.left, pos.top, pos.rw, pos.rh),"NEW")

                    #list_rect.remove(pos) #<-- if you want grid on the screen open this code 
    
    elif(event.type == pygame.MOUSEBUTTONDOWN):
        pos_start = pygame.mouse.get_pos()
        if(event.button == 1):
            for pos in list_rect:
                if(  (pos.left < pos_start[0] < pos.left+pos.rw) and (pos.top < pos_start[1] < pos.top+pos.rh)  ):
                    pos_start_rect = pos
                    #print(pos_start)

    screen.blit( surface, (0,0) )
    pygame.display.update()
    
pygame.quit()
###################################################################