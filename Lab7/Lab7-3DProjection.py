# Import a library of functions called 'pygame'
import pygame
from math import pi
import numpy as np
from math import sin, cos, radians

class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y

class Point3D:
	def __init__(self,x,y,z):
		self.x = x
		self.y = y
		self.z = z
		
class Line3D():
	
	def __init__(self, start, end):
		self.start = start
		self.end = end

def loadOBJ(filename):
	
	vertices = []
	indices = []
	lines = []
	
	f = open(filename, "r")
	for line in f:
		t = str.split(line)
		if not t:
			continue
		if t[0] == "v":
			vertices.append(Point3D(float(t[1]),float(t[2]),float(t[3])))
			
		if t[0] == "f":
			for i in range(1,len(t) - 1):
				index1 = int(str.split(t[i],"/")[0])
				index2 = int(str.split(t[i+1],"/")[0])
				indices.append((index1,index2))
			
	f.close()
	
	#Add faces as lines
	for index_pair in indices:
		index1 = index_pair[0]
		index2 = index_pair[1]
		lines.append(Line3D(vertices[index1 - 1],vertices[index2 - 1]))
		
	#Find duplicates
	duplicates = []
	for i in range(len(lines)):
		for j in range(i+1, len(lines)):
			line1 = lines[i]
			line2 = lines[j]
			
			# Case 1 -> Starts match
			if line1.start.x == line2.start.x and line1.start.y == line2.start.y and line1.start.z == line2.start.z:
				if line1.end.x == line2.end.x and line1.end.y == line2.end.y and line1.end.z == line2.end.z:
					duplicates.append(j)
			# Case 2 -> Start matches end
			if line1.start.x == line2.end.x and line1.start.y == line2.end.y and line1.start.z == line2.end.z:
				if line1.end.x == line2.start.x and line1.end.y == line2.start.y and line1.end.z == line2.start.z:
					duplicates.append(j)
					
	duplicates = list(set(duplicates))
	duplicates.sort()
	duplicates = duplicates[::-1]
	
	#Remove duplicates
	for j in range(len(duplicates)):
		del lines[duplicates[j]]
	
	return lines

def loadHouse():
    house = []
    #Floor
    house.append(Line3D(Point3D(-5, 0, -5), Point3D(5, 0, -5)))
    house.append(Line3D(Point3D(5, 0, -5), Point3D(5, 0, 5)))
    house.append(Line3D(Point3D(5, 0, 5), Point3D(-5, 0, 5)))
    house.append(Line3D(Point3D(-5, 0, 5), Point3D(-5, 0, -5)))
    #Ceiling
    house.append(Line3D(Point3D(-5, 5, -5), Point3D(5, 5, -5)))
    house.append(Line3D(Point3D(5, 5, -5), Point3D(5, 5, 5)))
    house.append(Line3D(Point3D(5, 5, 5), Point3D(-5, 5, 5)))
    house.append(Line3D(Point3D(-5, 5, 5), Point3D(-5, 5, -5)))
    #Walls
    house.append(Line3D(Point3D(-5, 0, -5), Point3D(-5, 5, -5)))
    house.append(Line3D(Point3D(5, 0, -5), Point3D(5, 5, -5)))
    house.append(Line3D(Point3D(5, 0, 5), Point3D(5, 5, 5)))
    house.append(Line3D(Point3D(-5, 0, 5), Point3D(-5, 5, 5)))
    #Door
    house.append(Line3D(Point3D(-1, 0, 5), Point3D(-1, 3, 5)))
    house.append(Line3D(Point3D(-1, 3, 5), Point3D(1, 3, 5)))
    house.append(Line3D(Point3D(1, 3, 5), Point3D(1, 0, 5)))
    #Roof
    house.append(Line3D(Point3D(-5, 5, -5), Point3D(0, 8, -5)))
    house.append(Line3D(Point3D(0, 8, -5), Point3D(5, 5, -5)))
    house.append(Line3D(Point3D(-5, 5, 5), Point3D(0, 8, 5)))
    house.append(Line3D(Point3D(0, 8, 5), Point3D(5, 5, 5)))
    house.append(Line3D(Point3D(0, 8, 5), Point3D(0, 8, -5)))
	
    return house

