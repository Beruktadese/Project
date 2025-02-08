# to accept three number form user and to find the average of the number

'''x=int(input("enter the number"))
y=int(input("enter the number"))
z=int(input("enter the number"))
a=x+y+z
b=a/3
print(b)
'''

# to find the persentage of female and male 
'''
F=int(input("enter the number of female"))   # f is stands for female
M=int(input("enter the number of male"))   #M is stands for male
k=F+M
L=F/k
print("the persentage of female is ",L)
P=M/k
print("the persentage of male is",P)
'''
# to chech if the number is posotive, negative or zero 
'''
num=int(input("entr the number"))
if num>0:
    print(num,"is posotive number ")
elif num==0:
    print(num,"is zero")
else:
    print(num,"is negative")
'''


# to  check if the number is even or odd
'''
num=int(input("enter the number"))
if num%2==0:
    print(num,"is even")
else:
    print(num,"is odd")
'''

# to find the leap year 
'''
year=int(input("enter the year"))
if year%400==0 and year%100==0:
    print("{0} is leap year".format(year))
elif year%4==0 and year%100!=0:
    print("{o} is leap year".format(year))
else:
    print("{0} is not leap year".format(year))
'''

# to checK the give number is prime or not prime
'''
count=0
num=int(input("enter the number"))
for i in range (1,num+1):
    if num%i==0:
        count=count+1
if count==2:
    print("the number is prime")
else:
    print("the number is not prime")
'''

# to find the prime number in the interval of 1- 100
'''
lower=1
upper=100
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)
'''

# to find the factorial of the number 
'''
factorial=1
n=int(input("enter the number"))
for i in range(1,n+1):
    factorial=factorial*i
print("factorial of %d is %d" %(n,factorial))
'''
# Write a Python Program to Find the Sum of Natural Numbers.
'''
num=int(input("enter the number"))
sum=0
for i in range(num):
    sum=sum+i
print(f"the sum of natural number is ",sum)
'''

# Write a Python Program to Find LCM.
'''
def compute_lcm(x,y):
    if x>y:
        greater=x
    else:
        greater=y
    while(True):
        if greater%x==0 and greater%y==0:
            lcm=greater
            break
        greater+=1
    return lcm
num1=int(input("enter the number"))
num2=int(input("enter the number"))
print(f"the lcm of the number is", compute_lcm(num1,num2))
 '''
 
 # Write a Python Program to Find HCF.
'''
def compute_hcf(x,y):
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range (1,smaller+1):
        if x%i==0 and y%i==0:
            hcf=i
    return hcf
num1=int(input("enter the number1"))
num2=int(input("enter the number 2"))
print("the hcf of the number is",compute_hcf(num1,num2))
'''


# Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal.
'''
num=int(input("enter the number"))
print("the decimal value of ", num,"is")
print(bin(num),"in binary")
print(oct(num),"in octal")
print(hex(num),"in hexadecimal")
'''

# Write a Python Program To Find ASCII value of a character
'''
char=str(input("enter the char"))
print("the ascii value of " + char + "is",ord(char))
'''

# Write a Python Program for cube sum of first n natural numbers
'''
def cub_sum(n):
    if n<=0:
        return 0
    else:
        total=sum([i**3 for i in range(1,n+1)])
        return total
n=int(input("enter the number"))
if n<=0:
    print("please enter the valid posotive number")
else:
    result=cub_sum(n)
    print(f"the cube number of the natural number is :,{result}")
    '''
    
# Write a Python Program to find sum of array
'''
arr=[1,3,4]
x=sum(arr)
print("the sum of the arr :",x)
'''

# Write a Python Program to find largest element in an array.
'''
list=[12,5343,23,678,43]
list.sort()
b=list[-1]
print(b)
'''

# Write a Python Program to Sort Words in Alphabetic Order
'''
my_str=input("enter the word")
words=[word.capitalize() for word in my_str.split()]
words.sort()
print("the sorted words are :")
for word in words :
    print(word)
'''
    
# Write a Python program to Multiply all numbers in the list.
'''
numbers=[2,4,5,8,9]
product=1
for i in numbers:
    product*=i
print("the product of the the number is :",product) 
'''

# Write a Python program to find smallest number in a list.
'''
list=[23,45,12,5,12,46,1,54]
list.sort()
x=list[0]
print('the smallest number of the list is :',x)
'''

# Write a Python program to print odd numbers in a List.
'''
list=[12,4,45,56,21,65,2,21,87]
x=[a for a in list if a % 2!= 0]
print("The odd number in the list is :",x)    
'''

# Write a Python program to Remove empty List from List.
'''
list=[[24,234],[],[343],[523],[]]
x=[i for i in list if i]
print("the number is :",x)
'''

# 