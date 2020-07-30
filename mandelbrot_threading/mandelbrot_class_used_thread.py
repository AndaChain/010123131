from threading import Thread
from threading import Lock
from threading import Semaphore

import time
import pygame
#-----pygame section-----
pygame.init()
pygame.display.set_caption( "Mandelbrot" )
scr_w, scr_h = 500, 500
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

    def draw(self, id):
        for x in range(id*w_th, (id+1)*w_th):
            for y in range( scr_h ):
                re = self.scale*( x-scr_w/2 ) + self.offset.real
                im = self.scale*( y-scr_h/2 ) + self.offset.imag
                c = complex( re, im )

                color = self.mandelbrot(c, 63)
                r = (color << 6) & 0xc0
                g = (color << 4) & 0xc0
                b = (color << 2) & 0xc0
                surface.set_at( (x,y), (255-r,255-g,255-b) )

class MyThread(Thread):
    def __init__(self, id, sem):
        Thread.__init__(self)
        self.id = id
        self.sem = sem
    
    def run(self):
        if(sem.acquire()):
            draw = draw_mandelbrot()
            draw.draw(self.id)

        end.append(time.time()-start)

# set number of thread for running program & area
N = 100
w_th = scr_w//N #+ scr_w%N
#h_th = scr_h//N + scr_h%N

# lock thread
lock = Lock()

# list of semaphore **for lock thread**
list_sem = [Semaphore(0) for i in range(N)]

# list of thread
list_threads = []

# create list of thread
for id in range(N):
    sem = list_sem[id]
    list_threads.append( MyThread(id, sem) )

start = time.time()
end = []
# time to start threads!!! oh yessss!!
for thread in list_threads:
    thread.start()

running = True
while running:
    # release semaphore
    for thread in list_sem:
        thread.release()
        
    # draw the surface on the screen
    screen.blit( surface, (0,0) )

    # update the display
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# after you close the program all thread is join
for thread in list_threads:
    if(  thread.is_alive()  ):
        thread.join()

print("using time in",max(end),"second")