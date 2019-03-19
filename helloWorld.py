import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import * 


def display_text():

    glColor3f(1.0,1.0,1.0)

    string =  "Hello World"

    x=0.5
    #glRasterPos2f((x-800.0)/2,0)
    
    for i in string: 
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24,ord(i))
                
def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Example code for Hello World in OpenGL")
    done = False
    
    while not done:
        pygame.time.wait(1000)
    
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                done=True 
        
        display_text()
        pygame.display.flip()
    
    pygame.quit()
	
main()