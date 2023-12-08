# 176
my_list = ["가", "나", "다", "라", "마"]

first3_list = my_list[:3] # 0, 1, 2
middle3_list = my_list[1:4]
last3_list = my_list[2:]

for i in range(3):
    print(first3_list[i], middle3_list[i], last3_list[i])
