import random
from colorama import init, Fore, Style
init(autoreset=True)

def display_board(board):
    print()
    for row in range(3):
        if row == 1:
            print(Fore.RED + ctrl + Style.RESET_ALL)
        elif row == 2:
            print(Fore.MAGENTA + ctrl + Style.RESET_ALL)
        print(Fore.YELLOW + " | ".join([board[row][0], board[row][1], board[row][2]]) + Style.RESET_ALL)
        if row < 2:
            print(Fore.CYAN + "---+---+---" + Style.RESET_ALL)
    print()

def get_move(symbol):
    while True:
        pos = input(Fore.CYAN + f"Do you want to be X or O? " + Style.RESET_ALL).upper()
        if symbol not in ["X", "O"]:
            symbol = input(Fore.YELLOW + "Try again (X or O): ").upper()
        else:
            return pos if pos in ("X", "O") else get_move(symbol)

def play_move(board, symbol):
    while True:
        try:
            move = int(input(Fore.GREEN + "Enter your move (1-9): "))
            if move < 1 or move > 9 or board[(move - 1) // 3][(move - 1) % 3] != " ":
                raise ValueError
            board[(move - 1) // 3][(move - 1) % 3] = symbol
            break
        except ValueError:
            print(Fore.RED + "Invalid move. Try again.")

def ai_move(board, symbol, player_symbol):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = symbol
                if check_win(board, symbol):
                    return
                board[i][j] = " "

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = player_symbol
                if check_win(board, player_symbol):
                    board[i][j] = symbol
                    return
                board[i][j] = " "

    possible_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    move = random.choice(possible_moves)
    board[move[0]][move[1]] = symbol
def check_win(board, symbol):
    win_cond = [
        [(0, 0), (0, 1), (0, 2)],  # Horizontal
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],  # Vertical
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],  # Diagonal
        [(0, 2), (1, 1), (2, 0)]
    ]
    for cond in win_cond:
        if board[cond[0][0]][cond[0][1]] == board[cond[1][0]][cond[1][1]] == board[cond[2][0]][cond[2][1]] == symbol:
            return True
    return False

def check_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    print(Fore.CYAN + "=== Tic-Tac-Toe ===" + Style.RESET_ALL)
    player_name = input(Fore.GREEN + "Enter your name: " + Style.RESET_ALL)
    player_symbol = get_move("X")
    ai_symbol = "O" if player_symbol == "X" else "X"
    board = [[" "]*3 for _ in range(3)]
    current_turn = "player" if player_symbol == "X" else "ai"
    game_on = True

    while game_on:
        display_board(board)
        if current_turn == "player":
            play_move(board, player_symbol)
            if check_win(board, player_symbol):
                display_board(board)
                print(Fore.GREEN + player_name + ", you have won the game!")
                game_on = False
            else:
                current_turn = "ai"
        else:
            ai_move(board, ai_symbol, player_symbol)
            if check_win(board, ai_symbol):
                display_board(board)
                print(Fore.RED + "AI wins!")
                game_on = False
            else:
                current_turn = "player"
        if check_full(board) and game_on:
            display_board(board)
            print(Fore.YELLOW + "It's a tie!")
            break

    play_again = input(Fore.CYAN + "Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        tic_tac_toe()
    else:
        print(Fore.CYAN + "Thanks for playing!")

# Run the game
tic_tac_toe()
