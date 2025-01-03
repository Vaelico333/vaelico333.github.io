import pygame as pg
import sys
import time

# Initialize Pygame
pg.init()

# Constants
WIDTH = 400
HEIGHT = 500
BACKGROUND = (0, 0, 0)
LINE_COLOR = (255, 255, 255)
FONT_COLOR = (255, 255, 255)
WIN_LINE_COLOR = (250, 70, 70)
GRID_LINE_WIDTH = 7
WIN_LINE_WIDTH = 4
FONT_SIZE = 30

# Global variables
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Tic Tac Toe")
clock = pg.time.Clock()
FPS = 30

current_player = 'x'
current_winner = None
is_draw = False
grid = [[None]*3, [None]*3, [None]*3]

def game_initiating_window():
    """Draws the initial game state."""
    screen.fill(BACKGROUND)
    draw_grid()
    draw_status()
    pg.display.update()

def draw_grid():
    """Draws the Tic Tac Toe grid lines."""
    # Vertical lines
    pg.draw.line(screen, LINE_COLOR, (WIDTH / 3, 0), (WIDTH / 3, HEIGHT), GRID_LINE_WIDTH)
    pg.draw.line(screen, LINE_COLOR, ((WIDTH / 3)*2, 0), ((WIDTH / 3)*2, HEIGHT), GRID_LINE_WIDTH)
    # Horizontal lines
    pg.draw.line(screen, LINE_COLOR, (0, HEIGHT / 3), (WIDTH, HEIGHT / 3), GRID_LINE_WIDTH)
    pg.draw.line(screen, LINE_COLOR, (0, (HEIGHT / 3)*2), (WIDTH, (HEIGHT / 3)*2), GRID_LINE_WIDTH)

def draw_status():
    """Displays the current status at the bottom."""
    global is_draw
    # Displays a black rectangle that covers the old message
    message = "No message"
    font = pg.font.Font(None, FONT_SIZE)
    text = font.render(message, True, (0,0,0), BACKGROUND)
    screen.fill((0, 0, 0), (0, HEIGHT, WIDTH, 100))
    text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 1.7))
    screen.blit(text, text_rect)
    pg.display.update()
    
    # Displays the message of the current status of the game
    if current_winner:
        message = current_winner.upper() + " won!"
    elif is_draw:
        message = "Game Draw!"
    else:
        message = current_player.upper() + "'s Turn"

    font = pg.font.Font(None, FONT_SIZE)
    text = font.render(message, True, FONT_COLOR, BACKGROUND)
    screen.fill((0, 0, 0), (0, HEIGHT, WIDTH, 100))
    text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 1.7))
    screen.blit(text, text_rect)
    pg.display.update()

def check_win():
    """Checks for a winner or a draw."""
    global current_winner, is_draw

    # Check rows
    for row in range(3):
        if (grid[row][0] == grid[row][1] == grid[row][2]) and grid[row][0] is not None:
            current_winner = grid[row][0]
            pg.draw.line(screen, WIN_LINE_COLOR,
                         (0, (row+1)*HEIGHT/3 - HEIGHT/6),
                         (WIDTH, (row+1)*HEIGHT/3 - HEIGHT/6),
                         WIN_LINE_WIDTH)
            break

    # Check columns
    for col in range(3):
        if (grid[0][col] == grid[1][col] == grid[2][col]) and grid[0][col] is not None:
            current_winner = grid[0][col]
            pg.draw.line(screen, WIN_LINE_COLOR,
                         ((col+1)*WIDTH/3 - WIDTH/6, 0),
                         ((col+1)*WIDTH/3 - WIDTH/6, HEIGHT),
                         WIN_LINE_WIDTH)
            break

    # Check diagonals
    if (grid[0][0] == grid[1][1] == grid[2][2]) and grid[0][0] is not None:
        current_winner = grid[0][0]
        pg.draw.line(screen, WIN_LINE_COLOR, (50, 50), (WIDTH-50, HEIGHT-50), WIN_LINE_WIDTH)

    if (grid[0][2] == grid[1][1] == grid[2][0]) and grid[0][2] is not None:
        current_winner = grid[0][2]
        pg.draw.line(screen, WIN_LINE_COLOR, (WIDTH-50, 50), (50, HEIGHT-50), WIN_LINE_WIDTH)

    # Check for draw
    if all(all(row) for row in grid) and not current_winner:
        is_draw = True

    draw_status()

def drawXO(row, col):
    """Draws X or O in the selected grid cell."""
    global current_player
    pos_x = (col-1)*WIDTH/3 + WIDTH/6
    pos_y = (row-1)*HEIGHT/3 + HEIGHT/6

    font = pg.font.Font(None, 100)
    text = font.render(current_player.upper(), True, (255, 255, 255))
    text_rect = text.get_rect(center=(pos_x, pos_y))
    screen.blit(text, text_rect)
    grid[row-1][col-1] = current_player
    current_player = 'o' if current_player == 'x' else 'x'
    pg.display.update()

def user_click():
    """Handles mouse click and updates the game state."""
    x, y = pg.mouse.get_pos()

    if x < WIDTH / 3:
        col = 1
    elif x < (WIDTH / 3) * 2:
        col = 2
    elif x < WIDTH:
        col = 3
    else:
        col = None

    if y < HEIGHT / 3:
        row = 1
    elif y < (HEIGHT / 3) * 2:
        row = 2
    elif y < HEIGHT:
        row = 3
    else:
        row = None

    if row and col and grid[row-1][col-1] is None:
        drawXO(row, col)
        check_win()

def reset_game():
    """Restarts the game on win or draw."""
    global grid, current_winner, current_player, is_draw
    time.sleep(10)
    current_player = 'x'
    current_winner = None
    is_draw = False
    grid = [[None]*3 for _ in range(3)]
    game_initiating_window()

def main():
    """
    Entry point to initialize and start the test4.5 game.
    """
    game_initiating_window()
    # Potentially other setup calls here...
    # Example of a loop or function in test4.5 to start the game:
    # test4_5.run_game_loop()

if __name__ == "__main__":
    main()

# Main game loop
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            user_click()
            if current_winner or is_draw:
                reset_game()

    pg.display.update()
    clock.tick(FPS)