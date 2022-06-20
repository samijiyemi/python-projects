from timeit import timeit

code1 = """

def calculate_xfactor(age):
     if age <= 0:
          raise ValueError("Age can't be zero or less")
     return 10 / age

try:
    print(calculate_xfactor(-1))
except ValueError as error:
    pass

"""

print("First Code=", timeit(code1, number=100))
