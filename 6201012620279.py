"""
HEAD HEAD HEAD HEAD HEAD HEAD HEAD HEAD HEAD HEAD HEAD HEAD HEAD HEAD HEAD HEAD HEAD HEAD HEAD HEAD HEAD HEAD HEAD HEAD HEAD HEAD 
######################################
Coding by: Anda Pattanachoo
file: 6201012620279.py
Date: 2020-07-23,24
######################################
"""

import threading
import time
import pygame

print( 'Runnig file at:', __file__ )

# initialize pygame
pygame.init()

# set screen is width=500 and height=500
scr_w, scr_h = 500, 500
screen = pygame.display.set_mode( (scr_w, scr_h) )

# set window title
pygame.display.set_caption('Mandelbrot set image by multithreading programing.') 

# create a surface ***for drawing***
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

# half width half hight ***for set visual at center***
w_half, h_half = scr_w/2, scr_h/2

# create a clock
clock = pygame.time.Clock()

#start = time.time()

# Heart of this program!!!!. Do calculate Mandelbrot set to fill colour in a pixel
def mandelbrot(c,max_iters=100):
    i = 0
    z = complex(0,0)
    while abs(z) <= 2 and i < max_iters:
        z = z*z + c
        i += 1
        
    return i

# fill colour in a pixel follower by mandelbrot set
def fill_colour_each_pixel(i, sem, lock):
    scale = 0.006
    offset = complex(-0.55,0.0)

    # w_th is how width each thread running
    # w_th = int(scr_w/N)
    # h_20 = int(scr_h/N) !!No using!!

    # i = current thread id & i+1 is next thread id
    if( sem.acquire(timeout=0.1) ):
        for x in range(i*w_th, (i+1)*w_th):
            for y in range(scr_h):   
                with lock:
                    ###################### Main engine #########################
                    re = scale*(x-w_half) + offset.real
                    im = scale*(y-h_half) + offset.imag
                    c = complex( re, im )

                    color = mandelbrot(c, 63)
                    r = (color << 6) & 0xc0
                    g = (color << 4) & 0xc0
                    b = (color << 2) & 0xc0
                    surface.set_at( (x, y), (255-r,255-g,255-b) )
                    ############################################################
# set number of thread for running program
N = 100
w_th = int(scr_w/N)

# lock thread
lock = threading.Lock()

# list of semaphore **for lock thread**
list_sem = [threading.Semaphore(0) for i in range(N)]

# list of thread
list_threads = []

# create list of thread
for thread_id in range(N):
    sem = list_sem[thread_id]
    thread = threading.Thread(target=fill_colour_each_pixel, args=(thread_id, sem, lock))
    list_threads.append(thread)

# time to start threads!!! oh yessss!!
for thread in list_threads:
    thread.start()

#running all time
running = True
while running:

    for thread in list_sem:
        thread.release()

    time.sleep(0.01)

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

#print(time.time()-start)
pygame.quit()
print( 'Mandelbrot is ... Good!!!!!!!!!!!!!!!!!!!!!!')
"""
TAIL TAIL TAIL TAIL TAIL TAIL TAIL TAIL TAIL TAIL TAIL TAIL TAIL TAIL TAIL TAIL TAIL TAIL TAIL TAIL TAIL TAIL TAIL 
"""

