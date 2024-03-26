dict={1:'hello',2:'hai'}
dict[1]='bye'
print(dict)
a=["a","b","c"]
a[1:2]=[4]
print(a)

a=('a','b',1)
b=list(a)
b[1]=26
a=tuple(b)
print(a)