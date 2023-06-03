list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

merged_list = []

i = 0
j = 0

while i < len(list1) and j < len(list2):
    if list1[i] <= list2[j]:
        merged_list.append(list1[i])
        i += 1
    else:
        merged_list.append(list2[j])
        j += 1

merged_list += list1[i:]
merged_list += list2[j:]

print("Merged and sorted list:", merged_list)