# Tic-Tac-Toe in Processing (Python Mode)
#
# Controls:
#   Left click -> place your mark in a cell
#   R          -> restart with a new board
from processing import *

COLS = 3
ROWS = 3
CELL = 120

board = []          # board[row][col] -> "", "X", or "O"
current_player = "X"
game_over = False
winner = ""          # "X", "O", or "" (no winner yet / draw)


def setup():
    size(COLS * CELL, ROWS * CELL + 50)
    textAlign(CENTER, CENTER)
    new_game()


def new_game():
    global board, current_player, game_over, winner

    board = make_grid()
    current_player = "X"
    game_over = False
    winner = ""


def make_grid():
    grid = []
    for r in range(ROWS):
        row = []
        for c in range(COLS):
            row.append("")
        grid.append(row)
    return grid


def check_winner():
    # Check each row
    for r in range(ROWS):
        if board[r][0] != "" and board[r][0] == board[r][1] and board[r][1] == board[r][2]:
            return board[r][0]

    # Check each column
    for c in range(COLS):
        if board[0][c] != "" and board[0][c] == board[1][c] and board[1][c] == board[2][c]:
            return board[0][c]

    # Check both diagonals
    if board[0][0] != "" and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]

    if board[0][2] != "" and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]

    return ""


def board_is_full():
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == "":
                return False
    return True


def mousePressed():
    global current_player, game_over, winner

    if game_over:
        return

    if mouseY >= ROWS * CELL:
        return

    c = mouseX // CELL
    r = mouseY // CELL

    if r < 0 or r >= ROWS or c < 0 or c >= COLS:
        return

    if board[r][c] != "":
        return

    board[r][c] = current_player

    winner = check_winner()
    if winner != "":
        game_over = True
    elif board_is_full():
        game_over = True
    else:
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


def keyPressed():
    if key == 'r' or key == 'R':
        new_game()


def draw():
    background(240)
    draw_grid_lines()
    draw_marks()
    draw_status_bar()


def draw_grid_lines():
    stroke(50)
    strokeWeight(3)

    for c in range(1, COLS):
        x = c * CELL
        line(x, 0, x, ROWS * CELL)

    for r in range(1, ROWS):
        y = r * CELL
        line(0, y, COLS * CELL, y)


def draw_marks():
    strokeWeight(6)

    for r in range(ROWS):
        for c in range(COLS):
            mark = board[r][c]
            x = c * CELL
            y = r * CELL
            pad = CELL * 0.2

            if mark == "X":
                stroke(200, 50, 50)
                line(x + pad, y + pad, x + CELL - pad, y + CELL - pad)
                line(x + CELL - pad, y + pad, x + pad, y + CELL - pad)
            elif mark == "O":
                stroke(50, 90, 200)
                noFill()
                ellipse(x + CELL / 2, y + CELL / 2, CELL - 2 * pad, CELL - 2 * pad)


def draw_status_bar():
    noStroke()
    fill(50)
    rect(0, ROWS * CELL, COLS * CELL, 50)

    fill(255)
    textSize(18)

    if not game_over:
        message = "Turn: " + current_player
    elif winner != "":
        message = winner + " wins!  Press R to play again."
    else:
        message = "It's a draw!  Press R to play again."

    text(message, COLS * CELL / 2, ROWS * CELL + 25)

run()
#6901012610137
#Lab07-1