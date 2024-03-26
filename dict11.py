# dict compherehsion

keys =['a','b','c']
values =['1','2','3']

dict ={keys:values for (keys,values) in zip(keys,values)}
dict1 ={i:i+'1' for i in (keys)}

print(dict)
print(dict1)