import pygame
from pygame.locals import *
from OpenGL.GL import *
from Cubo import *
from OpenGL.GLU import *
from Object import *
from Transform import *

# Alunos:
# Jeferson Bruno Bezerra Silva
# Mônica Guerra De Oliveira
# Maria Luiza Guerra Soares

pygame.init()
screen_width = 700
screen_height = 700
screen = pygame.display.set_mode((screen_width,screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption("Inicio PyOpenGL")

done = False
branco = pygame.Color(255,255,255)
glMatrixMode(GL_PROJECTION)
gluPerspective(60, (screen_width/screen_height), 0.1, 100.0)
glMatrixMode(GL_MODELVIEW)
glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)
glLight(GL_LIGHT0, GL_POSITION, (5, 5, 5, 1))
glLightfv(GL_LIGHT0, GL_DIFFUSE,(1,1,1,1))
glLightfv(GL_LIGHT0, GL_SPECULAR,(0,1,0,1))
glEnable(GL_LIGHT0)
glMaterial(GL_FRONT, GL_DIFFUSE, (1,0,0,1))
glTranslatef(0.0,0.0,-3.0)

objects = []

cubo = Object( "Cubo")
cubo.add_component(Transform(( 0, 0, -1)))
cubo.add_component(Cubo(GL_POLYGON, "../Texturas/Pac Man.png" ))
objects.append(cubo)

cubo2 = Object("Cubo2")
cubo2.add_component(Transform((0, 1, 0)))
cubo2.add_component(Cubo(GL_POLYGON, "../Texturas/bricks1.png"))
objects.append(cubo2)

clock = pygame.time.Clock()
fps = 30

while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glRotatef(5, 1, 0, 1)

    for obj in objects:
        obj.update()

    pygame.display.flip()
    #print("tick = {}, fps = {}".format(clock.tick(fps), clock.get_fps()))
    clock.tick(fps)
pygame.quit()