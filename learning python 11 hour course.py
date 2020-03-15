             ##-----PYTHON VISUALIZING-----##
import turtle         #turtle is a drawing board ,vector graphic which allows you to draw all over it.


a=turtle.Turtle()
a.speed(3)



### defining a function
def  square():
    a.forward(100)
    a.right(90)
    a.forward(100)       # { making a square}
    a.right(90)
    a.forward(100)
    a.right(90)
    a.forward(100)  

square()                 #calling a function 
#a.forward(100)
#square()

      ##------- if else statement------##
#elephant_weight=1000
#ant_weight=3
#if elephant_weight<ant_weight:
    #square()
#else:
    #a.forward(100)


        ##-------while loop-------##      {when we don't know when something is going to end}
b='happy'
#while b=='happy':            #infinite loop
    #a.forward(10)


        ##---------for loop------##    {when you have the idea how many times you are gonna do something }
for i in range(4):
    square()                # numbering in computer starts from 0 to n-1.}


               ##---------Data Types--------## {a way such that computer can understand data.}

#string 
z='hello'
print(z)                         

#integer
1,2,3,4,5

#boolean
True
False

#float
2.3, 3.088


                   ##----------CASTING IN PYTHON---------##
       #        {changing from one datatype to another datatype}
x=1
type(x)
str(x)
float(x)

y='hello'
type(y)
int(y)                  #i.e you can't change character string into an integer.

z='3'
type(z)                        
int(z)                  # but if number is a string it can be converted into int.


# you only print strings to the screen not numbers
print(5)                # before printing the number 5 is casted to a string type.

bool(5)
bool(0)                # anything which is not zero is true


                       # STRINGS IN PYTHON
k='hello world'
print(k[0])            # this will give the element of k at index(position) 0.


                       
                       # LISTS  {DATA STRUCTURE}
l_1=[1,2,3]                       
list_1=[0,1,2,3,'hello',3.4, True,[l_1]]
print(list_1)
print(list_1[2])              #indexing

                       # different fns of lists
team=['james','jonh','carry']
print(team)                       
 #now i want to add another name to a team
team.append('roy')           
#append means adding something in the end.
print(team)


team.insert(0,'rock')          # insert is used to insert additional info at a particular spot .team
print(team)

team.remove('jonh')         #this will remove jonh from the team list
print(team)

team.reverse()         #reversing the list 
print(team)

numbers=[5,4,7,1,2,8]
print(numbers)
# arranging in ascending order
numbers.sort()            #by default it arranges in  ascending order.team
print(numbers)
numbers.reverse()
print(numbers)

for i in numbers:
    print(i)
