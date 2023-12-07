import pygame
import sys
import numpy as np


def draw_triangles(triangles):
    pygame.init()

    width, height = 900, 500
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Triangle Drawing")

    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)

    offset_x, offset_y = width // 2 - 700, height // 2 - 270

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(white)

        for triangle in triangles:
            pygame.draw.polygon(screen, black, [(p[0] + offset_x, p[1] + offset_y) for p in triangle], 2)

            font = pygame.font.Font(None, 20)

            for i, point in enumerate(triangle):
                text = font.render(f"({point[0]}, {point[1]})", True, red)
                screen.blit(text, (point[0] + offset_x + 5, point[1] + offset_y))

        pygame.display.flip()

    pygame.quit()
    sys.exit()


def transform_matrix(matrix, transformation_matrix):
    transformed_matrix = []

    for point in matrix:
        point = np.dot(transformation_matrix, np.array(point + [1]))[:2]
        transformed_matrix.append([int(point[0]), int(point[1])])

    return transformed_matrix


L = [[500, 100], [500, 200], [300, 200]]
T = [[2, 0], [0, 2]]

L_transformed = transform_matrix(np.array(L), np.array(T))

draw_triangles([L, L_transformed])
