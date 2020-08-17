import pygame
import time

import CreateTree # create tree by list
import SplitExpression # Split a Expression to a list
import Filter # Filter a bracket

width,high = 800,600

# Colour Set
Black = (0,0,0)
White = (255,255,255)
Green = (0,255,0)
Red = (255,0,0)
blue = (82,220,200)
Blue = (82,100,220)


pygame.init()

display = pygame.display.set_mode([width,high],0,32)
pygame.display.set_caption("Visualization a Binary Tree")
myfont = pygame.font.SysFont("Comic Sans MS",20)
display.fill(White)

#----------------------------------------------Class Node & Line#----------------------------------------------
class Node:
    def __init__(self, x, y, text, radian=20):
        self.x = x
        self.y = y
        self.text = text
        self.radian = radian

    def draw(self, colour):
        # if text is "" then ignore them
        if(self.text != ""):
            pygame.draw.circle( display, colour, [self.x, self.y], self.radian )
            label = myfont.render( str(self.text),1,(Black) )
            display.blit( label,(self.x-5, self.y-15) )
            pygame.display.update()

class Line:
    def __init__(self, x_start, y_start):
        self.x_start = x_start
        self.y_start = y_start

    def draw(self, target ,colour):
        # Is a target node ""
        if(target.text != ""):
            pygame.draw.line(  display, colour, [self.x_start,self.y_start], [target.x, target.y], 5)
            pygame.display.update()
        else:
            pass

#-------------------------------------------------------------------------------------------------------------

# data set for testing my algorithm
Test_data_set = (  "!(1+0)" # index 0
                    ,"!(!(0+I0&1))" # index 1
                    ,"(I0+!I1+!(I2))&(!I0+I1+I2)" # index 2
                    ,"!(I0&I1)+!(I1+I2)" # index 3
                    ,"(((I0&I1&!I2)+!I1)+I3)" # index 4
                    ,"((I2&I1)+(I0&I1))" # index 5
                    ,"I2&I1+I0&I1" # index 6
                    ,"(I0&I1+!(I1&I2))" # index 7
                    ,"!!!I1+!!I0" # index 8
                    ,"I1&I0+I3&!!I0" # index 9
                    ,"!!!I0" # index 10  
                    ,"( ((I0&I1+I0&I1)&(I0&I1+I0&I1))+((I0&I1+I0&I1)&(I0&I1+I0&I1)) )"  ) # index 11


index = 2
q = 0
split_expression = SplitExpression.Boolean_algebra(Test_data_set[index]).split_expreesion()
Test = CreateTree.CreateTree()
result = Test.Tree('','','',split_expression, q)

print(result)
# (I0+!I1+!(I2))&(!I0+I1+I2) Test 3
#                                       &
#                             /                  \
#                      +                              +
#              /               \                  /       \
#            +                    !            +             I2
#          /    \               /            /   \          
#      I0        !           I2            !      I1      
#              /                         /
#            I1                        I0

def cut(Result):
    i = 0
    new = []
    while(i < 31):
        new.append(result[i])
        i += 1
    return new

def pre_draw_node():
    radian = 20
    x = 0
    y = (high-radian-200) # 200 is offset bottom
    border = radian
    Index = len(already_cut)-1

    for R in range(Level): # level of tree
        Power = (2**R) # number of node
            
        # W*Power is divided node on each level
        for i in range(width-border-5, border, -W*Power): # since (far left border) to (far right borader)
            x = i
            circle = Node(x, y, already_cut[Index])
            pos_draw_line.append(circle)

            Index -= 1

        border += Power*25 # Level 5
        
        # ***************NO Use************************
        #border += Power*54 # Level 4
        #border += Power*126 # Level 3
        #border += Power*379 # Level 2
        #border += Power # Level 1
        # *********************************************

        y -= H + radian -80 # 80 is offset distance each level

def connect_node_and_line():
    pos_draw_line.reverse()

    for j in range(len(pos_draw_line)):
        # q is root index
        # pl is left index
        # pr is right index
        print(pos_draw_line[j].x, pos_draw_line[j].y, pos_draw_line[j].text)

        # set index
        q = j
        pl = 2*q + 1
        pr = 2*q + 2

        if(  pr > len(pos_draw_line)-1  ):
            break

        # set x, y and text in target node
        x_node = pos_draw_line[q].x
        y_node = pos_draw_line[q].y
        text_node = pos_draw_line[q].text
        
        # draw line to target
        line = Line(x_node, y_node)
        line.draw(pos_draw_line[pl], Black)
        line.draw(pos_draw_line[pr], Black)

        # draw node after draw line because I want node cover line
        pos_draw_line[q].draw(Blue)
        pos_draw_line[pl].draw(Blue)
        pos_draw_line[pr].draw(Blue)

Level = 5 # level of tree
column = 2**(Level-1) # column
row = Level # row
pos_draw_line = [] # contain position for draw Tree
W = width//column
H = high//row

already_cut = cut(result)
pre_draw_node()
connect_node_and_line()

running = True
while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.image.save(display, "screenshot.jpg")
            running = False
    label = myfont.render( str(Test_data_set[index]),1,(Black) )
    display.blit( label,(0, 0) )
    pygame.display.update()

pygame.quit()