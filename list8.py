# Write a Python Program to Interchange First and Last Elements of in a List

# swapping first & last items of a list - using indexing
List1 = ['XYZ', 'ABC', 'xyz', 'abc']
print("Original List:", str(List1))

List1[0], List1[-1] = List1[-1], List1[0]

# updated list
print("List after swapping:", str(List1))
