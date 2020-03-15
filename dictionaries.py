  ##-------------DICTIONARIES------##
   # organising data in a more organised way.
groceries={'bananas':6,'apples':10}
# here 'bananas' represents the key and "6" represents key value

#slicing in dictionaries is done by using key to get the value. lets see how it works.

print(groceries['bananas'])

#instead of indexing we can use get() method.
print(groceries.get('apples'))


print(groceries.get('mangoes'))  #but get() fn don't give us a key error it'll just pop up with a message "NONE"
#print(groceries['oranges'])      #it'll give a key error as the key "oranges " does not exist


contact_list={
    'joe':{'phone':124567,'email':wm@you.com},
    'mandy':{'phone':536723,'email':em@your.com},
}
print(contact_list['joe']['phone'])         #this means we are extracting phone no. from joe list which is in contact list.


