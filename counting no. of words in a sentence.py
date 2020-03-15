#sentence='i like the name aaron because aaron is the best'
 #counting the occurence of words in a sentence

 # there are three methods to do this:
 
 

words_count={
    'i':1,
    'the':1,
    'best':2
}

## adding key and value in a dict.
print(words_count)
words_count['aaron']=2
print(words_count)


print(words_count.items())       # dict.items() - gives both key and values in a tuple
print(words_count.keys())        # dict.keys() - gives only keys
print(words_count.values())      # dict.values()- gives only values


## deleting something from dictionary using pop('key') method
(words_count.pop('the'))         # it will delete the key and value from dict 
print(words_count.pop('the'))    # it will print the value of the key sep.
print(words_count)
words_count.popitem()            # delete the last key and value.


