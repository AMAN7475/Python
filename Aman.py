"""num = int(input("Enter No : "))
x = num

factors = []
prime = []
factors_repeat = []

for i in range(2,x):
	if x % i == 0:
		factors.append(i)


print("Factors : ", factors)"""


# SQUARE ROOT #
"""var_a = int(input("Enter No : "))
var_b = var_a ** (1/2)

print("Square Root of {} is {}".format(var_a,var_b))"""


# SQUARE AND CUBE #
"""var_a = int(input("Enter Value : "))
var_b = var_a * var_a  #for square
print(var_b)
#var_b = var_a * var_a * vare_a #for cube"""


# EVEN NO AND ODD NO #
"""a = int(input("Enter No : "))
b = a % 2

if b == 0:
	print ("{} is even no".format(a))

else:
	print ("{} is odd no".format(a))"""	

# DIVISIBLE BY 5 OR NOT #
"""a = int(input("Enter No : "))	
b = a % 5

if b != 0:
	print ("{} is not divisible by 5".format(a))

else:
	print("{} is divisible by 5".format(a))"""


# HIGHEST AMONG 3 GIVEN NO #
"""a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

if a == b == c:
	print("All three are same")

elif a >= b and a >= c :
	print(a)

elif b >= a and b >= c :
	print(b) 	

else:
	print(c)"""


# DRINK SELECETION ON BASIS OF TEMPERATURE # 
"""temp = int(input("Enter Temperature : "))

if temp <= 25 :
	print("I will have hot coffee ")

elif temp > 25 and temp <= 35:
	print("I will have tea")

else:
	print("I will have cold coffee")"""

# NESTED-IF CONCEPT #
"""a = int(input("Enter Value a : "))
b = int(input("Enter Value b : "))
c = int(input("Enter Value c : "))
least = a 

if b < least:
    least = b
    if c < least:
        least = c
    print("Least:", least)

else:
    if c < least:
        least = c
    print("Least:", least)"""


"""a = int(input("Enter Value a: "))
b = int(input("Enter Value b: "))
c = int(input("Enter Value c: "))
d = int(input("Enter Value d: "))
e = int(input("Enter Value e: "))

least = a

if b < least:
    least = b
    if c < least:
        least = c
        if d < least:
            least = d
            if e < least:
                least = e
    
    print("Least:", least)

elif c < least:
    least = c 
    if d < least:
        least = d 
        if e <least:
            least = e 
    print("Least:", least)

elif d < least:
    least = d
    if e < least:
        least = e 
    print("Least:", least) 
    9
elif e < least:
    least = e
    print("Least:", least)

else:
    least = a 
    print("Least:", least)"""              


 #TABLE OF USER DEFINED VALUE#
"""x = int(input("Enter No : "))
y = 0
for i in range(1,11):
    y = y + x
    print ("{} * {} = {}".format(x,i,y))"""


#FACTORIAL#
"""x = int(input("Enter No : "))
y = 1

for i in range(1,x+1): #(or (x,1,-1))
        y = y * i 
        print("{} * {} ={}".format(x,i,y))"""


#AVERAGE#
"""x = int(input("Enter No of Values : "))
sum = 0

for i in range(x):
    y = int(input("Enter No : "))
    sum = sum + y

avg =  sum/x

print("Average of {} = {}".format(y,avg))"""   


#PRIME OR COMPOSITE NO#
"""x = int(input("Enter No : "))
for i in range(2,x):
    if x % i == 0:
        print("It is a composite No")
        break
else:
    print("It is a prime No") """

#PERMUTATION USING FOR LOOP#
"""n = int(input("Enter value of n:"))
r = int(input("Enter value of r :"))

fact_n = 1
for i in range(1,n+1) :
    fact_n = fact_n * i

fact_nr = 1
for j in  range(1,n-r+1):
    fact_nr = fact_nr * j

    Permutation = fact_n/ fact_nr

    print("Permutation of {} over {} = {}". format(r,n,Permutation))"""


