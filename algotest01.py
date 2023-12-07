import string


def get_idx_naive(S):
		# O(N^2)
    # string.ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    result = [-1]*len(string.ascii_lowercase)
    # result = [-1, -1, -1, -1, -1, -1, -1, ... ]
    for i in range(len(S)):
        char = S[i]
        for j in range(len(string.ascii_lowercase)):
            lo = string.ascii_lowercase[j]
            if result[j] == -1 and char == lo:
                result[j] = i
    return result


def get_idx(word):
    # O(N)
    result = [-1]*len(string.ascii_lowercase)
    # a부터 z까지 26개의 소문자들을 -1로 바꾸고, 리스트로 저장함.
    for i in range(len(word)):
        # ord 란 Unicode 코드 포인트를 반환하는 함수임
        # 97번이 소문자 a , 122번이 소문자 z
        # 거기서 97을 빼면, a 는 0, b 는 1, z 는 25가됨.
        idx = ord(word[i]) - 97

        if result[idx] == -1:
            result[idx] = i
            # sparta 글자들을 -1 에서 i 로 변경함.
    return result


print(get_idx_naive('baekjoon'))
print(get_idx('sparta'))
print(ord('a'))

# check = [-1]*26
# for i in range(26):
#     print(check[i], end=' ')

"""
230731 백준 문제풀이

S = input()
result = [-1]*26

for i in range(len(word)):
    idx = ord(word[i]) - 97
    if result[idx] == -1:
        result[idx] = i
        return result

for i in range(26):
    print(result[i], end=' ')

"""
