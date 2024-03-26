# Write a Python Program to Remove Multiple Empty Strings From a List of Strings

# Using remove()
List1 = ['', 'ABC', 'xyz', '', 'abc', 'XYZ']
print("Original List:", str(List1))

# iterate & remove ''strings
while ("" in List1):
    List1.remove("")

# updated list
print("List after removing empty strings:", str(List1))
