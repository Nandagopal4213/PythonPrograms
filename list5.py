# Program in Python to Find the Smallest and the Largest List

temp = []

num = int(input("how many nos?:"))

for x in range(num):
    numbers= int(input("ENter nos:"))
    temp.append(numbers)

print("\nMax element in list:",max(temp))
print("min element in list:",min(temp))