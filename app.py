def fizz_buzz(num):
    if (num % 3 == 0) and (num % 5 == 0):
        return "fizzbuzz"
    if num % 3 == 0:
        return "fizz"
    if num % 5 == 0:
        return "Buzz"
    return num


print(fizz_buzz(15))
