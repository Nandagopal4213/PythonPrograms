# Write a Python Program to Remove All Occurrences of an Element From a Given List

a = [8, 7,3,3,7,8,8,6,6,2]
out = list(set(a))
print(out)

# or

# Remove All Occurrences of an Element
List1 = [22, 24, 30, 22, 45, 67, 22, 30, 45]
item_to_remove = 22

print("The original list is : " + str(List1))


# function to remove all occurances
def remove_an_item(test_list, value):
    # remove the item for all its occurrences
    for x in test_list:
        if (x == value):
            test_list.remove(x)
    return test_list


# calling the function remove_items()
res_list = remove_an_item(List1, item_to_remove)

# updated list after removing 22
print("Updated list after remove operation: " + str(res_list))