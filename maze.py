#0 for move, 1 for block, 2 for home
def drawBoard(a):
    for row in maze:
        print(row)
    print()

maze=[[0,0,0,0],[0,0,-1,-1],[0,-1,0,-1],[0,0,0,2]]
xmax=3
ymax=3
dir=1
count=1
y=0
x=0
drawBoard(maze)
while True:
#*******************************Move forward**********************8
    if dir == 1:
        if x>=xmax:
            dir = (dir + 1) % 4
        elif maze[y][x+1]==-1:
            dir = (dir + 1) % 4
        else:
            x=x+1
            maze[y][x]=count
            count+=1
            dir = (dir + 3) % 4
#*******************************Move forward**********************8
    if dir==2:
        if y>=ymax:
            dir=(dir + 1) % 4;
        elif maze[y+1][x]==-1:
            dir = (dir + 1) % 4
        else:
            y+=1
            maze[y][x]=count
            dir =(dir + 3)%4
            count+=1
#*******************************Move forward**********************8
    if dir==3:
        if x<=0:
            dir =(dir + 1) % 4
        elif maze[y][x-1]==-1:
            dir = (dir + 1) % 4
        else:
            maze[y][x-1]=count
            count+=1
            x-=1
            dir =(dir + 3) %4
#*******************************Move forward**********************8
    if dir==0:
        if y<=0:
            dir =(dir + 1) % 4
        elif maze[y-1][x]==-1:
            dir = (dir + 1) % 4
        else:
            maze[y-1][x]=count
            count+=1
            dir =(dir + 3) %4
            y-=1
    drawBoard(maze)
    input()
    if y==3 and x==3:
        drawBoard(maze)
        break
    if y==0 and x==0:
        print("blocked")
        drawBoard(maze)
        break




