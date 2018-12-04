from sense_hat import SenseHat
sense = SenseHat()
r = (255,0,0)
w = (255,255,255)
b = (0,0,0)
sense.clear(w)
maze = [
    [r,r,r,r,r,r,r,r,],
    [r,b,b,r,b,b,b,r,],
    [r,b,r,r,b,r,b,r,],
    [r,b,b,b,b,r,b,r,],
    [r,b,r,b,b,r,r,r,],
    [r,r,r,r,b,r,b,r,],
    [r,b,b,b,b,b,b,r,],
    [r,r,r,r,r,r,r,r,],
    ]
sense.set_pixels(sum(maze,[]))
sense.set_pixel(1,1,w)

