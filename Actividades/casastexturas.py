import glfw
from OpenGL.GL import *
from OpenGL.GLU import gluPerspective, gluLookAt
from PIL import Image
import sys

# Texturas para diferentes partes de la casa
tex_pared = None
tex_techo = None
tex_suelo = None
tex_puerta = None
tex_ventana = None
tex_pasto = None

def load_texture(path):
    """Cargar una textura desde un archivo"""
    try:
        img = Image.open(path).convert("RGB")
        img = img.transpose(Image.FLIP_TOP_BOTTOM)
        img_data = img.tobytes()

        texture_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture_id)

        # Configurar parámetros de textura
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)

        # Cargar datos de textura
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.width, img.height, 0, 
                    GL_RGB, GL_UNSIGNED_BYTE, img_data)
        glGenerateMipmap(GL_TEXTURE_2D)

        glBindTexture(GL_TEXTURE_2D, 0)
        return texture_id
    except Exception as e:
        print(f"Error cargando textura {path}: {e}")
        return None

def init():
    """Configuración inicial de OpenGL"""
    global tex_pared, tex_techo, tex_suelo, tex_puerta, tex_ventana, tex_pasto
    
    glClearColor(0.5, 0.8, 1.0, 1.0)  # Fondo azul cielo
    glEnable(GL_DEPTH_TEST)           # Activar prueba de profundidad
    glEnable(GL_TEXTURE_2D)           # Activar texturas
    
    # Configurar iluminación para mejor visualización de texturas
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    # Configuración de la perspectiva
    glMatrixMode(GL_PROJECTION)
    gluPerspective(60, 1, 1, 100.0)
    glMatrixMode(GL_MODELVIEW)

    # Cargar texturas (usa nombres de archivo genéricos - cambia según tus imágenes)
    # Si no tienes estas imágenes, puedes crearlas o descargar algunas de ejemplo
    tex_pared = load_texture("pared.jepg") or create_default_texture((150, 200, 150))
    tex_techo = load_texture("techo.jepg") or create_default_texture((180, 100, 100))
    tex_suelo = load_texture("suelo.jepg") or create_default_texture((120, 120, 120))
    tex_puerta = load_texture("puerta.jepg") or create_default_texture((150, 100, 50))
    tex_ventana = load_texture("ventana.jepg") or create_default_texture((200, 230, 255))
    tex_pasto = load_texture("pasto.jepg") or create_default_texture((50, 150, 50))

def create_default_texture(color):
    """Crear una textura sólida de un color específico"""
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    
    # Crear una imagen de 64x64 con el color especificado
    size = 64
    data = bytes()
    for i in range(size * size):
        data += bytes([color[0], color[1], color[2]])
    
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, size, size, 0, 
                GL_RGB, GL_UNSIGNED_BYTE, data)
    
    glBindTexture(GL_TEXTURE_2D, 0)
    return texture_id

def draw_cube():
    """Dibuja el cubo (base de la casa) con texturas"""
    # Cara frontal con puerta
    glBindTexture(GL_TEXTURE_2D, tex_pared)
    glBegin(GL_QUADS)
    
    # Cara frontal (sin puerta por ahora)
    glTexCoord2f(0.0, 0.0); glVertex3f(-1, 0, 1)
    glTexCoord2f(2.0, 0.0); glVertex3f(1, 0, 1)
    glTexCoord2f(2.0, 2.5); glVertex3f(1, 5, 1)
    glTexCoord2f(0.0, 2.5); glVertex3f(-1, 5, 1)
    glEnd()
    
    # Cara trasera
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0); glVertex3f(-1, 0, -1)
    glTexCoord2f(2.0, 0.0); glVertex3f(1, 0, -1)
    glTexCoord2f(2.0, 2.5); glVertex3f(1, 5, -1)
    glTexCoord2f(0.0, 2.5); glVertex3f(-1, 5, -1)
    glEnd()
    
    # Cara izquierda con ventana
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0); glVertex3f(-1, 0, -1)
    glTexCoord2f(1.0, 0.0); glVertex3f(-1, 0, 1)
    glTexCoord2f(1.0, 2.5); glVertex3f(-1, 5, 1)
    glTexCoord2f(0.0, 2.5); glVertex3f(-1, 5, -1)
    glEnd()
    
    # Cara derecha con ventana
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0); glVertex3f(1, 0, -1)
    glTexCoord2f(1.0, 0.0); glVertex3f(1, 0, 1)
    glTexCoord2f(1.0, 2.5); glVertex3f(1, 5, 1)
    glTexCoord2f(0.0, 2.5); glVertex3f(1, 5, -1)
    glEnd()
    
    # Techo (parte superior del cubo)
    glBindTexture(GL_TEXTURE_2D, tex_suelo)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0); glVertex3f(-1, 5, -1)
    glTexCoord2f(1.0, 0.0); glVertex3f(1, 5, -1)
    glTexCoord2f(1.0, 1.0); glVertex3f(1, 5, 1)
    glTexCoord2f(0.0, 1.0); glVertex3f(-1, 5, 1)
    glEnd()
    
    # Suelo (parte inferior del cubo)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0); glVertex3f(-1, 0, -1)
    glTexCoord2f(1.0, 0.0); glVertex3f(1, 0, -1)
    glTexCoord2f(1.0, 1.0); glVertex3f(1, 0, 1)
    glTexCoord2f(0.0, 1.0); glVertex3f(-1, 0, 1)
    glEnd()
    
    # Dibujar puerta en la cara frontal
    glBindTexture(GL_TEXTURE_2D, tex_puerta)
    glPushMatrix()
    glTranslatef(0, 0, 1.01)  # Un poco adelante para evitar z-fighting
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0); glVertex3f(-0.3, 0, 0)
    glTexCoord2f(1.0, 0.0); glVertex3f(0.3, 0, 0)
    glTexCoord2f(1.0, 1.5); glVertex3f(0.3, 3, 0)
    glTexCoord2f(0.0, 1.5); glVertex3f(-0.3, 3, 0)
    glEnd()
    glPopMatrix()
    
    # Dibujar ventanas en las caras laterales
    glBindTexture(GL_TEXTURE_2D, tex_ventana)
    
    # Ventana izquierda
    glPushMatrix()
    glTranslatef(-1.01, 0, 0)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0); glVertex3f(0, 2, -0.3)
    glTexCoord2f(1.0, 0.0); glVertex3f(0, 2, 0.3)
    glTexCoord2f(1.0, 1.0); glVertex3f(0, 3.5, 0.3)
    glTexCoord2f(0.0, 1.0); glVertex3f(0, 3.5, -0.3)
    glEnd()
    glPopMatrix()
    
    # Ventana derecha
    glPushMatrix()
    glTranslatef(1.01, 0, 0)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0); glVertex3f(0, 2, 0.3)
    glTexCoord2f(1.0, 0.0); glVertex3f(0, 2, -0.3)
    glTexCoord2f(1.0, 1.0); glVertex3f(0, 3.5, -0.3)
    glTexCoord2f(0.0, 1.0); glVertex3f(0, 3.5, 0.3)
    glEnd()
    glPopMatrix()
    
    glBindTexture(GL_TEXTURE_2D, 0)

