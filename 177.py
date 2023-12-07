my_list = ["가", "나", "다", "라"]

reverse_list = my_list[::-1]
first3_rvs_list = reverse_list[:3]
last3_rvs_list = reverse_list[1:]

for i in range(3):
    print(first3_rvs_list[i], last3_rvs_list[i])
