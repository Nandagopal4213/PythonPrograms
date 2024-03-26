def filter_by_type(list_to_test, type_of):
    return [n for n in list_to_test if isinstance(n, type_of)]

myList = [ 4,'a', 'b', 'c', 1, 'd', 3]
nums = filter_by_type(myList,int)
strs = filter_by_type(myList,str)
print(nums)
print(strs)
