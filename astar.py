import pygame
import random
import cell as cell


width = 800
height = 600

column = 40
row = 30
blockSize = 20

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Astar demo')

done = False
clock = pygame.time.Clock()

cells = []

open =[]

close = []

    

def updateGUI():

    for c in cells:
        c.draw()


def createCells():
    color = (0,0,0)


    for j in range(row):
        for i in range(column):
            cells.append(cell.cell(i*blockSize, j* blockSize, blockSize, color, screen))

start = None
end = None
def initGame():
    global start
    global end
    start = cells[5*column+5] #(5,5)
    end = cells[20*column + 30] #(30,20)

    start.SetStart()
    end.SetEnd()

found = False
def ShowPath():
    c = end
    while c is not start:
        c = c.pre
        c.color = (0,255,0)
def checknode(index,o):
        if cells[index] in close:
            return
        if cells[index].block:
            return
        elif cells[index].end:
            global found 
            found = True
            print("found")
            cells[index].SetPre(o)
            ShowPath()
            return
        elif cells[index] in open:
            if cells[index].h + o.step +1 < cells[index].f:
                cells[index].SetPre(o)
        else :
            cells[index].SetPre(o)
            open.append(cells[index])
            cells[index].color = (20,120,255)

def move():
    if(len(open) == 0):
        return
    # find smallest node    
    o=open[0]
    for c in open:
        if c.f < o.f:
            o = c

    open.remove(o)
    # 4 possible moves
    index = 0;
    x = int((o.x )/blockSize)
    y = int((o.y ) /blockSize)
    if x > 0:
        index = y*column + x -1
        checknode(index, o)
    if(x< column -1):
        index = y*column +x +1
        checknode(index, o)
    if y > 0:
        index = column * (y -1) +x
        checknode(index, o)
    if y < row -1:
        index = column * ( y+1) + x
        checknode(index, o)

    if not found:
        close.append(o)
        o.color = (255,255,255)
        
# initialize cells
createCells()
initGame()
open.append(start)


print("Edit mode")
edit = True
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                edit = False
                print("Start")

    if edit and pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()
        x = int(pos[0]/blockSize)
        y = int(pos[1]/blockSize)
        if x >= 0 and x <column and y >=0 and y< row and not cells[column*y +x].start and not cells[column*y+x].end:
            cells[column*y +x].SetBlock()
    screen.fill((255, 255, 255))
    if not found and not edit:
        move()
    updateGUI()
    pygame.display.flip()
    clock.tick(60)
