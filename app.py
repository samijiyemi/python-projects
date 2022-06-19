products = [
    ("mug", 19),
    ("cup", 25),
    ("phones", 200),
    ("laptop", 27)
]

x = list(filter(lambda item: item[1] >= 20, products))
x_map = list(map(lambda item: item[1], products))
print(x_map)
print("*" * 100)
filtered = [item[1] for item in products if item[1] >= 20]
print(filtered)
print("*" * 100)
print(x)
