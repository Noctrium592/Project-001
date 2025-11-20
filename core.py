# calc_single.py
# Single-file simple calculator CLI - paste into Acode and run in Pydroid 3

import math

class CalculatorError(Exception):
    pass

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def truediv(a, b):
    if b == 0:
        raise CalculatorError("Division by zero")
    return a / b
def mod(a, b):
    if b == 0:
        raise CalculatorError("Modulo by zero")
    return a % b
def power(a, b): return a ** b
def sqrt(a):
    if a < 0:
        raise CalculatorError("Square root of negative number")
    return math.sqrt(a)

OPERATIONS = {
    '+': add, '-': sub, '*': mul, '/': truediv,
    '%': mod, '**': power, 'sqrt': lambda x: sqrt(x)
}

def parse_and_eval(text):
    text = text.strip()
    if not text:
        raise ValueError("Empty input")
    parts = text.split()
    if parts[0].lower() in ('exit','quit'):
        return "EXIT_CMD"
    if parts[0] in ('help','?'):
        return ("Examples:\n  2 + 3\n  10 / 2\n  5 ** 3\n  sqrt 16\nType 'exit' to quit.")
    if parts[0] == 'sqrt' and len(parts) == 2:
        a = float(parts[1])
        return OPERATIONS['sqrt'](a)
    if len(parts) == 3:
        a = float(parts[0])
        op = parts[1]
        b = float(parts[2])
        if op not in OPERATIONS:
            raise ValueError("Unsupported operator")
        return OPERATIONS[op](a,b)
    raise ValueError("Invalid format. Type 'help' for examples.")

def main():
    print("Simple Calculator — type 'help' for examples, 'exit' to quit")
    while True:
        try:
            user = input(">>> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye 👋")
            break
        if not user:
            continue
        try:
            res = parse_and_eval(user)
            if res == "EXIT_CMD":
                print("Bye 👋")
                break
            print(res)
        except CalculatorError as ce:
            print("Error:", ce)
        except ValueError as ve:
            print("Input error:", ve)
        except Exception as e:
            print("Unexpected error:", e)

if __name__ == "__main__":
    main()