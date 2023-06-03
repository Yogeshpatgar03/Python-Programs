def gcd(num1, num2):
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1 % num2)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("GCD:", gcd(num1, num2))