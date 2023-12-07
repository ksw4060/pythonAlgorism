my_list = ["가", "나", "다", "라"]

first3_list = my_list[:3] # 0, 1, 2
last3_list = my_list[1:] # 1, 2, 3

my_dict = {first3_list[i]: last3_list[i] for i in range(3)}

for key, value in my_dict.items():
    print(key, value)
