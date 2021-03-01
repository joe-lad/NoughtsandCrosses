import pygame
import time

pygame.init()

WIDTH = 350
HEIGHT = 300
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('My Game')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.font.init()

SCREEN.fill(WHITE)

cords = {
    "CenterCol" : 175.0,
    "RightCol" : 291.6666666666667,
    "LeftCol" : 58.333333333333336,
    "Top" : 50.0,
    "Middle" : 150.0,
    "Bottom" : 250.0,
}

boxes = {
}

# check if 3 in row with dict (cords : name) print(175, 50) = x or o
def checkcondition(cords):
    possiblewinRow()
    possiblewinCol()
    possiblewinCross()
    if len(boxes) == 9:
        win('DRAW')
        
def possiblewinRow():
    col = [59, 175, 291]
    row = [50, 150, 250]
    top = []
    middle = []
    bottom = []
    for i in range(0, 3):
        for j in range(0, 3):
            temp = col[j], row[i]
            tup = tuple(temp)
            if tup in boxes:
                if row[i] == 50:
                    top.append(boxes[tup])
                elif row[i] == 150:
                    middle.append(boxes[tup])
                elif row[i] == 250:
                    bottom.append(boxes[tup])
            else:
                'nohere'

    if len(top) == 3:
        if 'o' in top:
            if 'x' not in top:
                win('o')
        else:
            win('x')
    if len(middle) == 3:
        if 'o' in middle:
            if 'x' not in middle:
                win('o')
        else:
            win('x')
    if len(bottom) == 3:
        if 'o' in bottom:
            if 'x' not in bottom:
                win('o')
        else:
            win('x')

def possiblewinCol():
    col = [59, 175, 291]
    row = [50, 150, 250]
    left = []
    middleCol = []
    right = []
    for i in range(0, 3):
        for j in range(0, 3):
            temp = col[i], row[j]
            tup = tuple(temp)
            if tup in boxes:
                if row[i] == 50:
                    left.append(boxes[tup])
                elif row[i] == 150:
                    middleCol.append(boxes[tup])
                elif row[i] == 250:
                    right.append(boxes[tup])
            else:
                'nohere'
                
    if len(left) == 3:
        if 'o' in left:
            if 'x' not in left:
                win('o')
        else:
            win('x')
    if len(middleCol) == 3:
        if 'o' in middleCol:
            if 'x' not in middleCol:
                win('o')
        else:
            win('x')
    if len(right) == 3:
        if 'o' in right:
            if 'x' not in right:
                win('o')
        else:
            win('x')

def possiblewinCross():
    col = [59, 175, 291]
    row = [50, 150, 250]
    leftright = []
    rightleft = []
    for i in range(0, 3):
        temp = col[i], row[i]
        tup = tuple(temp)
        if tup in boxes:
            leftright.append(boxes[tup])
    for i in range(0, 3):
        if i == 0:
            temp = col[i], row[2]
            tup = tuple(temp)
            if tup in boxes:
                rightleft.append(boxes[tup])
        elif i == 1:
            temp = col[i], row[1]
            tup = tuple(temp)
            if tup in boxes:
                rightleft.append(boxes[tup])
        else:
            temp = col[i], row[0]
            tup = tuple(temp)
            if tup in boxes:
                rightleft.append(boxes[tup])
                
    if len(leftright) == 3:
        if 'o' in leftright:
            if 'x' not in leftright:
                win('o')
        else:
            win('x')
    if len(rightleft) == 3:
        if 'o' in rightleft:
            if 'x' not in rightleft:
                win('o')
        else:
            win('x')

            

def checkpos(posx, posy):
    ycolumns = [50, 150, 250]
    for y in ycolumns:
        if y - 50 <= posy <= y + 50:
            drawy = y
    xcolumns = [59, 175, 291]
    for x in xcolumns:
        if x - 58 <= posx <= x + 58:
            drawx = x
    return(drawx, drawy)

def win(winstate):
    if winstate == 'DRAW':
        print(f'{winstate} - you tied')
        winstate = f'{winstate} - you tied'
    else:
        print(f'{winstate} won this match')
        winstate= f'{winstate} won this match'

    blankwin(winstate)

def blankwin(winstate):
    time.sleep(2)
    SCREEN.fill((0, 0, 0))
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render(winstate, False, (255, 255, 255))
    SCREEN.blit(textsurface,(100, 0))
    pygame.display.update()

turns = 1 

is_running = True
while is_running:
    pygame.display.flip()

    class lines(object):
        for Lines in range(1, 3):
            pygame.draw.line(SCREEN, BLACK, (WIDTH/3 * Lines, 0), (WIDTH/3 * Lines, HEIGHT), 4)
            pygame.draw.line(SCREEN, BLACK, (0, HEIGHT/3 * Lines), (WIDTH, HEIGHT/3 * Lines), 4)
        
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            posx = int(pos[0])
            posy = int(pos[1])
            cordofdraw = checkpos(posx, posy)
            if turns % 2 == 0:
                if cordofdraw not in boxes:
                    turns += 1
                    pygame.draw.circle(SCREEN, BLACK, cordofdraw, 10, 2)
                    boxes.update({cordofdraw : 'o'})
                    pygame.display.flip()
                    checkcondition(cordofdraw)
            else:
                if cordofdraw not in boxes:
                    turns += 1
                    pygame.draw.lines(SCREEN, BLACK, False, [(cordofdraw[0]+10, cordofdraw[1]+10), (cordofdraw[0]-10, cordofdraw[1]-10), (cordofdraw[0], cordofdraw[1]), (cordofdraw[0]-10, cordofdraw[1]+10), (cordofdraw[0]+10, cordofdraw[1]-10)], 4)
                    boxes.update({cordofdraw : 'x'})
                    pygame.display.flip()
                    checkcondition(cordofdraw)
        if event.type == pygame.QUIT:
            is_running = False

pygame.quit()
