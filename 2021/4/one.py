num_queue_str = input()
num_queue = []
for s in num_queue_str.split(","):
    num_queue.append(int(s))


boards = []
marked = []
grid_length = 5
while True:
    try:
        input()
    except EOFError:
        break

    board = []
    mark = []
    
    for j in range(grid_length):
        bstr = input()
        row = []
        mark_row = []
        for st in bstr.split(" "):
            if (st != ""):
                row.append(int(st))
                mark_row.append(False)
        mark.append(mark_row)
        board.append(row)
        print(row)
    marked.append(mark)
    boards.append(board)
    print()


def victory(win_num, win_board):
    unmarked_sum = 0
    for i in range(grid_length):
        for j in range(grid_length):
            if(marked[win_board][i][j] == False):
                unmarked_sum += boards[win_board][i][j]

    print(unmarked_sum, win_num)
    print(unmarked_sum * win_num)

winning_num = -1
winning_board_num = -1
for num in num_queue:
    for i in range(len(boards)):
        for j in range(grid_length):
            winning_row = True
            for k in range(grid_length):
                if (num == boards[i][j][k]):
                    marked[i][j][k] = True
                if (marked[i][j][k] != True):
                    winning_row = False
            if winning_row:
                victory(num, i)
                exit()
        
        for k in range(grid_length):
            winning_col = True
            for j in range(grid_length):
                if (i == 2 and k == 0):
                    print(boards[i][j][k], marked[i][j][k])
                if (marked[i][j][k] != True):
                    winning_col = False
            if winning_col:
                victory(num, i)
                exit()
unmarked_sum = -1
for i in range(grid_length):
    for j in range(grid_length):
        if(marked[winning_board_num][i][j] == False):
            unmarked_sum += boards[winning_board_num][i][j]

print(unmarked_sum, winning_num)
print(unmarked_sum * winning_num)