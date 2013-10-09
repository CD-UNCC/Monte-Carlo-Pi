#A Monte Carlo method of Approximating Pi
Author = 'Scott Clark'
Date = 'June 21 2013'
from PIL import Image, ImageDraw
import math as m
import random, sys
while True:
    img = Image.new( 'RGB', (200,200), "black")
    pixels = img.load()
    points = 0.0
    pointsIn = 0.0
    print 'Enter amount of points to pick (Enter 0 to exit): '
    iterations = input()
    if iterations == 0:
        sys.exit()
    for i in range(0,iterations):
        x = random.randint(0,199)
        y = random.randint(0,199)
        if((m.pow(x-100.0,2.0)+m.pow(y-100.0,2.0)) < m.pow(100.0,2.0)):
            pixels[x,y] = (0, 0, 100)
            pointsIn = pointsIn + 1.0
        else:
            pixels[x,y] = (100, 0, 0)
        points = points + 1.0
    print "points in circle: ",pointsIn*4,"total points: ", points
    Pi =(4.0*pointsIn/points)
    print "Our approximation: ",Pi
    print "Actual value of pi: ",m.pi
    img.show()
