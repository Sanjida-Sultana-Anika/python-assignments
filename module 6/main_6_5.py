
def remove_uneven(full_list):
    even_list = []
    for i in full_list:
        if i % 2 == 0:
            even_list.append(i)
    return even_list


mylist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print("Original list:", mylist)
print("Even list:", remove_uneven(mylist))
