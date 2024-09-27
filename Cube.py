import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Initialize Pygame
pygame.init()

# Set up display
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
pygame.display.set_caption("03 Lab 1 - [Naorence B. Dacullo]")

# Set up perspective
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0, 0, -5)

# Function to draw a wireframe cube
def draw_cube():
    vertices = [
        [1, 1, 1],
        [1, 1, -1],
        [1, -1, -1],
        [1, -1, 1],
        [-1, 1, 1],
        [-1, -1, -1],
        [-1, -1, 1],
        [-1, 1, -1]
    ]

    edges = [
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 0),
        (4, 7),
        (7, 5),
        (5, 6),
        (6, 4),
        (3, 6),
        (0, 4),
        (2, 5),
        (1, 7)
    ]

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glRotatef(1, 1, 1, 1)  # Rotate the cube
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear the buffers
    draw_cube()  # Draw the cube
    pygame.display.flip()  # Update the display
    pygame.time.wait(15)  # Pause for a moment


MEAW 
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Step 7: Initialize pygame
pygame.init()

# Step 8: Set up the application window
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

# Step 9: Set the window's caption
pygame.display.set_caption("03 Lab 1 - [Your Full Name]")

# Step 10: Set up the viewer's perspective
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0, 0, -5)

# Step 11: Initialize the event loop
def draw_cube():
    vertices = [
        [1, 1, 1],
        [1, 1, -1],
        [1, -1, -1],
        [1, -1, 1],
        [-1, 1, 1],
        [-1, -1, -1],
        [-1, -1, 1],
        [-1, 1, -1],
    ]

    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 7), (7, 5), (5, 6), (6, 4),
        (3, 6), (0, 4), (2, 5), (1, 7),
    ]

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Step 16: Rotate the cube
    glRotatef(1, 1, 1, 1)

    # Step 17: Clear the screen and draw the cube
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_cube()

    pygame.display.flip()
    pygame.time.wait(15)

