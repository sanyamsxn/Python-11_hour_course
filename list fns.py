digits=[0,1,2,3,4,5,6,7,8,9]
print(digits)
print(digits[2])
        ##---------------SLICING------------##
print(digits[0:9])            # 0 refers to 1st position and 9 refers to end of the list, but 9 here is exclusive.
print(digits[:9])
print(digits[::])             # slicing from start till the end.
print(digits[::2])            # here 2 refers to the size by which slicing has to be done.
print(digits[::-1])           # will began the slicing from backward of the list.
print(digits[5:0:-2])                      
print(digits[-len(digits)])
print(digits[5:9])


#strings list
strings="hello from the other side"
print(strings)
print(strings[:9:2])


# slicing with for loop         ,DYNAMIC SLICING
for i in range(len(digits)):
    print(digits[0:i])

for i in range(len(digits)):
    print(digits[i:i+3])