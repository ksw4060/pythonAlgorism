# 대소문자 바꿔서 출력하기

# link : https://school.programmers.co.kr/learn/courses/30/lessons/181949?language=python3

str = input()

for i in str:
    # 대문자인 경우
    if i.isupper():
        print(i.lower(), end='')
    # 소문자인 경우
    else:
        print(i.upper(), end='')

"""
str = input()
a = ''

for s in str :
    if(s.isupper()) :
        a = a + s.lower()
    else :
        a = a + s.upper()

print(a)
"""
