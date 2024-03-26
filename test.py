L = [12, 156,4788, 12238]
odd = [i for i in  L  if len(str(i))%2 ==0 ]
even = [i for i in  L  if len(str(i))%2 !=0 ]
print(odd)
print(even)


