import pygame
import random
import cell as cell


width = 800
height = 600

pygame.init()
screen = pygame.display.set_mode((width, height))
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
    size = 16

    for j in range(30):
        for i in range(40):
            
            cells.append(cell.cell(i*20+2, j* 20+2, size, color, screen))

def initGame():
  cells[0].SetStart()
  cells[-1].SetEnd()
  #random some blocks
  for c in cells[1:-2]:
      if random.randint(1,3)  == 2 :
         c.SetBlock() 

found = False
def ShowPath():
    c = cells[-1]
    while c is not cells[0]:
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
    
    o=open[0]
    for c in open:
        if c.f < o.f:
            o = c

    open.remove(o)
    # 4 possible moves
    index = 0;
    x = int((o.x -2 )/20)
    y = int((o.y -2) /20)
    if x > 0:
        index = y*40 + x -1
        checknode(index, o)
    if(x< 40 -1):
        index = y*40 +x +1
        checknode(index, o)
    if y > 0:
        index = 40 * (y -1) +x
        checknode(index, o)
    if y < 30 -1:
        index = 40 * ( y+1) + x
        checknode(index, o)

    if not found:
        close.append(o)
        o.color = (255,255,255)
        
# initialize cells
createCells()
initGame()
print(len(cells))
open.append(cells[0])

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255))
    if not found:
        move()
    updateGUI()
    pygame.display.flip()
    clock.tick(30)
