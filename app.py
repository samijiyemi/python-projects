l1 = ["eat", "sleep", "repeat"]
s1 = "geek"

obj1 = enumerate(l1)
obj2 = enumerate(s1)

print("Return Type:", type(obj1))
print(list(enumerate(l1)))

print(list(enumerate(s1, 2)))
print(type(s1))
