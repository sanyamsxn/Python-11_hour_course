import re
text="a random string"          #creating a regular expression
pattern=re.compile("[random]")    #creating a pattern which will be used to find out the object
result=pattern.search(text)     #using pattern to check in text.
print(result) 



google="trees are beautiful"
pattern_1=re.compile("[tdm]")
result_1=pattern_1.search(google)
print(result_1)
#it will just printout t as it only find the first match and then stops, even it matches e and 
#s also but it finds t first and then terminates.



# instead of (abc) we can write (a-c)
random_1="random string_1"
pattern_2=re.compile("[a-zA-Z0-9]+")    #we can also add no.s
#here + sign reads multiple letters but when space occurs it stops as space is neither upper
#case or lower case.
result_2=pattern_2.search(random_1)
print(result_2)
#it will printout A as it compiles both from a-z and A-Z ...as A occurs first, it then terminates
