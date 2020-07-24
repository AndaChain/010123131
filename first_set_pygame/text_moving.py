################################################################
# File: work_1.py
# Date: 2020-07-10, 16:31
################################################################

from random import randint
import pygame
import time
import math

#ฟังก์ชันนี้ใช้สำหรับแปลงวันที่แบบภาษาอังกฤษเป็นภาษาไทยโดยใช้ดิกชันนารีมาเก็บ วันภาษาไทย เดือนภาษาไทย
def Time_function(mode=''):
    #named_tuple = time.localtime() # get struct_time
    if mode == "thai":
        day = {1:"วันจันทร์", 2:"วันอังคาร", 3:"วันพุธ", 4:"วันพฤหัสบดี", 5:"วันศุกร์", 6:"วันเสาร์", 0:"วันอาทิตย์"}
        month = {0:"มกราคม", 1:"กุมภาพันธ์", 2:"มีนาคม", 3:"เมษายน", 4:"พฤษภาคม", 5:"มิถุนายน", 6:"กรกฎาคม"
        , 7:"สิงหาคม", 8:"กันยายน", 9:"ตุลาคม", 10:"พฤศจิกายน", 11:"ธันวาคม"}

        Day = day.get(int(time.strftime("%w")))
        Month = month.get(int(time.strftime("%m"))-1) #ลบ 1 เพราะ มกราคมคือ 1
        Year = int(time.strftime("%Y"))+543

        thai_format_date = time.strftime(f"{Day}, %d/{Month}/{Year}, เวลาคือ %H:%M:%Sน.")
        return thai_format_date

    date = time.strftime(f"%A, %d/%B/%Y, Time is %I:%M:%S %p")
    return date

def run():
    #@@@@@ รหัสสีแบบ tuple
    WHITE = (255, 255, 255) 
    GREEN = (0, 255, 0) 
    BLUE  = (0, 0, 255)
    BLACK = (0, 0, 0)


    # initialize pygame
    pygame.init()

    #-------------------------------------- @@@@@ แสดงฟอนต์ที่สามารถใช้ได้
    # show available PyGame fonts
    fonts = pygame.font.get_fonts()
    print( 'Number of fonts available: {}'.format( len(fonts) ) )
    for f in fonts:
        print( 'Font "{}"'.format(f) )
    #--------------------------------------

    # create a screen of width=600 and height=400 @@@@@ หน้าจอกว้าง 600x400
    scr_w, scr_h = 600, 400
    screen = pygame.display.set_mode( (scr_w, scr_h) )

    # set window caption @@@@@ ชื่อที่แทบบน
    pygame.display.set_caption('Time slide.') 

    # @@@@@ ฟอนต์ที่จะใช้ในหน้าจอ
    pygame.font.init()
    #text_font = pygame.font.SysFont('browallianewbrowallianewbrowallianewboldbrowallianewitalicbrowalliaupcbrowalliaupcboldbrowalliaupcbolditalicbrowalliaupcitalic', 36)
    text_font = pygame.font.SysFont("eucrosiaupc", 30)

    #text_font = pygame.font.Font("FreeSans.ttf", 36)
    #text_font = pygame.font.Font("THSarabunNew.ttf", 48)

    # create a clock @@@@@ เรียกฟังก์ชันเวลามา
    clock = pygame.time.Clock()

    # set the initial value for x-position @@@@@ กำหนดตำแหน่ง x
    x = scr_w
    #y = -scr_h
    y = scr_h

    """h = 0
    radius_s=220
    radius_m=220
    radius_h=180"""

    # @@@@@ ให้หน้าจอเล่นซ้ำเรื่อยๆโดยใช้ "while" ลูป
    running = True
    while running:

        # This limits the while loop to a max of 30 times per second. @@@@@ หน่วงเวลาไป 30 ครั้งการทำงาน/1 วินาที
        clock.tick(30) 

        # check four QUIT button event @@@@@ ตรวจว่ามีการกดปุ่มออก [X] หรือไม่ (ถ้าไม่มีกดไม่ได้และจะ "not responding" ไปเลยควรใส่)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                print('exit')
        
        msg = Time_function() #ข้อความภาษาอังกฤษ
        msg2 = Time_function("thai") #ข้อความไทย
        

        text_width, text_height = text_font.size( msg )

        text_surface = text_font.render( msg, False, (0,0,255) )
        text_surface2 = text_font.render( msg2, False, (50,50,255) ) #ข้อความไทย
        text_width, text_height = text_surface.get_rect()[2:]

        # fill the screen with white color @@@@@ สีพื้นหลังหน้าจอ
        screen.fill( GREEN )
        #bg =pygame.image.load("C:/Users/s6201012620279/Software development/100763/picture/picture2.jpg")
        #screen.blit(bg,[0,0])

        # set the y position for text drawing @@@@@ กำหนดตำแหน่ง y
        """y = scr_h//2 - text_height"""
        x = scr_w - text_width - 110
        x_thai = scr_w - text_width - 120

        # show text on the screen @@@@@ แสดงข้อความบนหน้าจอ
        """h += 1
        if(h == 60):
            h = 0"""
        #pos=[math.cos(math.radians(h*6+270))*radius_h+330,math.sin(math.radians(h*6+270))*radius_h+330]
        screen.blit( text_surface,(x,y+150) )
        screen.blit( text_surface2,(x_thai,y+175) ) #ข้อความไทย

        # decrease the x position for the next text drawing @@@@@ มันจะลดค่า x ไปเลื่อนๆจนสุดของความกว้างที่ติดลบของตัวหนังสือ (เลื่อนไปจนสุดหน้าจอฝั่งซ้าย)
        # และค่อยทำให้กลับมาค่าเดิมคือเท่ากับความกว้างตัวอักษร ทำไปเรื่อยๆจนกว่าผู้ใช้กดปุ่มออก [X]
        
        #ขวาไปซ้าย
        """x -= 4
        if x < -text_width:
            x = scr_w"""

        #ซ้ายไปขวา
        """x += 4
        if x > text_width:
            x = -scr_w"""

        #ล่างขึ้นบน
        y -= 4
        if y < -text_height-175: #ลบ 75 จะได้ไหลไปครบก่อนที่จะเริ่มรอบใหม่
            y = scr_h

        """#บนลงล่าง
        y += 4
        if y > scr_h: #ลบ 50 จะได้ไหลไปครบก่อนที่จะเริ่มรอบใหม่
            y = -75"""


        # update the entire display. @@@@@อัพเดทหน้าจอให้ชุดคำสั่งทำงาน
        pygame.display.flip()

    pygame.quit()

#สั่งทำงานฟังก์ชัน run
run()

################################################################
# To do: Write PyGame code that shows a running text  with current 
# local time and date for both Thai and English languages.
################################################################
