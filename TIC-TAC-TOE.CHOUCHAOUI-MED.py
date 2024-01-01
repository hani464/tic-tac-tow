import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return 1
    if check_winner(board, 'X'):
        return -1
    if is_board_full(board):
        return 0

    if is_maximizing:
        max_eval = float('-inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'O'  # AI's move
            eval = minimax(board, depth + 1, False)
            board[i][j] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'X'  # Player's move
            eval = minimax(board, depth + 1, True)
            board[i][j] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

def get_best_move(board, difficulty):
    if difficulty == 'easy':
        return random.choice(get_empty_cells(board))
    elif difficulty == 'hard':
        best_val = float('-inf')
        best_move = (-1, -1)
        for i, j in get_empty_cells(board):
            board[i][j] = 'O'
            move_val = minimax(board, 0, False)
            board[i][j] = ' '
            if move_val > best_val:
                best_move = (i, j)
                best_val = move_val
        return best_move

def play_tic_tac_toe():
    player_name = input("Enter your name: ")
    difficulty = input("Choose difficulty (easy/hard): ").lower()
    score = {player_name: 0, 'AI': 0}

    while True:
        board = [[' ' for _ in range(3)] for _ in range(3)]
        player_turn = random.choice([True, False])  # Randomly choose starting player

        print_board(board)

        while not (check_winner(board, 'X') or check_winner(board, 'O') or is_board_full(board)):
            if player_turn:
                while True:
                    try:
                        row = int(input("Enter row (0, 1, or 2): "))
                        col = int(input("Enter column (0, 1, or 2): "))
                        if board[row][col] == ' ':
                            board[row][col] = 'X'
                            break
                        else:
                            print("Cell already occupied. Try again.")
                    except (ValueError, IndexError):
                        print("Invalid input. Please enter a valid row and column.")
            else:
                print("AI is making a move...")
                row, col = get_best_move(board, difficulty)
                board[row][col] = 'O'

            print_board(board)
            player_turn = not player_turn

        if check_winner(board, 'X'):
            print(f"{player_name} wins!")
            score[player_name] += 1
        elif check_winner(board, 'O'):
            print("AI wins!")
            score['AI'] += 1
        else:
            print("It's a draw!")

        print(f"Score - {player_name}: {score[player_name]} | AI: {score['AI']}")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    play_tic_tac_toe()
