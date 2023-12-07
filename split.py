string = "hello/python/world!!"
string_list = string.split("/")
print(string_list)
string_join = "@".join(string_list)
print(string_join)
string_upper = string_join.upper()
print(string_upper)
string_replace = string_join.replace("@", "~")
print(string_replace)

# 난수 생성, 임의의 번호 생성 등 랜덤한 동작이 필요할 때 사용
import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(numbers) # numbers를 무작위하게 섞기
print(numbers) # [2, 8, 6, 4, 3, 7, 1, 5]

random_number = random.randint(1, 10) # 1 ~ 10 사이의 무작위 번호 생성
print(random_number) # 4

import time

start_time = time.time() # 현재 시간 저장

time.sleep(1) # 1초간 대기

end_time = time.time()

# 코드가 종료된 시간 - 코드가 시작된 시간으로 실행 시간 구하기 (단위 : 초)
print(end_time, start_time)
print(f"코드 실행 시간 : {end_time-start_time:.5f}") # 코드 실행 시간 : 1.00100
