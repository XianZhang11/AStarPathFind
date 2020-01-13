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

opon =[]

close = []

    

def updateGUI():

    for c in cells:
        c.draw()


def createCells():
    color = (0,0,0)
    size = 16

    for i in range(40):
        for j in range(30):
            
            cells.append(cell.cell(i*20+2, j* 20+2, size, color, screen))

def initGame():
  cells[0].SetStart()
  cells[-1].SetEnd()
  #random some blocks
  for c in cells[1:-2]:
      if random.randint(1,4)  == 3 :
         c.SetBlock() 

found = false
def move():
    if found: 
        return
    if(len(open) == 0):
        return
    
    o=open[0]
    for c in open:
        if c.f < o.f:
            o = c



# initialize cells
createCells()
initGame()


open.append(cells[0])

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255))
    updateGUI()
    pygame.display.flip()
    clock.tick(60)
