import threading
import time
import pygame
#-----pygame section-----
pygame.init()
pygame.display.set_caption( "Mandelbrot" )
scr_w, scr_h = 800, 600
screen = pygame.display.set_mode( (scr_w, scr_h) )
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

class draw_mandelbrot:
    def __init__(self):
        #-----set scale & offset of Mandelbrot visual-----
        self.scale = 0.006
        self.offset = complex(-0.55,0.0)

    def mandelbrot(self, c, max_iters=100):
        i = 0
        z = complex(0,0)
        while abs(z) <= 2 and i < max_iters:
            z = z*z + c
            i += 1
        
        return i

    def draw(self):
        start = time.time()

        for x in range( scr_w ):
            for y in range( scr_h ):
                re = self.scale*( x-scr_w/2 ) + self.offset.real
                im = self.scale*( y-scr_h/2 ) + self.offset.imag
                c = complex( re, im )

                color = self.mandelbrot(c, 63)
                r = (color << 6) & 0xc0
                g = (color << 4) & 0xc0
                b = (color << 2) & 0xc0
                surface.set_at( (x,y), (255-r,255-g,255-b) )

        print(time.time()-start)

draw = draw_mandelbrot()
draw.draw()

running = True
while running:
    # draw the surface on the screen
    screen.blit( surface, (0,0) )

    # update the display
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False