def count_occurrences(my_list, num):
    count = 0
    for i in my_list:
        if i == num:
            count += 1
    return count

my_list = [1, 2, 3, 2, 4, 2, 5]
num = 2
print("Number of occurrences of", num, "in the list:", count_occurrences(my_list,num))