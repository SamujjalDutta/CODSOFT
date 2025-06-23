import random
from colorama import Fore, Style, init

init(autoreset=True)


def makeBoard():
    return [["-" for _ in range(3)] for _ in range(3)]


def showBoard(board):
    for r in board:
        print(" | ".join(Fore.BLUE + c + Style.RESET_ALL if c == "X"
                         else Fore.RED + c + Style.RESET_ALL if c == "O" else c for c in r))
        print("-" * 9)


def userMove(board, player, moves):
    while True:
        try:
            row = int(input(f"\n{player}'s turn. Pick row (0-2): "))
            col = int(input("Pick column (0-2): "))
            if row in range(3) and col in range(3):
                if board[row][col] == "-":
                    board[row][col] = player
                    moves.append((player, row, col))
                    break
                else:
                    print("Oops! Spot already filled.")
            else:
                print("Please enter values between 0 and 2.")
        except:
            print("Enter valid integers only.")


def hasWinner(board, player):
    b = board
    win_lines = (
        [b[0], b[1], b[2]],
        [[b[i][0] for i in range(3)], [b[i][1] for i in range(3)], [
            b[i][2] for i in range(3)]],
        [[b[i][i] for i in range(3)], [b[i][2-i]
                                       for i in range(3)]]
    )
    return any(all(cell == player for cell in line) for lines in win_lines for line in lines)


def draw(board):
    return all(cell != "-" for row in board for cell in row)


def thinkMinimax(board, depth, is_maxing):
    if hasWinner(board, "X"):
        return 1
    elif hasWinner(board, "O"):
        return -1
    elif draw(board):
        return 0

    if is_maxing:
        score = -float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == "-":
                    board[i][j] = "X"
                    score = max(score, thinkMinimax(board, depth + 1, False))
                    board[i][j] = "-"
        return score
    else:
        score = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == "-":
                    board[i][j] = "O"
                    score = min(score, thinkMinimax(board, depth + 1, True))
                    board[i][j] = "-"
        return score


def aiBestMove(board):
    best_score = float("inf")
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == "-":
                board[i][j] = "O"
                score = thinkMinimax(board, 0, True)
                board[i][j] = "-"
                if score < best_score:
                    best_score = score
                    move = (i, j)
    return move


def aiRandomMove(board):
    options = [(i, j) for i in range(3)
               for j in range(3) if board[i][j] == "-"]
    return random.choice(options)


def runGame():
    print("Welcome to Smart Tic-Tac-Toe \nYou are 'X', AI is 'O'\n")
    level = input("Choose difficulty (easy/hard): ").strip().lower()
    playerWins, aiWins = 0, 0

    while True:
        board = makeBoard()
        moves = []
        turn = "X"

        while True:
            showBoard(board)
            if turn == "X":
                userMove(board, "X", moves)
            else:
                print("AI is playing...")
                x, y = aiRandomMove(
                    board) if level == "easy" else aiBestMove(board)
                board[x][y] = "O"
                moves.append(("O", x, y))

            if hasWinner(board, turn):
                showBoard(board)
                print(f"{turn} wins this round!")
                if turn == "X":
                    playerWins += 1
                else:
                    aiWins += 1
                break
            elif draw(board):
                showBoard(board)
                print("It's a draw!")
                break

            turn = "O" if turn == "X" else "X"

        print("\nMove History:")
        for move in moves:
            print(f"{move[0]} played at ({move[1]}, {move[2]})")

        print(f"\nScore — You: {playerWins} | AI: {aiWins}")
        again = input("Play another round? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thanks for playing")
            break


runGame()
