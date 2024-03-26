# removing duplicated from the list using set() 

# initializing list 
x = [11, 15, 13, 16, 13, 15, 16, 11] 
#print ("The list is: " + str(x)) 

# to remove duplicated from list 
x = list(set(x)) 

# printing list after removal 
# ordering distorted
print ("The list after removing duplicates: " + str(x))