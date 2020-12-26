# variable are the c ontainer in which we store data temprary bases
# variable is name as any nme as you want but it can't start with numerical
# and no space in between like { var of name ---> give error} correct{varofname/ var_of_name}

var1 = "amg"     # string
var2 = "world"   # string
var3 = 3         # int
var4 = 3.56      # float
var5 = "45"   # string

print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))
print(type(var5))

print(var1+var2)    #return string
# print(var1+var3)  #return error because str and int can't add
print(var3+var4)    #return value
print(var1+var5)    #return string here var5 -->45 is stored as string
# print(var3+var5)    #return error because str and int can't add

# Type casting type()
# type is process in which we convert the data into desired datatype
var6 = int(var5)
print(type(var6))
print(var6)



