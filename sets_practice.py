#######----------SETS------------####
#any bunch of things stored in braces {} is known as sets , it can't hold duplicates.
# there is no sequential order of elements in sets, they are arranged randomly

list_1=[1,2,3,4,2,1]
print(list_1)
sets_1=set(list_1)             #casting list into sets to get rid of duplicates in list.
print(sets_1)



s={'blueberry','raspberry'}
print(s)
s.add('strawberry')
print(s)


library_1={'harry porter','killing a mockingbird','power of subconscious mind'}
library_2={'harry porter','think and grow rich'}
new=library_1.union(library_2)      #union()  method returns a new set with all items from both sets, no dup.
print(new)


library_3={'harry porter','killing a mockingbird','power of subconscious mind'}
library_4={'harry porter','think and grow rich'}
library_3.update(library_4)      #update()  method update the existing set with all items from both sets, no duplicates
print(library_3)


library_12={'harry porter','killing a mockingbird','power of subconscious mind'}
library_21={'harry porter','think and grow rich'}
new_1=library_12.intersection(library_21)   #intersection()  method returns a new set with common element from both sets, no dup.
print(new_1)


diff=library_1.difference(library_2)            #difference() tells how library_1 is different from library_2
print(diff)


library_1.clear()
print(library_1)                               #clear() method clear the whole set it does not take any parameter.







