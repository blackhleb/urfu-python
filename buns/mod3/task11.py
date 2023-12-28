def check_winner(board):
    n = len(board)
    k = len(board[0])

    for i in range(n):
        for j in range(n - k + 1):
            symbol = board[i][j]
            if symbol == '_':
                continue
            if all(board[i][j + l] == symbol for l in range(k)):
                return symbol

    for i in range(n - k + 1):
        for j in range(n):
            symbol = board[i][j]
            if symbol == '_':
                continue
            if all(board[i + l][j] == symbol for l in range(k)):
                return symbol

    for i in range(n - k + 1):
        for j in range(n - k + 1):
            symbol = board[i][j]
            if symbol == '_':
                continue
            if all(board[i + l][j + l] == symbol for l in range(k)):
                return symbol

    for i in range(n - k + 1):
        for j in range(k - 1, n):
            symbol = board[i][j]
            if symbol == '_':
                continue
            if all(board[i + l][j - l] == symbol for l in range(k)):
                return symbol

    return "Ничья"


a = input()
board = [list(a)]

for i in range(len(a)-1):
    row = input()
    board.append(list(row))

winner = check_winner(board)

print(winner)
