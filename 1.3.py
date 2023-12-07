import pygame
import sys
import numpy as np


def draw_lines_and_points(lines):
    pygame.init()

    width, height = 1100, 1500
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Lines and Points")

    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)

    offset_x, offset_y = width // 2 - 200, height // 2 - 200

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(white)

        for line in lines:
            centered_line = [
                [point[0] + offset_x, point[1] + offset_y]
                for point in line
            ]
            pygame.draw.line(screen, black, (centered_line[0][0], centered_line[0][1]),
                             (centered_line[1][0], centered_line[1][1]))

            font = pygame.font.Font(None, 20)

            for i, point in enumerate(line):
                text = font.render(f"({point[0]}, {point[1]})", True, red)
                screen.blit(text, (centered_line[i][0] + 5, centered_line[i][1]))

        pygame.display.flip()

    pygame.quit()
    sys.exit()


def transform_matrix(matrix, transformation_matrix):
    transformed_matrix = []

    for point in matrix:
        point = np.dot(transformation_matrix, np.array(point + [1]))[:2]
        transformed_matrix.append([int(point[0]), int(point[1])])

    return transformed_matrix


L = [[-1 / 2, 3 / 2], [3, -2], [-1, -1], [3, 5 / 3]]
T = [[1, 2], [1, -3]]

L_transformed = transform_matrix(np.array(L) * 100, np.array(T))

draw_lines_and_points([np.array(L[:2]) * 100, np.array(L[2:]) * 100, L_transformed[:2], L_transformed[2:]])
