# string is nothing but a data type which is use to do spcefic operation 
var1 ='same eggs'
var2 ='same eggs\'t'
var3 ="same eggs't"
var4 ='"same," eggs'

var5 ='same\n eggs' # \n use for new line 
var6 =r'c:\sum\name' # r use for raw string 

print(var1,"\n",var2,"\n",var3,"\n",var4,"\n",var5,"\n",var6)
print("""\
    multi line
    print
    option
""")

# string operation

var7 = 3*'amg'+'cool'    # amg print 3 time
var8 = 'aditya''malik'   # string catinate without using + 
var9 = 'amg'
var10 = var9+'cool'
# var11 = ('un'*3)'ium'   #throw error 
print(var7,"\n",var8,"\n",var10,)

print("hi every on this is", end='amg')
print("is cool boy")

print("hi every on this is", end=' ')
print("aditya is cool boy")

print("hi every on this is", "amg")
print("is cool boy")

# sring slicing

a ='aditya malik gupta'
print(a[0])     #accessing with index 
print(a[7])     #accessing with index
print(a[-2])    #accessing with negative index
print(a[-5])    #accessing with negative index
print(a[0:2])   #accessing with index first will be starting and second ending index from were you want
a = a[:2] + a[2:]  # default starting index is 0 and second ending index is length of sting
print(a)
print(a[-2:])      #accessing with negative index   

#   a  d  i  t  y  a  
#  0  1  2  3  4  5 6 
# -6 -5 -4 -3 -2 -1

print(a[::2])   # third index is for escape index default is 1 if we enter 2 (n-1) it will escape 1 index after each index
print(a[::-1])  # revers string
print(a[::-2])  # revers string and escape 1 index

# some function 
# The capitalize() method returns a string where the first character is upper case.

txt = "hello, and welcome to my world."

x = txt.capitalize()

print (x)

# The casefold() method returns a string where all the characters are lower case.
# This method is similar to the lower() method, but the casefold() method is stronger, more aggressive, meaning that it will convert more characters into lower case, and will find more matches when comparing two strings and both are converted using the casefold() method.

txt = "Hello, And Welcome To My World!"

x = txt.casefold()

print(x)

# The center() method will center align the string, using a specified character (space is default) as the fill character.
# string.center(length, character)
# length :-	Required. The length of the returned string
# character:-	Optional. The character to fill the missing space on each side. Default is " " (space)
# Example
# Using the letter "O" as the padding character:

txt = "banana"

x = txt.center(20, "-")

print(x)



# The count() method returns the number of times a specified value appears in the string.
# Syntax :- string.count(value, start, end)
# Parameter	Description
# value :- Required. A String. The string to value to search for
# start :- Optional. An Integer. The position to start the search. Default is 0
# end	  :- Optional. An Integer. The position to end the search. Default is the end of the string
# Example
txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")

print(x)
# Example
# Search from position 10 to 24:

txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple", 10, 24)

print(x)



