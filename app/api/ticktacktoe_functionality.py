def check_winstates(board, i, j):
    average = 0
    priorAverage = 0
    # Horizontal Line
    if j <= 15-5:
        for x in range(0, 5):
            average += int(board[i][j + x] == "X") - int(board[i][j + x] == "O")
    if abs(priorAverage) < abs(average): priorAverage = average
    average = 0
    # Vertical Line
    if i <= 5:
        for x in range(0, 5): 
            average += int(board[i + x][j] == "X") - int(board[i + x][j] == "O")
    if abs(priorAverage) < abs(average): priorAverage = average
    average = 0
    # Left Diagonal Line
    if i <= 15-5 and j >= 5:
        for x in range(0, 5):
            average += int(board[i + x][j - x] == "X") - int(board[i + x][j - x] == "O")
    if abs(priorAverage) < abs(average): priorAverage = average
    average = 0
    # Right Diagonal Line
    if i <= 15-5 and j <= 15-5:
        for x in range(0, 5):
            average += int(board[i + x][j + x] == "X") - int(board[i + x][j + x] == "O")
    if abs(priorAverage) < abs(average): priorAverage = average
    return priorAverage

def validate_gamestate(board):
    round = 1
    xCount = 0
    oCount = 0
    for y in board:
        for x in y:
            xCount += int(x =="X")
            oCount += int(x =="O")
            round += int(x =="O")
    if round > 5: return "midgame"

    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            result = check_winstates(board, i, j)
            if result == 4 and not bool(abs(xCount-oCount)): return "endgame"
            if result == -4 and bool(abs(xCount-oCount)): return "endgame"
    return "opening"

def has_invalid_char(board):
    for y in board:
        for x in y:
            if x not in ["X", "O", ""]: return True
    return False

def has_illegal_size(board):
    if len(board) != 15: return True
    for x in board:
        if len(x) != 15: return True
    return False

def has_bad_actor(board):
    xCount = 0
    oCount = 0
    for y in board:
        for x in y:
            xCount += int(x =="X")
            oCount += int(x =="O")
    difference = xCount - oCount
    if abs(difference) > 1: return True
    else: return False