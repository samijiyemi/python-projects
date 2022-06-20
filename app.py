def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age can't be zero or less")
    return 10 / age
