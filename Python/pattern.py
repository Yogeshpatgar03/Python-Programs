def construct_pattern():
    n = 3  # Number of rows in the pattern
    width = 2 * n - 1  # Width of the pattern

    for i in range(n):
        for j in range(width):
            if j >= n - i - 1 and j < width - (n - i - 1):
                print("8", end=" ")
            else:
                print(" ", end=" ")
        print()

    for i in range(n - 2, -1, -1):
        for j in range(width):
            if j >= n - i - 1 and j < width - (n - i - 1):
                print("8", end=" ")
            else:
                print(" ", end=" ")
        print()

construct_pattern()


