###################################################################
# File: pygame_camera-2.py
# Date: 2020-07-31
###################################################################
import pygame
import pygame.camera

pygame.init()

#camera wide & height depends on screen wide & height
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
        pygame.draw.rect( img, (120,0,120) ,pos.pos, 1 )
        surface.blit( img, (self.left, self.top, self.rw, self.rh), self.pos )
        
# function for open camera
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

# create retangle W x H cell
W, H = 5, 5
rw, rh = scr_w//W, scr_h//H
for w in range(W):
    for h in range(H):
        rect = Rectangle(w*rw, h*rh, rw, rh)
        list_rect.append(rect)

# check your machine that has cameras.
camera = open_camera()
if(camera != None):
    camera.start()
elif(camera == None):
    print("I don't know what happen about your camera, please check your camera.")

running = True
while(running):
    # get image screenshot
    img = camera.get_image()
    
    # for close program
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False

    # for draw rectangle
    for pos in list_rect:
        pygame.draw.rect( surface, (120,0,120) ,pos.pos, 1 )

    # draw camera on the screen
    for pos in theCamera:
        pos.draw()
            
    # take position input from mouse
    if(event.type == pygame.MOUSEBUTTONUP):
        global pos_start_rect
        if(event.button == 1):
            for pos in list_rect:
                pos_click = pygame.mouse.get_pos()
                if(  (pos.left < pos_click[0] < pos.left+pos.rw) and (pos.top < pos_click[1] < pos.top+pos.rh)  ):
                    if( pos_start_rect.pos == pos.pos ):
                        # append which position of rectangle to show camera
                        if(pos not in theCamera):
                            print("Pop!!")
                            theCamera.append(pos)
                    else:
                        """I used this code because mouse had remain MOUSEBUTTONUP always
                           so "check" help me solve this problem"""
                        if( check ):
                            # swap the camera
                            pos.pos, pos_start_rect.pos = pos_start_rect.pos, pos.pos
                            check = False 

    elif(event.type == pygame.MOUSEBUTTONDOWN): 
        check = True
        if(event.button == 1):
            for pos in list_rect:
                pos_click = pygame.mouse.get_pos()
                if(  (pos.left < pos_click[0] < pos.left+pos.rw) and (pos.top < pos_click[1] < pos.top+pos.rh)  ):
                    pos_start_rect = pos

    screen.blit( surface, (0,0) )
    pygame.display.update()
    
pygame.quit()
###################################################################