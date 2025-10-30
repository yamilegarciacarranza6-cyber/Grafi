import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Establecer color de fondo
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1.0, 0.1, 50.0)  # Configuración de perspectiva
    glMatrixMode(GL_MODELVIEW)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -5)  # Mover la cámara más atrás para ver ambas figuras

    # Dibujar TRIÁNGULO 
    glPushMatrix()
    glTranslatef(-1.0, 0.0, 0.0)  # Mover a la izquierda
    
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)  # Rojo
    glVertex3f(-1.0, -1.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)  # Verde
    glVertex3f(1.0, -1.0, 0.0)
    glColor3f(0.0, 0.0, 1.0)  # Azul
    glVertex3f(0.0, 1.0, 0.0)
    glEnd()
    
    glPopMatrix()

    # Dibujar CUADRADO 
    glPushMatrix()
    glTranslatef(1.0, 0.0, 0.0)  # Mover a la derecha
    
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
    
    glPopMatrix()

    glutSwapBuffers()

def main():
    # Inicializar GLUT
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(1000, 800)
    glutCreateWindow(b"Triangulo y Cuadrado con GLUT y Python")

    init()
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()