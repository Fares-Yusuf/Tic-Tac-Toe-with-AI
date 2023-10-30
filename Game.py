import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 3, 3
SQUARE_SIZE = WIDTH//COLS

# Set up the display
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Load the X and O images
X_IMAGE = pygame.transform.scale(pygame.image.load('x.png'), (200, 200))
O_IMAGE = pygame.transform.scale(pygame.image.load('o.png'), (200, 200))

# Set up the board
board = [' ' for _ in range(10)]


# Inserts a letter ('X' or 'O') at a given position on the game board.
def insertLetter(letter, position):
    board[position] = letter


# Checks if a space on the game board is free.
def spaceIsFree(position):
    return board[position] == ' '


# Checks if a player has won the game.
def isWinner(game_board: list, player_letter: str) -> bool:
    return (game_board[7] == player_letter and game_board[8] == player_letter and game_board[9] == player_letter) or \
           (game_board[4] == player_letter and game_board[5] == player_letter and game_board[6] == player_letter) or \
           (game_board[1] == player_letter and game_board[2] == player_letter and game_board[3] == player_letter) or \
           (game_board[1] == player_letter and game_board[4] == player_letter and game_board[7] == player_letter) or \
           (game_board[2] == player_letter and game_board[5] == player_letter and game_board[8] == player_letter) or \
           (game_board[3] == player_letter and game_board[6] == player_letter and game_board[9] == player_letter) or \
           (game_board[1] == player_letter and game_board[5] == player_letter and game_board[9] == player_letter) or \
           (game_board[3] == player_letter and game_board[5] ==
            player_letter and game_board[7] == player_letter)

# This function implements the Minimax algorithm to choose the best move for the AI.


def minimax(current_board, current_depth, isMaximizing):
    # Base cases: if the game has ended, return the score from the AI's perspective.
    if (isWinner(current_board, 'O')):  # AI has won
        return 1
    elif (isWinner(current_board, 'X')):  # Player has won
        return -1

    # Generate a list of all possible moves (empty spaces on the board).
    possibleMoves = [index for index, letter in enumerate(
        current_board) if letter == ' ' and index != 0]
    # If there are no possible moves left, the game is a tie.
    if len(possibleMoves) == 0:
        return 0

    # If this is a maximizing layer (AI's turn), find the maximum possible score.
    if (isMaximizing):
        bestScore = -800  # Start with a very low best score.
        for index in possibleMoves:  # For each possible move...
            current_board[index] = 'O'  # Try making that move.
            # Recursively calculate the score for that move.
            score = minimax(current_board, current_depth + 1, False)
            current_board[index] = ' '  # Undo the move.
            # Update the best score if necessary.
            bestScore = max(score, bestScore)
        return bestScore
    # If this is a minimizing layer (player's turn), find the minimum possible score.
    else:
        bestScore = 800  # Start with a very high best score.
        for index in possibleMoves:  # For each possible move...
            current_board[index] = 'X'  # Try making that move.
            # Recursively calculate the score for that move.
            score = minimax(current_board, current_depth + 1, True)
            current_board[index] = ' '  # Undo the move.
            # Update the best score if necessary.
            bestScore = min(score, bestScore)
        return bestScore


def compMove():
    # Creating a list of possible moves
    possibleMoves = [x for x, letter in enumerate(
        board) if letter == ' ' and x != 0]
    move = 0

    # Checking for a winning move or blocking an opponent's winning move
    for let in ['O', 'X']:
        for index in possibleMoves:
            boardCopy = board[:]
            boardCopy[index] = let
            if isWinner(boardCopy, let):
                move = index
                return move

    # If no winning move is available, use the minimax algorithm to select the best move
    bestScore = -800
    for index in possibleMoves:
        boardCopy = board[:]
        boardCopy[index] = 'O'
        score = minimax(boardCopy, 0, False)
        if (score > bestScore):
            bestScore = score
            move = index

    return move


def draw_button(text, x, y, ic, ac, action=None):
    w, h = 100, 50  # Fixed width and height
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(WIN, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(WIN, ic, (x, y, w, h))

    smallText = pygame.font.SysFont(None, 20)
    textSurf = smallText.render(text, True, (0, 0, 0))
    textRect = textSurf.get_rect()
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    WIN.blit(textSurf, textRect)


def draw_window():
    WIN.fill((255, 255, 255))

    # Draw grid
    for i in range(1, ROWS):
        pygame.draw.line(WIN, (0, 0, 0), (0, i*SQUARE_SIZE),
                         (WIDTH, i*SQUARE_SIZE))
        pygame.draw.line(WIN, (0, 0, 0), (i*SQUARE_SIZE, 0),
                         (i*SQUARE_SIZE, HEIGHT))

    # Draw X's and O's
    for i in range(1, 10):
        x = (i-1) % 3
        y = (i-1)//3

        if board[i] == 'X':
            WIN.blit(X_IMAGE, (x*SQUARE_SIZE + SQUARE_SIZE//2 - X_IMAGE.get_width() //
                     2, y*SQUARE_SIZE + SQUARE_SIZE//2 - X_IMAGE.get_height()//2))
        elif board[i] == 'O':
            WIN.blit(O_IMAGE, (x*SQUARE_SIZE + SQUARE_SIZE//2 - O_IMAGE.get_width() //
                     2, y*SQUARE_SIZE + SQUARE_SIZE//2 - O_IMAGE.get_height()//2))

    pygame.display.update()


def reset_game():
    global board
    board = [' ' for _ in range(10)]
    main()  # Call the main function to restart the game


def quit_game():
    pygame.quit()
    sys.exit()


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


# This is the main function that runs the game loop.
def main():
    # Create a clock object to control the game's frame rate.
    clock = pygame.time.Clock()
    # This variable is used to control the game loop.
    run = True

    # Start the game loop.
    while run:
        # Set the game's frame rate to 60 frames per second.
        clock.tick(60)

        # Process all events in the event queue.
        for event in pygame.event.get():
            # If the QUIT event is detected, stop the game loop.
            if event.type == pygame.QUIT:
                run = False

            # If a mouse button down event is detected, process the player's move.
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Get the current mouse position.
                x, y = pygame.mouse.get_pos()
                # Calculate the board position corresponding to the mouse position.
                pos = x//SQUARE_SIZE + 1 + (y//SQUARE_SIZE)*3
                # If the calculated position is free, insert an 'X' there.
                if spaceIsFree(pos):
                    insertLetter('X', pos)
                    if not isWinner(board, 'X'):
                        move = compMove()
                        # If a valid move was found, insert an 'O' there.
                        if move != 0:
                            insertLetter('O', move)

        # Redraw the game window.
        draw_window()

        # Check for end of game
        if isWinner(board, 'O') or isWinner(board, 'X') or isBoardFull(board):
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                # Draw buttons
                draw_button("Play Again", WIDTH // 2 - 120, HEIGHT // 2 - 25,
                            (0, 255, 0), (0, 200, 0), reset_game)
                draw_button("Quit", WIDTH // 2 + 20, HEIGHT // 2 - 25,
                            (255, 0, 0), (200, 0, 0), quit_game)

                pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
