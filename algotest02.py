import string

S = "sparta"

result = [-1]*len(string.ascii_lowercase)

for i in range(len(S)):
    char = S[i]
    for j in range(len(string.ascii_lowercase)):
        lo = string.ascii_lowercase[j]
        if result[j] == -1 and char == lo:
            result[j] = i

for i in range(26):
    print(result[i], end=' ')
