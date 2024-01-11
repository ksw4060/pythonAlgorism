"""
link : https://school.programmers.co.kr/learn/courses/30/lessons/181913

문제 설명
    문자열 my_string과 이차원 정수 배열 queries가 매개변수로 주어집니다. queries의 원소는 [s, e] 형태로, my_string의 __인덱스 s부터 인덱스 e까지를 뒤집으라는 의미입니다.__ my_string에 queries의 명령을 순서대로 처리한 후의 문자열을 return 하는 solution 함수를 작성해 주세요.
제한사항
    my_string은 영소문자로만 이루어져 있습니다.
    1 ≤ my_string의 길이 ≤ 1,000
    queries의 원소는 [s, e]의 형태로 0 ≤ s ≤ e < my_string의 길이를 만족합니다.
    1 ≤ queries의 길이 ≤ 1,000

"""

my_string = "rermgorpsam"
queries = [[2, 3], [0, 7], [5, 9], [6, 10]]
# def solution(my_string, queries):
#     my_string_list = list(my_string)
for query in queries:
    x, y = query
    my_string = list(my_string)
    print(x, y)

    my_string[x], my_string[y] = my_string[y], my_string[x]
    print(my_string)



    # return ''.join(my_string_list)

# print(solution(my_string, queries))
