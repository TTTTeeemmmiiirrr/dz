data = {10: 2, 2: 5, "123": 4, 18: 0, (): 15, 8: 4}
result = {}
errors = {}

for i, key in enumerate(data):
    try:
        a = int(key)
        b = int(data[key])
        if b == 0:
            raise ZeroDivisionError(f"Index {i}: division by zero")
        if b > 100:
            raise IndexError(f"Index {i}: b > 100")
        result[i] = a / b
    except Exception as e:
        errors[i] = str(e)
        result[i] = 0.0

print("Errors:")
for k, v in errors.items():
    print(f"{k}: {v}")

print("Results:")
for k, v in sorted(result.items(), key=lambda x: x[0]):
    print(f"{k}: {v}")
