def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)

num_terms = int(input("Enter the number of terms: "))

if num_terms <= 0:
    print("Invalid input.")
else:
    print("Fibonacci sequence:")
    for i in range(num_terms):
        print(fibonacci(i))