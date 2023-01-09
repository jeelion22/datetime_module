def divide():
    try:
        a, b = map(int, input().split())
        c = a / b
        print(c)
    except ZeroDivisionError:
        print("Denominator can't be 0")
    except ValueError:
        print("Input should be an integer")


divide()
