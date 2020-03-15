import re
name="random string. myname123@website.com .some random text."
pattern=re.compile("[a-zA-Z0-9]+@[a-zA-Z0-9]+\.+[a-zA-Z0-9]+")     
#\. represents that treat period as period
result=pattern.search(name)   #search only searches for first occurance.
print(result)

# to look out for multiple occurance we can use 'findall' instead of search.



    #USING FINDALL
name_1="random string. myname123@website.com .  yourname222@company.net  .some random text."
pattern_1=re.compile("[a-zA-Z0-9]+@[a-zA-Z0-9]+\.+[a-zA-Z0-9]+")     
result_new=pattern_1.findall(name_1)   
print(result_new)
 
 #now it will print out both the emails.

 #we can use -_. as email contains these sometimes inside brackets and we have to use backslash
 #to treat it what it actually is.