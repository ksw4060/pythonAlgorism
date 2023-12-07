
s = "one4seveneight"

# def solution(s):
num_arr = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
print(num_arr)
for index, value in enumerate(num_arr):
    print(f"Index: {index}, Value: {value}")
# for key, idx in enmrt_arr:

def solution(s):
    num_arr = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    enmrt_arr = enumerate(num_arr)
    for index, value in enmrt_arr:
        s = s.replace(value, str(index))
    answer = int(s)
    return answer