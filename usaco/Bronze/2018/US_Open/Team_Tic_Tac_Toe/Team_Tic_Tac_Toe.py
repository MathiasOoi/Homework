from itertools import combinations
with open("tttt.in") as fin:
    cows, board = set(), []
    for s in fin.readlines():
        curr = []
        for i in s:
            if i != "\n":
                cows.add(i)
                curr.append(i)
        board.append(curr)


def single_win(char, board):
    return board[0][0] == board[0][1] == board[0][2] == char or \
        board[1][0] == board[1][1] == board[1][2] == char or \
        board[2][0] == board[2][1] == board[2][2] == char or \
        board[0][0] == board[1][0] == board[2][0] == char or \
        board[0][1] == board[1][1] == board[2][1] == char or \
        board[0][2] == board[1][2] == board[2][2] == char or \
        board[0][0] == board[1][1] == board[2][2] == char or \
        board[0][2] == board[1][1] == board[2][2] == char



def double_win(char1, char2):
    temp_board = [lst[:] for lst in board]
    for i, a in enumerate(temp_board):
        for k,b in enumerate(a):
            if b == char1 or b == char2:
                temp_board[i][k] = "_"
    return single_win("_", temp_board)


with open("tttt.out", "w") as fout:
    single_count = double_count = 0
    for i in cows:
        if single_win(i, board)[0]:
            single_count += 1
    for i, k in combinations(cows, 2):
        if double_win(i, k) and i != k:
            print(i, k)
            double_count += 1
    for s in board:
        print(s)
    fout.write(str(single_count) + "\n" + str(double_count))
