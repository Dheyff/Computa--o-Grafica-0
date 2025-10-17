from Malha3D import *
from Transform import *
from OpenGL.GL import *

class Object:

    def __init__(self, obj_name):
        self.name = obj_name
        self.components = []

    def add_component (self, component):

        self.components.append(component)

    def update(self):
        glPushMatrix()
        for c in self.components :
            if isinstance(c, Transform):
                pos = c.get_position()
                glTranslatef(pos.x, pos.y, pos.z)

            if isinstance(c, Malha3D):
                c.desenhar()
        glPopMatrix()

