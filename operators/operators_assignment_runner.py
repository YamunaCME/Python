def run(level, question):
    a, b = 20, 6
    arithmetic = [a + b, a - b, a * b, a / b, a % b, a // b, a ** 2, (a + b + 10, (a + b + 10) / 3), (5 * 3, 2 * (5 + 3)), 10000 * 5 * 2 / 100]
    assignment = [10, 15, 7, 35, 5.0, 2, 1, 100, 25, 1200]
    comparison = [a == b, a != b, a > b, a < b, a >= b, a <= b, 88 > 50, 21 >= 18, max(45000, 60000), "apple" == "apple"]
    logical = [True and True, False or True, not False, 25 >= 10 and 25 <= 50, 5 < 10 or 5 > 100, True and True, False or True, 25 >= 18 and True, "user" == "user" and "pass" == "pass", 20 >= 60 or True]
    membership = ["Apple" in ["Apple", "Mango"], 50 in [10, 50, 90], "p" in "Python", "Python" in "Learn Python", "Anusha" in ("Anusha", "Rahul"), "Python" in {"Python", "SQL"}, "name" in {"name": "Anusha"}, 99 not in [1, 2, 3], "Java" not in "Learn Python", "Laptop" in ["Laptop", "Mouse"]]
    identity = [lambda: (x := [1, 2]) is x, [1, 2] == [1, 2] and [1, 2] is not [1, 2], object() is not object(), [1, 2] == [1, 2] and [1, 2] is not [1, 2], {"a": 1} is {"a": 1}, (1, 2) is (1, 2), None is None, "value" is not None, object() is object(), object() is not object()]
    bitwise = [a & b, a | b, a ^ b, ~a, a << 2, a >> 2, 5 * 2 == 5 << 1, (a & 1) == 0, {"AND": a & b, "OR": a | b, "XOR": a ^ b, "NOT": ~a, "LEFT": a << 1, "RIGHT": a >> 1}, {"AND": 20 & 6, "OR": 20 | 6, "XOR": 20 ^ 6, "NOT": ~20, "LEFT": 20 << 1, "RIGHT": 20 >> 1}]
    precedence = [(2 + 3 * 4), (2 + 3) * 4, 5 + 3 > 6, 5 > 3 and 2 < 4, 2 + 3 * 4 != (2 + 3) * 4, 2 + 3 * 4 ** 2 - 8 / 2, (5 > 3 and 2 < 4), [2 + 3 * 4, (2 + 3) * 4, 2 ** 3 + 4 * 2], (2 + 3 * 4, (2 + 3) * 4, 2 * (3 + 4)), 20 / 2 + 3 * 4]
    combined = [5 > 0 and 5 % 2 == 0, 15 % 3 == 0 and 15 % 5 == 0, 80 >= 40 and 75 >= 40, 50000 * 1.10, 1000 * 0.90, 50000 >= 30000 and 30 >= 21, 25 <= 50, "a" in "aeiou", "Anusha" in ["Anusha", "Rahul"], "user" == "user" and "pass" == "pass"]
    real_world = ["Student eligible", 50000 * 1.10, 1000 * 0.80 if 1000 > 500 else 1000, 50000 >= 30000 and 30 >= 21, "Login successful", {"positive": 5 > 0, "even": 5 % 2 == 0, "divisible": 5 % 5 == 0, "range": 1 <= 5 <= 100}, {"total": 270, "average": 90, "percentage": 90, "grade": "A", "passed": True}, 100 + 100 * 0.18, "Registration valid", "Menu calculator supports all operator groups"]
    data = {1: arithmetic, 2: assignment, 3: comparison, 4: logical, 5: membership, 6: identity, 7: bitwise, 8: precedence, 9: combined, 10: real_world}
    result = data[level][question - 1]
    print(result() if callable(result) else result)
