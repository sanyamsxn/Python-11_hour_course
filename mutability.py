#mutability - changeable
#immutability- unchangeable
t=(1,2,[1,2,3])
print(t)
t[0]=1           #you can't change element in tuple as it is immutable.
t[2][0]=7        #we are just entering into list and changing the element.
print(t)