from sense_hat import SenseHat
sense = SenseHat()
from time import sleep
import random


false = False
true = True
r = (0,0,255)
w = (255,255,255)
b = (0,0,0)
k = (255,0,0)
g = (0,255,0)
wins = 0
losses = 0


maze1 = [
    [r,r,r,r,r,r,r,r,],
    [r,b,b,r,b,b,b,r,],
    [r,b,r,r,b,r,b,r,],
    [r,b,b,b,b,r,g,r,],
    [r,b,r,k,b,r,r,r,],
    [r,r,r,r,b,r,b,r,],
    [r,k,b,b,b,b,b,r,],
    [r,r,r,r,r,r,r,r,],
    ]
maze2 = [
    [r,r,r,r,r,r,r,r,],
    [r,b,r,k,r,k,b,r,],
    [r,b,r,b,r,r,b,r,],
    [r,b,r,b,b,b,b,r,],
    [r,b,b,b,r,k,b,r,],
    [r,b,r,b,r,r,b,r,],
    [r,k,r,b,r,g,b,r,],
    [r,r,r,r,r,r,r,r,],
    ]
maze3 = [
    [r,r,r,r,r,r,r,r,],
    [r,b,b,b,b,b,k,r,],
    [r,r,r,b,r,r,r,r,],
    [k,b,b,b,b,b,r,r,],
    [r,b,b,r,b,b,k,r,],
    [r,b,r,r,b,r,r,r,],
    [r,b,g,r,b,b,k,r,],
    [r,r,r,r,r,r,r,r,],
    ]
maze4 = [
    [r,r,r,r,r,r,r,r,],
    [r,b,r,b,b,b,b,r,],
    [r,b,r,r,b,r,b,r,],
    [r,b,r,g,b,r,b,r,],
    [r,b,r,k,b,r,b,r,],
    [r,b,r,r,r,r,b,r,],
    [r,b,b,b,b,b,b,r,],
    [r,r,r,r,r,r,r,r,],
    ]
maze5 = [
    [r,r,r,r,r,r,r,r,],
    [r,b,b,r,g,b,b,r,],
    [r,b,b,r,r,b,b,r,],
    [r,r,b,k,k,b,r,r,],
    [r,r,b,k,k,b,r,r,],
    [r,b,b,r,r,b,b,r,],
    [r,b,b,b,b,b,b,r,],
    [r,r,r,r,r,r,r,r,]
    ]
mazes = [maze1,maze2,maze3,maze4,maze5]
maze = random.choice(mazes)
y=1
x=1
gameOver = False
win = False
while gameOver == False:
    maze[y][x] = w
    o = sense.get_orientation()
    pitch = o["pitch"]
    roll = o["roll"]
    yaw = o["yaw"]
    if 10 < pitch and pitch < 170:
        if not gameOver and not win:
            if maze[y][x-1]==b:
                maze[y][x]=b
                x -= 1
            if maze[y][x-1]== g:
                maze[y][x]=b
                x -= 1
                win = True
            if maze[y][x-1]==k:
                maze[y][x]=b
                x -= 1
                gameOver=true
    if 170 < pitch and pitch < 350:
        if not gameOver and not win:
            if maze[y][x+1]== b:
                maze[y][x]= b
                x += 1
            if maze[1][x+1]== g:
                maze[y][x]= b
                x += 1
                win = True
                print(' hi ')
            if maze[y][x+1]== k:
                maze[y][x]=b
                x += 1
                gameOver = True
    if 10 < roll and roll < 170:
        if not gameOver and not win:
            if maze[y+1][x]== b:
                maze[y][x]=b
                y += 1
            if maze[y+1][x]==g:
                maze[y][x]=b
                y += 1
                win=true
            if maze[y+1][x]==k:
                maze[y][x]=b
                y += 1
                gameOver=true
    if 170 < roll and roll < 350:
        if not gameOver and not win:
            if maze[y-1][x]==b:
                maze[y][x]=b
                y -= 1
            if maze[y-1][x]==g:
                maze[y][x]=b
                y -= 1
                win = true
            if maze[y-1][x]==k:
                maze[y][x]=b
                y -= 1
                gameOver=true
    maze[y][x] = w
    if not win and not gameOver:
        sense.set_pixels(sum(maze,[]))
    if win:
        sense.set_pixels(sum(maze,[]))
        sleep(.125)
        wins += 1
        maze[y][x] = g
        if wins == 10:
            sense.show_message('You Win!',.1,w,g)
            break
        else:
            sense.show_letter(str(wins),w,g)
            sleep(1)
            maze = random.choice(mazes)
            win = false
            x=1
            y=1
        sense.set_pixels(sum(maze,[]))
        sleep(.5)
    if gameOver:
        sense.set_pixels(sum(maze,[]))
        sleep(.25)
        losses += 1
        maze[y][x]= k
        if losses == 10:
            sense.show_message('You lose.',.1,w,k)
            break 
        else:
            sense.show_letter(str(losses),w,k)
            sleep(1)
            gameOver = false
            x=1
            y=1
            sense.set_pixels(sum(maze,[]))