def loadCar():
    car = []
    #Front Side
    car.append(Line3D(Point3D(-3, 2, 2), Point3D(-2, 3, 2)))
    car.append(Line3D(Point3D(-2, 3, 2), Point3D(2, 3, 2)))
    car.append(Line3D(Point3D(2, 3, 2), Point3D(3, 2, 2)))
    car.append(Line3D(Point3D(3, 2, 2), Point3D(3, 1, 2)))
    car.append(Line3D(Point3D(3, 1, 2), Point3D(-3, 1, 2)))
    car.append(Line3D(Point3D(-3, 1, 2), Point3D(-3, 2, 2)))

    #Back Side
    car.append(Line3D(Point3D(-3, 2, -2), Point3D(-2, 3, -2)))
    car.append(Line3D(Point3D(-2, 3, -2), Point3D(2, 3, -2)))
    car.append(Line3D(Point3D(2, 3, -2), Point3D(3, 2, -2)))
    car.append(Line3D(Point3D(3, 2, -2), Point3D(3, 1, -2)))
    car.append(Line3D(Point3D(3, 1, -2), Point3D(-3, 1, -2)))
    car.append(Line3D(Point3D(-3, 1, -2), Point3D(-3, 2, -2)))
    
    #Connectors
    car.append(Line3D(Point3D(-3, 2, 2), Point3D(-3, 2, -2)))
    car.append(Line3D(Point3D(-2, 3, 2), Point3D(-2, 3, -2)))
    car.append(Line3D(Point3D(2, 3, 2), Point3D(2, 3, -2)))
    car.append(Line3D(Point3D(3, 2, 2), Point3D(3, 2, -2)))
    car.append(Line3D(Point3D(3, 1, 2), Point3D(3, 1, -2)))
    car.append(Line3D(Point3D(-3, 1, 2), Point3D(-3, 1, -2)))

    return car

def loadTire():
    tire = []
    #Front Side
    tire.append(Line3D(Point3D(-1, .5, .5), Point3D(-.5, 1, .5)))
    tire.append(Line3D(Point3D(-.5, 1, .5), Point3D(.5, 1, .5)))
    tire.append(Line3D(Point3D(.5, 1, .5), Point3D(1, .5, .5)))
    tire.append(Line3D(Point3D(1, .5, .5), Point3D(1, -.5, .5)))
    tire.append(Line3D(Point3D(1, -.5, .5), Point3D(.5, -1, .5)))
    tire.append(Line3D(Point3D(.5, -1, .5), Point3D(-.5, -1, .5)))
    tire.append(Line3D(Point3D(-.5, -1, .5), Point3D(-1, -.5, .5)))
    tire.append(Line3D(Point3D(-1, -.5, .5), Point3D(-1, .5, .5)))

    #Back Side
    tire.append(Line3D(Point3D(-1, .5, -.5), Point3D(-.5, 1, -.5)))
    tire.append(Line3D(Point3D(-.5, 1, -.5), Point3D(.5, 1, -.5)))
    tire.append(Line3D(Point3D(.5, 1, -.5), Point3D(1, .5, -.5)))
    tire.append(Line3D(Point3D(1, .5, -.5), Point3D(1, -.5, -.5)))
    tire.append(Line3D(Point3D(1, -.5, -.5), Point3D(.5, -1, -.5)))
    tire.append(Line3D(Point3D(.5, -1, -.5), Point3D(-.5, -1, -.5)))
    tire.append(Line3D(Point3D(-.5, -1, -.5), Point3D(-1, -.5, -.5)))
    tire.append(Line3D(Point3D(-1, -.5, -.5), Point3D(-1, .5, -.5)))

    #Connectors
    tire.append(Line3D(Point3D(-1, .5, .5), Point3D(-1, .5, -.5)))
    tire.append(Line3D(Point3D(-.5, 1, .5), Point3D(-.5, 1, -.5)))
    tire.append(Line3D(Point3D(.5, 1, .5), Point3D(.5, 1, -.5)))
    tire.append(Line3D(Point3D(1, .5, .5), Point3D(1, .5, -.5)))
    tire.append(Line3D(Point3D(1, -.5, .5), Point3D(1, -.5, -.5)))
    tire.append(Line3D(Point3D(.5, -1, .5), Point3D(.5, -1, -.5)))
    tire.append(Line3D(Point3D(-.5, -1, .5), Point3D(-.5, -1, -.5)))
    tire.append(Line3D(Point3D(-1, -.5, .5), Point3D(-1, -.5, -.5)))
    
    return tire

