import pygame
import sys
import numpy as np


def draw_lines_and_points(lines, points):
    pygame.init()

    width, height = 1000, 1000
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Lines and Points")

    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)

    offset_x, offset_y = -400, -500

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(white)

        for line in lines:
            centered_line = [
                [point[0] + width // 2 + offset_x, point[1] + height // 2 + offset_y]
                for point in line
            ]
            pygame.draw.line(screen, black, (centered_line[0][0], centered_line[0][1]),
                             (centered_line[1][0], centered_line[1][1]))

            font = pygame.font.Font(None, 20)
            for i, point in enumerate(line):
                text = font.render(f"({point[0] }, {point[1]})", True, red)
                screen.blit(text, (centered_line[i][0] + 5, centered_line[i][1]))

        for point in points:
            centered_point = [point[0] + width // 2 + offset_x, point[1] + height // 2 + offset_y]
            pygame.draw.circle(screen, red, (centered_point[0], centered_point[1]), 5)

            font = pygame.font.Font(None, 20)
            text = font.render(f"({point[0]}, {point[1]})", True, red)
            screen.blit(text, (centered_point[0] + 5, centered_point[1]))

        pygame.display.flip()

    pygame.quit()
    sys.exit()


def transform_line(line, transformation_matrix):
    transformed_line = []

    for point in line:
        point = np.dot(transformation_matrix, np.array(point + [1]))[:2]
        transformed_line.append([int(point[0]), int(point[1])])

    return transformed_line


def find_midpoint(line):
    x_mid = (line[0][0] + line[1][0]) // 2
    y_mid = (line[0][1] + line[1][1]) // 2
    return [x_mid, y_mid]


L = [[0, 100], [200, 300]]
T = [[1, 2], [3, 1]]


L_transformed = transform_line(np.array(L), np.array(T))

draw_lines_and_points([L, L_transformed], [find_midpoint(L), find_midpoint(L_transformed)])
