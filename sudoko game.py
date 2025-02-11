# Importing the libraries
import pygame
import requests


# Initialising the pygame
pygame.init()

# Setting width and height of the window
width = 550
height = 550

# Creating the window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sudoku")

font = pygame.font.Font("freesansbold.ttf", 35)


# Calling the API
response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
s_grid = response.json()['board']
grid_original = [[s_grid[x][y] for y in range(len(s_grid[0]))] for x in range(len(s_grid))]
grid_color = (52, 31, 151)

# Inserting user input
def insert(screen, position):
    i, j = position[1], position[0]
    font = pygame.font.Font("freesansbold.ttf", 35)
    while True:
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
                return
           if event.type == pygame.KEYDOWN:
                 if (grid_original[i - 1][j - 1] != 0):  # Checking to not disturb original
                    return
                 if (event.key == 48):  # checking with 0
                    s_grid[i - 1][j - 1] = event.key - 48
                    pygame.draw.rect(screen, (255, 255, 255),
                                     (position[0] * 50 + 5, position[1] * 50 + 10, 50 - 10, 50 - 10))
                    pygame.display.update()
                 if (0 < event.key - 48 < 10):  # valid input
                         pygame.draw.rect(screen, (255, 255, 255),(position[0] * 50 + 5, position[1] * 50 + 10, 50 - 10, 50 - 10))
                         value = font.render(str(event.key - 48), True, (0, 0, 0))
                         screen.blit(value, (position[0] * 50 + 15, position[1] * 50))
                         s_grid[i - 1][j - 1] = event.key - 48
                         pygame.display.update()
    return


# Game Loop
running = True
while running:
    screen.fill((255, 255, 255))
    # Checking the event
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            pos = pygame.mouse.get_pos()
            insert(screen, (pos // 50, pos // 50))
        if event.type == pygame.QUIT:
            running = False

    # Drawing the grid
    for i in range(0, 10):
        if (i % 3 == 0):
            pygame.draw.line(screen, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 4)
            pygame.draw.line(screen, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 4)
        pygame.draw.line(screen, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 2)
        pygame.draw.line(screen, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 2)

    pygame.display.update()

    # Manipulating the user value
    for i in range(0, len(s_grid[0])):
        for j in range(0, len(s_grid[0])):
            if (0 < s_grid[i][j] < 10):
                value = font.render(str(s_grid[i][j]), True, grid_color)
                screen.blit(value, ((j + 1) * 50 + 15, (i + 1) * 50))
    pygame.display.update()
pygame.quit() 