#Matrix Helpers
def translate(tx, ty, tz):
    M = np.identity(4)
    M[0,3], M[1,3], M[2,3] = tx, ty, tz
    return M

def rotate_y(angle):
    c, s = cos(angle), sin(angle)
    M = np.identity(4)
    M[0,0], M[0,2], M[2,0], M[2,2] = c, s, -s, c
    return M

def rotate_x(angle):
    c, s = cos(angle), sin(angle)
    M = np.identity(4)
    M[1,1], M[1,2], M[2,1], M[2,2] = c, -s, s, c
    return M

def rotate_z(angle):
    c, s = cos(angle), sin(angle)
    M = np.identity(4)
    M[0,0], M[0,1], M[1,0], M[1,1] = c, -s, s, c
    return M

def perspective(fov, aspect, n, f):
    t = np.tan(fov/2) * n
    r = t * aspect
    M = np.zeros((4,4))
    M[0,0] = n/r
    M[1,1] = n/t
    M[2,2] = -(f+n)/(f-n)
    M[2,3] = -(2*f*n)/(f-n)
    M[3,2] = -1
    return M

def look_at(eye, center, up):
    f = (center - eye)
    f /= np.linalg.norm(f)
    s = np.cross(f, up)
    s /= np.linalg.norm(s)
    u = np.cross(s, f)
    M = np.identity(4)
    M[0,:3], M[1,:3], M[2,:3] = s, u, -f
    T = np.identity(4)
    T[:3,3] = -eye
    return M @ T

def viewport(width, height):
    M = np.identity(4)
    M[0,0] = width/2
    M[1,1] = -height/2
    M[0,3] = width/2
    M[1,3] = height/2
    return M

#Transform Helpers
def apply_transform(M, p):
    v = np.array([p.x, p.y, p.z, 1])
    r = M @ v
    return Point3D(r[0]/r[3], r[1]/r[3], r[2]/r[3]) if r[3] != 0 else Point3D(r[0], r[1], r[2])

def transform_lines(lines, M):
    out = []
    for l in lines:
        out.append(Line3D(apply_transform(M, l.start), apply_transform(M, l.end)))
    return out

def draw_model(model, worldMatrix, color, screen, view, proj, vp, size):
	for line in model:
		# Convert to homogeneous coordinates
		p1 = np.array([line.start.x, line.start.y, line.start.z, 1])
		p2 = np.array([line.end.x, line.end.y, line.end.z, 1])

		# World → Camera
		p1Cam = view @ worldMatrix @ p1
		p2Cam = view @ worldMatrix @ p2

		# Near plane clipping
		if p1Cam[2] <= 0 or p2Cam[2] <= 0:
			continue

		# Camera → Clip space
		p1Clip = proj @ p1Cam
		p2Clip = proj @ p2Cam

		# Perspective divide → NDC
		p1NDC = p1Clip[:3] / p1Clip[3]
		p2NDC = p2Clip[:3] / p2Clip[3]

		# Simple clip rejection
		if np.any(np.abs(p1NDC) > 1.5) and np.any(np.abs(p2NDC) > 1.5):
			continue

		# NDC → Screen (viewport transform)
		p1Screen = vp @ np.array([p1NDC[0], p1NDC[1], p1NDC[2], 1])
		p2Screen = vp @ np.array([p2NDC[0], p2NDC[1], p2NDC[2], 1])

		# Draw 2D line (invert y-axis)
		pygame.draw.line(
			screen,
			color,
			(p1Screen[0], size[1] - p1Screen[1]),
			(p2Screen[0], size[1] - p2Screen[1])
		)

# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

# Set the height and width of the screen
size = [512, 512]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Shape Drawing")
 
#Set needed variables
done = False
clock = pygame.time.Clock()
start = Point(0.0,0.0)
end = Point(0.0,0.0)
linelist = loadHouse()
# Camera
eye = np.array([0.0, 3.0, 20.0])
yaw, pitch = 0.0, 0.0
up = np.array([0.0,1.0,0.0])
# Projection + viewport
proj = perspective(radians(60), 1.0, 1.0, 100.0)
vp = viewport(512,512)

time = 0.0

houses = [loadHouse() for _ in range(5)]
car = loadCar()
tire = loadTire()

#Loop until the user clicks the close button.
while not done:
 
	# This limits the while loop to a max of 100 times per second.
	# Leave this out and we will use all CPU we can.
	#clock.tick(100)
	dt = clock.tick(60)/1000.0
	time += dt

	# Clear the screen and set the screen background
	screen.fill(BLACK)

	#Controller Code#
	#####################################################################

	for event in pygame.event.get():
		if event.type == pygame.QUIT: # If user clicked close
			done=True
			
	pressed = pygame.key.get_pressed()
	speed = 10*dt
	rotSpeed = 1.5*dt
	
	forward = np.array([-sin(yaw), 0, -cos(yaw)])
	right = np.array([cos(yaw), 0, -sin(yaw)])

	if pressed[pygame.K_w]:
		eye += forward * speed
	if pressed[pygame.K_a]:
		eye -= right * speed
	if pressed[pygame.K_s]:
		eye -= forward * speed
	if pressed[pygame.K_d]:
		eye += right * speed
	if pressed[pygame.K_q]:
		yaw += rotSpeed
	if pressed[pygame.K_e]:
		yaw -= rotSpeed
	if pressed[pygame.K_r]:
		eye[1] += speed
	if pressed[pygame.K_f]:
		eye[1] -= speed
	if pressed[pygame.K_h]:
		eye = np.array([0.0, 3.0, 20.0])
		yaw, pitch = 0.0, 0.0
		up = np.array([0.0,1.0,0.0])
		time = 0.0
		
		
	center = eye + np.array([sin(yaw), 0, cos(yaw)])
	view = look_at(eye, center, up)

	#Viewer Code#
	#####################################################################

	for s in linelist:
		for i, h in enumerate(houses):
			worldFront = translate(i * 20 - 40, 0, 0)
			draw_model(h, worldFront, BLUE, screen, view, proj, vp, size)
			worldBack = translate(i * 20 - 40, 0, -30)
			draw_model(h, worldBack, BLUE, screen, view, proj, vp, size)

		carSpeed = 2.0
		tireRadius = 1.0
		carX = carSpeed * time
		rotationScale = 180 / pi
		wheelRotation = -(carSpeed * time / tireRadius) * rotationScale
		carWorld = translate(carX, 0, -15)

		draw_model(car, carWorld, RED, screen, view, proj, vp, size)
		tireOffsets = [
			(-2, 1, 2),   # front-left
			(2, 1, 2),    # front-right
			(-2, 1, -2),  # back-left
			(2, 1, -2)    # back-right
		]
		for tx, ty, tz in tireOffsets:
			tireWorld = carWorld @ translate(tx, ty, tz) @ rotate_z(radians(wheelRotation))
			draw_model(tire, tireWorld, GREEN, screen, view, proj, vp, size)
				
		# This MUST happen after all the other drawing commands.
		pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()