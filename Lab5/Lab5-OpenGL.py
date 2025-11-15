import sys, os, math

try:
    from OpenGL.GLUT import *
    from OpenGL.GL import *
    from OpenGL.GLU import *
    from OpenGL.GL import glOrtho
    from OpenGL.GLU import gluPerspective
    from OpenGL.GL import glRotated
    from OpenGL.GL import glTranslated
    from OpenGL.GL import glLoadIdentity
    from OpenGL.GL import glMatrixMode
    from OpenGL.GL import GL_MODELVIEW
    from OpenGL.GL import GL_PROJECTION
except:
    print("ERROR: PyOpenGL not installed properly. ")

DISPLAY_WIDTH = 500.0
DISPLAY_HEIGHT = 500.0
cameraX, cameraY, cameraZ = 0, -2, -20
angle = 0
projection = 'perspective'
carX = -15
wheelRotation = 0.0

def init(): 
    glClearColor (0.0, 0.0, 0.0, 0.0)
    glShadeModel (GL_FLAT)

def drawHouse ():
    glLineWidth(2.5)
    glColor3f(1.0, 0.0, 0.0)
    #Floor
    glBegin(GL_LINES)
    glVertex3f(-5.0, 0.0, -5.0)
    glVertex3f(5, 0, -5)
    glVertex3f(5, 0, -5)
    glVertex3f(5, 0, 5)
    glVertex3f(5, 0, 5)
    glVertex3f(-5, 0, 5)
    glVertex3f(-5, 0, 5)
    glVertex3f(-5, 0, -5)
    #Ceiling
    glVertex3f(-5, 5, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(5, 5, 5)
    glVertex3f(5, 5, 5)
    glVertex3f(-5, 5, 5)
    glVertex3f(-5, 5, 5)
    glVertex3f(-5, 5, -5)
    #Walls
    glVertex3f(-5, 0, -5)
    glVertex3f(-5, 5, -5)
    glVertex3f(5, 0, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(5, 0, 5)
    glVertex3f(5, 5, 5)
    glVertex3f(-5, 0, 5)
    glVertex3f(-5, 5, 5)
    #Door
    glVertex3f(-1, 0, 5)
    glVertex3f(-1, 3, 5)
    glVertex3f(-1, 3, 5)
    glVertex3f(1, 3, 5)
    glVertex3f(1, 3, 5)
    glVertex3f(1, 0, 5)
    #Roof
    glVertex3f(-5, 5, -5)
    glVertex3f(0, 8, -5)
    glVertex3f(0, 8, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(-5, 5, 5)
    glVertex3f(0, 8, 5)
    glVertex3f(0, 8, 5)
    glVertex3f(5, 5, 5)
    glVertex3f(0, 8, 5)
    glVertex3f(0, 8, -5)
    glEnd()

def drawCar():
	glLineWidth(2.5)
	glColor3f(0.0, 1.0, 0.0)
	glBegin(GL_LINES)
	#Front Side
	glVertex3f(-3, 2, 2)
	glVertex3f(-2, 3, 2)
	glVertex3f(-2, 3, 2)
	glVertex3f(2, 3, 2)
	glVertex3f(2, 3, 2)
	glVertex3f(3, 2, 2)
	glVertex3f(3, 2, 2)
	glVertex3f(3, 1, 2)
	glVertex3f(3, 1, 2)
	glVertex3f(-3, 1, 2)
	glVertex3f(-3, 1, 2)
	glVertex3f(-3, 2, 2)
	#Back Side
	glVertex3f(-3, 2, -2)
	glVertex3f(-2, 3, -2)
	glVertex3f(-2, 3, -2)
	glVertex3f(2, 3, -2)
	glVertex3f(2, 3, -2)
	glVertex3f(3, 2, -2)
	glVertex3f(3, 2, -2)
	glVertex3f(3, 1, -2)
	glVertex3f(3, 1, -2)
	glVertex3f(-3, 1, -2)
	glVertex3f(-3, 1, -2)
	glVertex3f(-3, 2, -2)
	#Connectors
	glVertex3f(-3, 2, 2)
	glVertex3f(-3, 2, -2)
	glVertex3f(-2, 3, 2)
	glVertex3f(-2, 3, -2)
	glVertex3f(2, 3, 2)
	glVertex3f(2, 3, -2)
	glVertex3f(3, 2, 2)
	glVertex3f(3, 2, -2)
	glVertex3f(3, 1, 2)
	glVertex3f(3, 1, -2)
	glVertex3f(-3, 1, 2)
	glVertex3f(-3, 1, -2)
	glEnd()
	
def drawTire():
	glLineWidth(2.5)
	glColor3f(0.0, 0.0, 1.0)
	glBegin(GL_LINES)
	#Front Side
	glVertex3f(-1, .5, .5)
	glVertex3f(-.5, 1, .5)
	glVertex3f(-.5, 1, .5)
	glVertex3f(.5, 1, .5)
	glVertex3f(.5, 1, .5)
	glVertex3f(1, .5, .5)
	glVertex3f(1, .5, .5)
	glVertex3f(1, -.5, .5)
	glVertex3f(1, -.5, .5)
	glVertex3f(.5, -1, .5)
	glVertex3f(.5, -1, .5)
	glVertex3f(-.5, -1, .5)
	glVertex3f(-.5, -1, .5)
	glVertex3f(-1, -.5, .5)
	glVertex3f(-1, -.5, .5)
	glVertex3f(-1, .5, .5)
	#Back Side
	glVertex3f(-1, .5, -.5)
	glVertex3f(-.5, 1, -.5)
	glVertex3f(-.5, 1, -.5)
	glVertex3f(.5, 1, -.5)
	glVertex3f(.5, 1, -.5)
	glVertex3f(1, .5, -.5)
	glVertex3f(1, .5, -.5)
	glVertex3f(1, -.5, -.5)
	glVertex3f(1, -.5, -.5)
	glVertex3f(.5, -1, -.5)
	glVertex3f(.5, -1, -.5)
	glVertex3f(-.5, -1, -.5)
	glVertex3f(-.5, -1, -.5)
	glVertex3f(-1, -.5, -.5)
	glVertex3f(-1, -.5, -.5)
	glVertex3f(-1, .5, -.5)
	#Connectors
	glVertex3f(-1, .5, .5)
	glVertex3f(-1, .5, -.5)
	glVertex3f(-.5, 1, .5)
	glVertex3f(-.5, 1, -.5)
	glVertex3f(.5, 1, .5)
	glVertex3f(.5, 1, -.5)
	glVertex3f(1, .5, .5)
	glVertex3f(1, .5, -.5)
	glVertex3f(1, -.5, .5)
	glVertex3f(1, -.5, -.5)
	glVertex3f(.5, -1, .5)
	glVertex3f(.5, -1, -.5)
	glVertex3f(-.5, -1, .5)
	glVertex3f(-.5, -1, -.5)
	glVertex3f(-1, -.5, .5)
	glVertex3f(-1, -.5, -.5)
	glEnd()

def display():
    glClear (GL_COLOR_BUFFER_BIT)
    glColor3f (1.0, 1.0, 1.0)
    # viewing transformation 
    
    #Your Code Here
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if projection == 'perspective':
        gluPerspective(60, DISPLAY_WIDTH/DISPLAY_HEIGHT, 1, 500)
    else:
        glOrtho(-20, 20, -20, 20, -50, 50)
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glRotated(angle, 0, 1, 0)
    glTranslated(cameraX, cameraY, cameraZ)
    
    makeNeighborhood()
    car()

    glFlush()

def makeNeighborhood():
    glPushMatrix()
    glTranslated(-7, 0, -20)
    drawHouse()
    glPopMatrix()

    glPushMatrix()
    glTranslated(7, 0, -20)
    drawHouse()
    glPopMatrix()

    glPushMatrix()
    glTranslated(22, 0, -18)
    glRotated(-15, 0, 1, 0)
    drawHouse()
    glPopMatrix()

    glPushMatrix()
    glTranslated(-22, 0, -18)
    glRotated(15, 0, 1, 0)
    drawHouse()
    glPopMatrix()

    glPushMatrix()
    glTranslated(-7, 0, 20)
    glRotated(180, 0, 1, 0)
    drawHouse()
    glPopMatrix()

    glPushMatrix()
    glTranslated(7, 0, 20)
    glRotated(180, 0, 1, 0)
    drawHouse()
    glPopMatrix()

    glPushMatrix()
    glTranslated(22, 0, 18)
    glRotated(195, 0, 1, 0)
    drawHouse()
    glPopMatrix()

    glPushMatrix()
    glTranslated(-22, 0, 18)
    glRotated(165, 0, 1, 0)
    drawHouse()
    glPopMatrix()


def car():
    global carX, wheelRotation
    glPushMatrix()
    glTranslated(carX, 0, 0)
    drawCar()
    
    for xTranslate in [-2, 2]:
        for zTranslate in [-1.5, 1.5]:
            glPushMatrix()
            glTranslated(xTranslate, 0, zTranslate)
            glRotated(wheelRotation, 0, 0, 1)
            drawTire()
            glPopMatrix()
    glPopMatrix()

def driveCar(value):
    global carX, wheelRotation
    wheelRadius = 1.0
    distancePerFrame = 0.1
    carX += distancePerFrame

    wheelRotation -= (distancePerFrame * 360) / (2 * math.pi * wheelRadius)
    glutPostRedisplay()
    glutTimerFunc(50, driveCar, 0)

def keyboard(key, x, y):
    global cameraX, cameraY, cameraZ, angle, projection, carX, wheelRotation
    step = 1
    rotationStep = 1
    rad = math.radians(angle)
    
    if key == b'\x1b':
        os._exit(0)
  
    if key == b'w': #forward
        cameraX -= step * math.sin(rad)
        cameraZ += step * math.cos(rad)
  
    #Your Code Here
    if key == b's': #backward
        cameraX += step * math.sin(rad)
        cameraZ -= step * math.cos(rad)

    if key == b'a': #left
        cameraX += step * math.cos(rad)
        cameraZ += step * math.sin(rad)
        
    if key == b'd': #right
        cameraX -= step * math.cos(rad)
        cameraZ -= step * math.sin(rad)

    if key == b'r': #up
        cameraY += -step

    if key == b'f': #down
        cameraY -= -step

    if key == b'q': #rotate left
        angle -= rotationStep

    if key == b'e': #rotate right
        angle += rotationStep

    if key == b'h':
        cameraX, cameraY, cameraZ = 0, -2, -20
        angle = 0
        carX = -15
        wheelRotation = 0.0

    if key == b'o':
        projection = 'orthographic'

    if key == b'p':
        projection = 'perspective'

    glutPostRedisplay()


glutInit(sys.argv)
glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize (int(DISPLAY_WIDTH), int(DISPLAY_HEIGHT))
glutInitWindowPosition (100, 100)
glutCreateWindow (b'OpenGL Lab')
init ()
glutDisplayFunc(display)
glutKeyboardFunc(keyboard)
glutTimerFunc(50, driveCar, 0)
glutMainLoop()
