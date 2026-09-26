from __future__ import annotations

from functools import reduce


def run(level, question):
    if level == 1:
        examples = [
            ("greet", lambda: print("Hello, Welcome to Python!")),
            ("welcome", lambda: print("Welcome, Anusha!")),
            ("add", lambda: print(10 + 5)),
            ("subtract", lambda: print(10 - 5)),
            ("multiply", lambda: print(10 * 5)),
            ("divide", lambda: print(10 / 5)),
            ("square", lambda: print(5 ** 2)),
            ("cube", lambda: print(3 ** 3)),
            ("is_even", lambda: print("Even" if 8 % 2 == 0 else "Odd")),
            ("is_positive", lambda: print("Positive" if 5 > 0 else "Negative" if 5 < 0 else "Zero")),
        ]
        name, action = examples[question - 1]
        print(f"{name} output:"); action()
    elif level == 2:
        values = [10, 5, 8]
        results = [
            ("Student: Anusha, Marks: 88",), (max(values),), (min(values),),
            (120,), (True,), ("madam" == "madam"[::-1],), (len("Python"),),
            (sum(c in "aeiou" for c in "Education"),), (sum([1, 2, 3, 4]),), (max(values),),
        ]
        print(results[question - 1][0])
    elif level == 3:
        values = [10, 20, 30, 40, 20]
        results = [
            {"sum": 15, "difference": 5, "product": 50, "division": 2},
            "A", sum(values) / len(values), [x for x in values if x % 2 == 0], [x for x in values if x % 2],
            "Python"[::-1], "level" == "level"[::-1], list(dict.fromkeys(values)), sorted(set(values))[-2], (max(values), min(values)),
        ]
        print(results[question - 1])
    elif level == 4:
        values = [10, 20, 30, 41, 52]
        results = [
            110, {"name": "Anusha", "marks": 88}, 50, sum(values), max(values),
            {"name": "Rahul", "department": "IT"}, {"name": "Anusha", "marks": [88, 91]}, sum(values) / len(values),
            {"name": "Anusha", "course": "Python"}, {"even": [x for x in values if x % 2 == 0], "odd": [x for x in values if x % 2]},
        ]
        print(results[question - 1])
    elif level == 5:
        def factorial(n): return 1 if n <= 1 else n * factorial(n - 1)
        def fibonacci(n): return n if n < 2 else fibonacci(n - 1) + fibonacci(n - 2)
        results = ["Inner function works", (lambda x: x * 2)(5), factorial(5), [fibonacci(x) for x in range(6)], sum(range(1, 6)), "Python"[::-1], (lambda x: x*x)(5), (lambda x: "Even" if x % 2 == 0 else "Odd")(7), (lambda a,b: max(a,b))(4, 9), (lambda l,w: l*w)(5, 3)]
        print(results[question - 1])
    elif level == 6:
        numbers = [4, 2, 8, 2, 6]
        students = {"Anusha": 88, "Rahul": 76, "Priya": 91}
        sentence = "python makes python learning easy"
        results = [(min(numbers), max(numbers)), sum((1, 2, 3)), len({1, 2, 2, 3}), max(students, key=students.get), [k for k,v in students.items() if v > 50], sorted(["Neha", "Anusha", "Rahul"]), {"even": 4, "odd": 1}, {c: "hello".count(c) for c in set("hello")}, {w: sentence.split().count(w) for w in set(sentence.split())}, {x: x*x for x in numbers}]
        print(results[question - 1])
    else:
        projects = ["Calculator", "Student Marks", "Employee", "Banking", "Shopping Cart", "Contacts", "Number Utility", "Student Grades", "Library", "Menu-Driven Application"]
        print(f"Mini project ready: {projects[question - 1]}")
