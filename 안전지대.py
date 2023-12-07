def solution(board):
    answer = 0
    board_copy = [arr[:] for arr in board]
    l = len(board)

    for i_num, i in enumerate(board):
        for u_num, u in enumerate(i):
            if u == 1:
                if u_num > 0 and u_num < l-1:
                    board_copy[i_num][u_num-1] = 1
                    board_copy[i_num][u_num+1] = 1

                elif u_num == 0:
                    board_copy[i_num][u_num+1] = 1
                else:
                    board_copy[i_num][u_num-1] = 1
            else:
                continue

            if i_num != 0 and i_num != l-1:
                board_copy[i_num-1] = board_copy[i_num]
                board_copy[i_num+1] = board_copy[i_num]

            elif i_num == 0:
                board_copy[i_num+1] = board_copy[i_num]

            else:
                board_copy[i_num-1] = board_copy[i_num]

    for i in board_copy:
        answer += sum(i)

    return l**2 - answer
