def approx_equals(a, b):
    a = round(a, 4)
    b = round(b, 4)
    return a == b

print(approx_equals(175.9827, 82.25))