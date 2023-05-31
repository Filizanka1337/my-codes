import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

# Inicjalizacja biblioteki Pygame
pygame.init()

# Ustawienie rozmiaru okna
width, height = 800, 600
screen = pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)

# Inicjalizacja OpenGL
glViewport(0, 0, width, height)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(45, width / height, 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

# Dodatkowe instrukcje czyszczenia buforów
glClearColor(0, 0, 0, 0)
glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

# Definicja wierzchołków i ścian kwadratu 4D
vertices = np.array([
    [1, -1, -1, -1],
    [1, 1, -1, -1],
    [-1, 1, -1, -1],
    [-1, -1, -1, -1],
    [1, -1, 1, -1],
    [1, 1, 1, -1],
    [-1, -1, 1, -1],
    [-1, 1, 1, -1],
    [1, -1, -1, 1],
    [1, 1, -1, 1],
    [-1, -1, -1, 1],
    [-1, 1, -1, 1],
    [1, -1, 1, 1],
    [1, 1, 1, 1],
    [-1, -1, 1, 1],
    [-1, 1, 1, 1]
], dtype=np.float32)

faces = np.array([
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [0, 1, 4, 5],
    [2, 3, 6, 7],
    [0, 3, 4, 7],
    [1, 2, 5, 6]
])

colors = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 0],
    [1, 0, 1],
    [0, 1, 1]
], dtype=np.float32)

# Główna pętla renderowania
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Czyszczenie buforów
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Ustawienie kamery
    gluLookAt(3, 3, 3, 0, 0, 0, 0, 1, 0)

    # Obroty kwadratu wokół osi X, Y, Z
    glRotatef(1, 1, 0, 0)
    glRotatef(1, 0, 1, 0)
    glRotatef(1, 0, 0, 1)

    # Rysowanie kwadratu
    glBegin(GL_QUADS)
    for face in faces:
        for vertex_id in face:
            glColor3fv(colors[vertex_id % 6])
            glVertex4fv(vertices[vertex_id])
    glEnd()

    # Aktualizacja ekranu
    pygame.display.flip()
    pygame.time.wait(10)
