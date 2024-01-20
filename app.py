import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, maximizing_player):
    scores = {'X': 1, 'O': -1, 'draw': 0}

    if check_winner(board, 'X'):
        return scores['X']
    elif check_winner(board, 'O'):
        return scores['O']
    elif check_draw(board):
        return scores['draw']

    if maximizing_player:
        max_eval = float('-inf')
        for move in available_moves(board):
            board[move[0]][move[1]] = 'X'
            eval = minimax(board, depth + 1, False)
            board[move[0]][move[1]] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in available_moves(board):
            board[move[0]][move[1]] = 'O'
            eval = minimax(board, depth + 1, True)
            board[move[0]][move[1]] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

def best_move(board):
    best_val = float('-inf')
    move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                eval = minimax(board, 0, False)
                board[i][j] = ' '

                if eval > best_val:
                    move = (i, j)
                    best_val = eval

    return move

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player_turn = True

    while True:
        print_board(board)

        if player_turn:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if board[row][col] == ' ':
                board[row][col] = 'X'
                player_turn = False
            else:
                print("Cell already taken. Try again.")
        else:
            print('player 2')
            move = best_move(board)
            board[move[0]][move[1]] = 'O'
            player_turn = True

        if check_winner(board, 'X'):
            print_board(board)
            print("Victory!")
            break
        elif check_winner(board, 'O'):
            print_board(board)
            print("Defeat!")
            break
        elif check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()

