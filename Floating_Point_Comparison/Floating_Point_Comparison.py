def approx_equals(a, b):
    a = round(a, 5)
    b = round(b, 5)
    float_value=0.001
    return abs(a-b) < float_value

print(approx_equals(175.9827, 82.25))