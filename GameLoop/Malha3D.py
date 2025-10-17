from OpenGL.GL import *
import pygame.image

class Malha3D:
    def __init__(self):
        self.vertices = [
            (0.5, -0.5, 0.5), (0.5, 0.5, 0.5),
            (-0.5, -0.5, 0.5), (-0.5, 0.5, 0.5),
            (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5)
        ]

        self.triangulos = [0, 2, 3,0,3,1]
        self.draw_type = GL_LINE_LOOP
        self.texture = None
        self.texID = 0

    def desenhar(self):
        glEnable(GL_TEXTURE_2D)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
        glBindTexture(GL_TEXTURE_2D, self.texID)
        for t in range (0, len(self.triangulos),3):
            glBegin(self.draw_type)
            glTexCoord2fv(self.uvs[self.triangulos[t]])
            glVertex3fv(self.vertices[self.triangulos[t]])
            glTexCoord2fv(self.uvs[self.triangulos[t + 1]])
            glVertex3fv(self.vertices[self.triangulos[t + 1]])
            glTexCoord2fv(self.uvs[self.triangulos[t + 2]])
            glVertex3fv(self.vertices[self.triangulos[t + 2]])
            glEnd()
        glDisable(GL_TEXTURE_2D)

    def init_texture(self):
        self.texID = glGenTextures(1)
        textureData = pygame.image.tostring(self.texture, "RGB", 1)
        width = self.texture.get_width()
        height = self.texture.get_height()
        glBindTexture(GL_TEXTURE_2D, self.texID)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, 3, width, height,0,GL_RGB, GL_UNSIGNED_BYTE, textureData)