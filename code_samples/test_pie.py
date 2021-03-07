import pygame
from math import sin,cos,radians

#function to draw pie using parametric coordinates of circle
def pie(scr,color,center,radius,start_angle,stop_angle):
    theta=start_angle
    while theta <= stop_angle:
        print((center[0]+radius*cos(radians(theta)),center[1]+radius*sin(radians(theta))))
        pygame.draw.line(scr, color, center, (center[0]+radius*cos(radians(theta)),center[1]+radius*sin(radians(theta))), 2)
        theta+=0.01

#for example:-
if __name__=="__main__":
    while True:
        winWidth,winHeight=500,500
        scr=pygame.display.set_mode((winWidth, winHeight))

        pie(scr,(255,0,0),(winWidth//2, winHeight//2), 250, 180, 360)
        pygame.display.update()