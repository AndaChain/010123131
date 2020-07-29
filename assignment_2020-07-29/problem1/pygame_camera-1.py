###################################################################
# File: pygame_camera-1.py
# Date: 2020-07-30
###################################################################
import pygame
import pygame.camera

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
        pygame.draw.rect( surface, (120,0,120) ,self.pos, 1)
        surface.blit( surface, self.pos, self.pos)

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

W, H = 10, 10
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
    for pos in list_rect:
        pos.draw()

    # draw camera on the screen
    if(len(theCamera) > 0):
        for pos in theCamera:
            surface.blit( img, pos.pos, pos.pos )

    # take position input from mouse
    if(event.type == pygame.MOUSEBUTTONUP):
        if(event.button == 1):
            for pos in list_rect:
                pos_click = pygame.mouse.get_pos()
                if(  (pos.left < pos_click[0] < pos.left+pos.rw) and (pos.top < pos_click[1] < pos.top+pos.rh)  ):
                    # append which position of rectangle to show camera
                    if(pos not in theCamera):
                        print("Pop!!")
                        theCamera.append(pos)

                    #list_rect.remove(pos) #<-- if you want grid on the screen open this code 


    screen.blit( surface, (0,0) )
    pygame.display.update()
    
pygame.quit()
###################################################################
