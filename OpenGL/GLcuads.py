import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Establecer color de fondo
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1.0, 0.1, 50.0)  # Configuración de perspectiva(Acercar)
    glMatrixMode(GL_MODELVIEW)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -3)

    # Dibujar un cuadrado usando GL_QUADS
    glBegin(GL_QUADS)
    glColor3f(1.0, 0.0, 0.0)  # Rojo
    glVertex3f(-1.0, -1.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)  # Verde
    glVertex3f(1.0, -1.0, 0.0)  
    glColor3f(0.0, 0.0, 1.0)  # Azul
    glVertex3f(1.0, 1.0, 0.0)   
    glColor3f(1.0, 1.0, 0.0)  # Amarillo
    glVertex3f(-1.0, 1.0, 0.0)  
    glEnd()

    glutSwapBuffers()

def main():
    # Inicializar GLUT
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Cuadrado con GLUT y Python")

    init()
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()