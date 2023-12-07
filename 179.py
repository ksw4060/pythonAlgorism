import numpy as np
# numpy

my_list = [100, 200, 400, 800, 1000, 1300]

for i in range(0, 4):
    # i, i+1, i+2의 평균을 구하시오
    # print(np.mean(my_list[i:i+3]))
    print(round(np.mean(my_list[i:i+3]), 2))
