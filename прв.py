result = {}
errors = {}


def divider(a, b, i):
    try:
        if a < b:
            raise ValueError(f"Index {i}: a < b")
        if b == 0:
            raise ZeroDivisionError(f"Index {i}: division by zero")
        if b > 100:
            raise IndexError(f"Index {i}: b > 100")
        result[i] = a / b
    except Exception as e:
        errors[i] = str(e)


data = {10: 2, 2: 5, "123": 4, 18: 0, (): 15, 8: 4}
for i, key in enumerate(data):
    divider(key, data[key], i)

print("Errors:")
for k, v in errors.items():
    print(f"{k}: {v}")

print("Results:")
for k, v in result.items():
    print(f"{k}: {v}")
