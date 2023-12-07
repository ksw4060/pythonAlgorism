
"""
price_list = [32100, 32150, 32000, 32500]
price_dict = {}
price_dict = {i: price_list[i] for i in range(4)}
print(price_dict)

for key, value in price_dict.items():
    print(key, value)
"""
price_list = [32100, 32150, 32000, 32500]
last3_price_list = price_list[1:]
index_list = [100, 110, 120]

price_dict = {index_list[i]: last3_price_list[i] for i in range(3)}
for key, value in price_dict.items():
    print(key, value)

