import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import math

rotation = 0.0
quadric = None

def draw_eye():
    """Dibuja un ojo más realista usando múltiples esferas y mejor iluminación"""
    global quadric
    
    glPushMatrix()
    
    # --- Esfera principal (esclerótica - parte blanca del ojo) ---
    glPushMatrix()
    glColor3f(0.95, 0.95, 0.97)  # Blanco ligeramente azulado
    glTranslatef(0.8, 0, 0)
    gluSphere(quadric, 0.5, 50, 50)
    glPopMatrix()
    
    # --- Córnea (capa transparente exterior) ---
    glPushMatrix()
    glColor4f(1.0, 1.0, 1.0, 0.3)  # Semi-transparente
    glTranslatef(0.65, 0, 0)
    gluSphere(quadric, 0.52, 40, 40)
    glPopMatrix()
    
    # --- Iris (con más detalle) ---
    glPushMatrix()
    glTranslatef(0.45, 0, 0)
    
    # Base del iris
    glColor3f(0.4, 0.6, 0.8)  # Color azul/verde
    gluSphere(quadric, 0.35, 40, 40)
    
    # Patrón radial del iris
    glColor3f(0.3, 0.5, 0.7)
    for i in range(12):
        angle = i * 30
        rad = math.radians(angle)
        glPushMatrix()
        glTranslatef(math.cos(rad) * 0.15, math.sin(rad) * 0.15, 0)
        gluSphere(quadric, 0.08, 20, 20)
        glPopMatrix()
    
    # Anillo exterior del iris
    glPushMatrix()
    glColor3f(0.2, 0.3, 0.4)
    gluSphere(quadric, 0.38, 30, 30)
    glPopMatrix()
    
    glPopMatrix()
    
    # --- Pupila ---
    glPushMatrix()
    glColor3f(0.05, 0.05, 0.05)  # Negro pero no completamente
    glTranslatef(0.3, 0, 0)
    gluSphere(quadric, 0.25, 30, 30)
    glPopMatrix()
    
    # --- Reflejo en la córnea (brillo) ---
    glPushMatrix()
    glColor3f(1.0, 1.0, 1.0)
    glTranslatef(0.9, 0.15, 0.1)
    gluSphere(quadric, 0.08, 20, 20)
    glPopMatrix()
    
    # --- Segundo reflejo más pequeño ---
    glPushMatrix()
    glColor3f(1.0, 1.0, 1.0)
    glTranslatef(0.85, -0.1, 0.15)
    gluSphere(quadric, 0.04, 15, 15)
    glPopMatrix()
    
    # --- Vasos sanguíneos en la esclerótica ---
    glPushMatrix()
    glColor3f(0.8, 0.3, 0.3)
    glTranslatef(0.8, 0, 0)
    for i in range(8):
        angle = i * 45
        rad = math.radians(angle)
        glPushMatrix()
        glRotatef(angle, 0, 0, 1)
        glTranslatef(0.45, 0, 0)
        gluSphere(quadric, 0.02, 10, 10)
        glPopMatrix()
    glPopMatrix()
    
    glPopMatrix()

def setup_lighting():
    """Configura iluminación más realista"""
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_NORMALIZE)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    
    # Luz principal (más cálida)
    light_position = [2.0, 2.0, 2.0, 1.0]
    glLightfv(GL_LIGHT0, GL_POSITION, (GLfloat * 4)(*light_position))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (GLfloat * 4)(1.0, 0.95, 0.9, 1.0))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (GLfloat * 4)(0.3, 0.3, 0.3, 1.0))
    glLightfv(GL_LIGHT0, GL_SPECULAR, (GLfloat * 4)(1.0, 1.0, 1.0, 1.0))
    
    # Luz de relleno
    light1_position = [-1.0, -1.0, 1.0, 1.0]
    glLightfv(GL_LIGHT1, GL_POSITION, (GLfloat * 4)(*light1_position))
    glLightfv(GL_LIGHT1, GL_DIFFUSE, (GLfloat * 4)(0.5, 0.5, 0.6, 1.0))
    glLightfv(GL_LIGHT1, GL_AMBIENT, (GLfloat * 4)(0.1, 0.1, 0.1, 1.0))
    
    # Material specular para brillo
    glMaterialfv(GL_FRONT, GL_SPECULAR, (GLfloat * 4)(0.5, 0.5, 0.5, 1.0))
    glMaterialf(GL_FRONT, GL_SHININESS, 50.0)

def main():
    global rotation, quadric

    if not glfw.init():
        print("No se pudo inicializar GLFW")
        return

    window = glfw.create_window(800, 600, "Ojo Realista 3D", None, None)
    if not window:
        glfw.terminate()
        print("No se pudo crear la ventana")
        return

    glfw.make_context_current(window)
    glfw.swap_interval(1)

    quadric = gluNewQuadric()
    gluQuadricNormals(quadric, GLU_SMOOTH)
    gluQuadricTexture(quadric, GL_TRUE)

    glClearColor(0.2, 0.2, 0.3, 1.0)  # Fondo más oscuro para resaltar
    setup_lighting()

    width, height = glfw.get_framebuffer_size(window)
    glViewport(0, 0, width, height)

    while not glfw.window_should_close(window):
        width, height = glfw.get_framebuffer_size(window)
        aspect = width / height if height != 0 else 1
        glViewport(0, 0, width, height)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, aspect, 0.1, 100.0)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5.0)

        # Rotación más lenta para apreciar detalles
        rotation += 0.3
        glRotatef(rotation, 0, 1, 0)
        
        # Inclinar ligeramente para mejor perspectiva
        glRotatef(15, 1, 0, 0)

        draw_eye()

        glfw.swap_buffers(window)
        glfw.poll_events()

    if quadric:
        gluDeleteQuadric(quadric)
    glfw.terminate()

if __name__ == "__main__":
    main()