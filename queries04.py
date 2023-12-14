# https://school.programmers.co.kr/learn/courses/30/lessons/181923
# 수열과 구간 쿼리 2

arr = [0, 1, 2, 3, 4]
queries = [[0, 4, 2],[0, 3, 2],[0, 2, 2]]

for query in queries:
    s, e, k = query
    available_arr = arr[s:e+1]
    print(available_arr)
    filtered_arr = [x for x in available_arr if x > k]
    print(filtered_arr)
print(arr)
print(max(arr))
