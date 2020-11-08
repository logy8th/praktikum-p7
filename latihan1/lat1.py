for row in range(10):
    for col in range(10):
        number = row + col
        if number < 10:
            empty = "  "
        else:
            empty  = " "
        print(empty, number, end = '')
    print()