from Object import *
from Cubo import *
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Button import *


def set_2d():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 1600, 0, 1200)
    #gluOrtho2D(0, screen.get_width(), 0, screen.get_height())
    glMatrixMode(GL_MODELVIEW)
    ##glLoadIdentity()
    glViewport(0, 0, screen.get_width(), screen.get_height())

def set_3d():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective( 60, (screen_width / screen_height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glViewport( 0, 0, screen.get_width(),    screen.get_height())
    glEnable(GL_DEPTH_TEST)

pygame.init()
screen_width = 800
screen_height = 600

pygame.display.set_caption( 'Button Interaction')
screen = pygame.display.set_mode((screen_width,screen_height), DOUBLEBUF | OPENGL)
done = False
white = pygame.Color( 255, 255, 255)
green = pygame.Color( 0, 255, 0)
blue = pygame.Color( 0, 0, 255)
objects_3d = []
objects_2d = []

button1 = Object( "Button")
button1.add_component(Button(screen, ( 0, 0), 100, 50, white, green, blue))
objects_2d.append(button1)

cubo = Object( "Cubo")
cubo.add_component(Transform(( 0, 0, -5)))
cubo.add_component(Cubo(GL_POLYGON,"../Texturas/bricks1.png" ))
objects_3d.append(cubo)
clock = pygame.time.Clock()
fps = 30

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    glPushMatrix()
    glClear(GL_COLOR_BUFFER_BIT |
    GL_DEPTH_BUFFER_BIT)
    set_3d()
    for o in objects_3d:
        o.update()
    set_2d()
    for o in objects_2d:
        o.update()
    glPopMatrix()
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()