def draw_roof():
    """Dibuja el techo (pirámide) con textura"""
    glBindTexture(GL_TEXTURE_2D, tex_techo)
    glBegin(GL_TRIANGLES)
    
    # Cara frontal
    glTexCoord2f(0.5, 1.0); glVertex3f(0, 9, 0)
    glTexCoord2f(0.0, 0.0); glVertex3f(-1, 5, 1)
    glTexCoord2f(1.0, 0.0); glVertex3f(1, 5, 1)
    
    # Cara trasera
    glTexCoord2f(0.5, 1.0); glVertex3f(0, 9, 0)
    glTexCoord2f(0.0, 0.0); glVertex3f(1, 5, -1)
    glTexCoord2f(1.0, 0.0); glVertex3f(-1, 5, -1)
    
    # Cara izquierda
    glTexCoord2f(0.5, 1.0); glVertex3f(0, 9, 0)
    glTexCoord2f(0.0, 0.0); glVertex3f(-1, 5, -1)
    glTexCoord2f(1.0, 0.0); glVertex3f(-1, 5, 1)
    
    # Cara derecha
    glTexCoord2f(0.5, 1.0); glVertex3f(0, 9, 0)
    glTexCoord2f(0.0, 0.0); glVertex3f(1, 5, 1)
    glTexCoord2f(1.0, 0.0); glVertex3f(1, 5, -1)
    
    glEnd()
    glBindTexture(GL_TEXTURE_2D, 0)

def draw_ground():
    """Dibuja un plano para representar el suelo con textura de pasto"""
    glBindTexture(GL_TEXTURE_2D, tex_pasto)
    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)  # Color blanco para textura completa
    
    # Coordenadas del plano con coordenadas de textura
    glTexCoord2f(0.0, 0.0); glVertex3f(-20, 0, 20)
    glTexCoord2f(10.0, 0.0); glVertex3f(20, 0, 20)
    glTexCoord2f(10.0, 10.0); glVertex3f(20, 0, -20)
    glTexCoord2f(0.0, 10.0); glVertex3f(-20, 0, -20)
    glEnd()
    
    glBindTexture(GL_TEXTURE_2D, 0)

def draw_house():
    """Dibuja una casa (base + techo)"""
    draw_cube()  # Base de la casa con texturas
    draw_roof()  # Techo con textura

def draw_scene():
    """Dibuja toda la escena con 4 casas"""
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Configuración de la cámara
    gluLookAt(15, 15, 20,  # Posición de la cámara
              0, 2, 0,      # Punto al que mira (centro de la escena)
              0, 1, 0)      # Vector hacia arriba
    
    # Configurar luz
    glLightfv(GL_LIGHT0, GL_POSITION, [10, 20, 10, 1])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.3, 0.3, 0.3, 1.0])

    # Dibujar el suelo
    draw_ground()

    # Dibujar las casas en diferentes posiciones
    positions = [
        (-8, 0, -8),  # Casa 1
        (8, 0, -8),   # Casa 2
        (-8, 0, 8),   # Casa 3
        (8, 0, 8),    # Casa 4
    ]
    
    # Diferentes rotaciones para variedad
    rotations = [0, 45, 90, 135]
    
    for i, pos in enumerate(positions):
        glPushMatrix()
        glTranslatef(pos[0], pos[1], pos[2])  # Mover a posición
        glRotatef(rotations[i], 0, 1, 0)     # Rotar para variedad
        glScalef(0.8, 0.8, 0.8)              # Escalar un poco
        draw_house()                         # Dibujar la casa
        glPopMatrix()

    glfw.swap_buffers(window)

def main():
    global window

    # Inicializar GLFW
    if not glfw.init():
        sys.exit()
    
    # Crear ventana de GLFW
    width, height = 1000, 800
    window = glfw.create_window(width, height, "4 Casas 3D con Texturas", None, None)
    if not window:
        glfw.terminate()
        sys.exit()

    glfw.make_context_current(window)
    glViewport(0, 0, width, height)
    init()

    # Bucle principal
    while not glfw.window_should_close(window):
        draw_scene()
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()