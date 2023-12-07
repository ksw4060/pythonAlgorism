s = input()

def solution(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result_str = ""
    
    for a in alphabet:
        result_str += str(str(s.find(a)) + " ")

    return result_str

print(solution(s))