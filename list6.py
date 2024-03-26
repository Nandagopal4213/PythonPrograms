# Write a Python Program to Split a List in Half and Store the Elements in Two Different Lists
# using list slicing to split the list to half
List1 = [1, 'ABC', 2, 3, 'abc', 'XYZ', 4]

# offset of middle element is 2
print("The first half of the list", List1[:3])
print("The second half of the list", List1[3:])

# to separate strings and intergers and store in diffrent list using python

integers_list = []
strings_list = []

for item in List1:
    if isinstance(item, int):
        integers_list.append(item)
    elif isinstance(item, str):
        strings_list.append(item)

print("Integers List:", integers_list)
print("Strings List:", strings_list)