"""n = int(input("Enter value of n : "))
r = int(input("Enter value of r : "))  
a = n - r 

b = 1
for i in range(1,n+1):
    b = b * i 
print(b)

c = 1
for j in range(1,a+1):
    c = c * j 
print(c) 

permutation = b / c 

print("Permutation of {} over {} = {}".format(n,r,permutation))""" 


#COMBINATION USING FOR LOOP#
"""n = int(input("Enter value of n : "))
r = int(input("Enter value of r : "))  
a = n - r 

b = 1
for i in range(1,n+1):
    b = b * i 
print(b)

c = 1
for j in range(1,a+1):
    c = c * j
print(c) 

d = 1
for k in range(1,r+1):
    d = d * k

print(d)

combination = b/(d*c)

print("Combination of {} over {} = {}".format(n,r,combination))"""


#PERMUTATION USING WHILE LOOP#
"""n = int(input("Enter value of n : "))
r = int(input("Enter value of r : "))

fact_n = 1
i = 1 
while i <= n:
    fact_n = fact_n * i
    i +=1 
    
fact_nr = 1
j = 1 
while j <= r:
    fact_nr = fact_nr * j
    j +=1 

Permutation = fact_n/fact_nr

print("Permutation of {} over {} = {}".format(n,r,Permutation))"""

#Prime No Checking by While Loop#
"""x = int(input("Enter No : "))
i = 2

while i < x:
    if x % i == 0:
        print("{} is composite".format(x))
        break
    i += 1      
else:
    print("{} is prime".format(x))"""


"""x = int(input("Enter value : "))
y = 2

z = x // y 

while x == 1:
    print(z)"""

"""l = int(input("Enter length : "))
b = int(input("Enter breadth : "))
h = int(input("Enter heigth : "))

Paint_Coverage = int(input("Enter Paint Coverage  : "))

Surface_Area = (l*b)+ 2*(b*h)+ 2*(h*l)

#Area = l*b

#Paintable_Area = (Surface_Area - Area)

Paint_Requirement = Surface_Area/Paint_Coverage

print("Paint Requirement for given room",Paint_Requirement)"""


# Function to convert float value into integer value 
"""def convert_to_int(value):
    if value.is_integer():
        return int(value)
    else:
        return value 

x = float(input("Enter Value : "))
y = convert_to_int(x)

print(y)""" 


"""def add(value_1,value_2):
    return (value_1 + value_2)

def substract(value_1,value_2):
    return (value_1 - value_2)

def multiply(value_1,value_2):
    return (value_1 * value_2)

def divide(value_1,value_2):
    return (value_1 / value_2)      

def convert_to_integer(value):
    new = value // 1

    aman = value - new 

    if aman == 0.0:
        return(int(value))

    else:
        return(value)   

def AMAN_R(): 
    select = int(input("Select operation among 1,2,3,4 : "))

    if select == 1:
        print ("{} + {} = {}".format(Num_1,Num_2,convert_to_integer(add(Num_1,Num_2))))

    elif select == 2:
        print ("{} - {} = {}".format(Num_1,Num_2,convert_to_integer(substract(Num_1,Num_2))))
        
    elif select == 3:
        print ("{} * {} = {}".format(Num_1,Num_2,convert_to_integer(multiply(Num_1,Num_2))))
            
    elif select == 4:
        print ("{} / {} = {}".format(Num_1,Num_2,convert_to_integer(divide(Num_1,Num_2))))  

    else:
        print("Invalid Input")
        AMAN_R()     

Num_1 = float(input("Enter 1st Number : "))
Num_2 = float(input("Enter 2nd Number : "))

print("Select among following operations")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")

aman = True
while aman:

    AMAN_R()

    next_calculation = input("Want to do next calculation ? Y/N : ")
    if next_calculation == "N":
        aman = False"""

def divisiblity():
    value = int(input("Enter No : "))

    if value % 3 == 0 and value % 5 == 0:
        print ("fizz, buzz")
        return divisiblity()

    elif value % 3 == 0:
        print("fizz")
        return divisiblity()

    elif value % 5 == 0:
        print ("buzz")
        return divisiblity()  

    else:
        print ("Invalid Input,try again")
        return divisiblity() 

print(divisiblity())


    