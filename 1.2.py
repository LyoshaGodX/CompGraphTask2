import pygame
import sys
import numpy as np


def draw_lines_and_points(lines):
    pygame.init()

    width, height = 1000, 1000
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Lines and Points")

    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)

    offset_x, offset_y = -500, -570

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
            angle = calculate_angle(line)
            text = font.render(f"{angle:.2f}", True, red)
            mid = find_midpoint(line)
            screen.blit(text, (mid[0] + width // 2 + offset_x, mid[1] + height // 2 + offset_y - 20))

        pygame.display.flip()

    pygame.quit()
    sys.exit()


def transform_matrix(matrix, transformation_matrix):
    transformed_matrix = []

    for point in matrix:
        point = np.dot(transformation_matrix, np.array(point + [1]))[:2]
        transformed_matrix.append([int(point[0]), int(point[1])])

    return transformed_matrix


def calculate_slope(line):
    x1, y1 = line[0]
    x2, y2 = line[1]

    if x2 - x1 == 0:
        return float('inf')

    slope = (y2 - y1) / (x2 - x1)
    return slope


def calculate_angle(line):
    slope = calculate_slope(line)
    angle_rad = np.arctan(slope)
    angle_deg = np.degrees(angle_rad)
    return angle_deg


def find_midpoint(line):
    x_mid = (line[0][0] + line[1][0]) // 2
    y_mid = (line[0][1] + line[1][1]) // 2
    return [x_mid, y_mid]


L = [[50, 100], [250, 200], [50, 200], [250, 300]]
T = [[1, 2], [3, 1]]

L_transformed = transform_matrix(np.array(L), np.array(T))

draw_lines_and_points([L[:2], L[2:], L_transformed[:2], L_transformed[2:]])

