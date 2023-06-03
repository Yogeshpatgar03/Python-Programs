my_list = []
for i in range(20):
    my_list.append(int(input("Enter a number: ")))

sum = 0
for num in my_list:
    sum += num

average = sum / len(my_list)

print("Sum:", sum)
print("Average:", average)