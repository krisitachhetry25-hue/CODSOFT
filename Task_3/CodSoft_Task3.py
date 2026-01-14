import numpy as np

b = np.zeros((3, 3), dtype=int)

def check_winner(board):
    rows = board.sum(axis=0)
    cols = board.sum(axis=1)
    d1 = np.trace(board)
    d2 = np.trace(np.fliplr(board))
    
    sums = np.concatenate([rows, cols, [d1, d2]])
    
    if 3 in sums:
        return 1
    if -3 in sums:
        return -1
    if 0 not in board:
        return 0
    return None

def minimax(board, is_max):
    winner = check_winner(board)
    if winner is not None:
        return winner
    
    scores = []
    for r, c in zip(*np.where(board == 0)):
        board[r, c] = 1 if is_max else -1
        scores.append(minimax(board, not is_max))
        board[r, c] = 0
    
    return max(scores) if is_max else min(scores)

def print_board(board):
    symbols = {1: 'O', -1: 'X', 0: ' '}
    for row in board:
        print("| " + " | ".join(symbols[val] for val in row) + " |")

def play_game():
    global b
    print("Tic-Tac-Toe - You are X, AI is O\n")
    
    while check_winner(b) is None:
        print_board(b)
        
        while True:
            try:
                inp = input("\nEnter your move (row col, 0-2): ").split()
                r, c = int(inp[0]), int(inp[1])
                if b[r, c] != 0:
                    print("That spot is taken!")
                    continue
                b[r, c] = -1
                break
            except:
                print("Invalid input, try again")
        
        if check_winner(b) is not None:
            break
        
        print("AI thinking...")
        best_val = -2
        best_move = None
        
        for r, c in zip(*np.where(b == 0)):
            b[r, c] = 1
            val = minimax(b, False)
            b[r, c] = 0
            if val > best_val:
                best_val = val
                best_move = (r, c)
        
        if best_move:
            b[best_move] = 1
    
    print("\n" + "="*20)
    print_board(b)
    
    winner = check_winner(b)
    if winner == 1:
        print("AI wins!")
    elif winner == -1:
        print("You win!")
    else:
        print("It's a tie!")
    print("="*20)

if __name__ == "__main__":
    play_game()