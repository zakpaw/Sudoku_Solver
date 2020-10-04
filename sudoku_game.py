import solver
import random
import pygame
import pandas as pd


pygame.init()
pygame.font.init()

screen_width = 600
screen_height = 800

black = (25, 25, 25)
white = (255, 255, 255)


clock = pygame.time.Clock()


def random_sudoku():
    puzzle = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    if all(a == 0 for a in puzzle):
        return puzzle
    else:
        file = pd.read_csv('randomsudoku.csv', sep=',', header=None)
        random_puzzle = random.randrange(len(file[0]))
        for i in range(9):
            for j in range(9):
                puzzle[i][j] = int(file[0][random_puzzle][i * 9 + j])
        return puzzle


def draw_grid(screen):
    gap = screen_width / 9
    for i in range(10):
        if i % 3 == 0:
            thick = 6
        else:
            thick = 1
        pygame.draw.line(screen, white, (gap * i, 100),
                         (gap * i, screen_height - 100), thick)
        pygame.draw.line(screen, white, (0, 100 + gap * i),
                         (screen_width, 100 + gap * i), thick)


def write_text(surface, output, X, Y):
    font = pygame.font.Font('freesansbold.ttf', 50)
    text = font.render(str(output), True, white)
    surface.blit(text, (X, Y))


if __name__ == '__main__':
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Sudoku Solver')
    sudoku = random_sudoku()

    font = pygame.font.Font('freesansbold.ttf', 25)
    space_text = font.render(
        'Press space to reveal the solution', True, white)
    clock = pygame.time.Clock()
    clock.tick(30)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    solver.solution(sudoku)

        screen.fill(black)
        draw_grid(screen)
        space_between = screen_width / 9
        for i in range(9):
            for j in range(9):
                if sudoku[i][j] != 0:
                    write_text(
                        screen, sudoku[i][j], 20 + space_between * j, 115 + space_between * i)
        screen.blit(space_text, (screen_width/2 -
                                 space_text.get_width()/2, 50))
        pygame.display.update()
        clock.tick(60)
