# https://school.programmers.co.kr/learn/courses/30/lessons/250125
# [PCCE 기출문제] 9번 / 이웃한 칸

def solution(board, h, w):
    answer = 0
    n = len(board)
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    count = 0 # 같은 색 개수 카운트 board[h][w]
    for i in 4:
        h_check = h + dh[i]
        w_check = w + dw[i]
        
    return answer