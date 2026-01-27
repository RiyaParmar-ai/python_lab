#1.Calculate simple interest
p=float(input("Enter principal amount: "))
r=float(input("Enter rate of interest: "))
t=float(input("enter time: "))
si=(p*r*t)/100
print("simple interest is: ",si)
#2.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Maximum number is: ",a)
else:
    print("Maximum number is: ",b)    
#3.
i=1
while i<5:
    print(i) 
    i=i+1
text="hello"
length=len(text)
print("length of string: ",length)
print("hello welcome to python")
text="python"
print(text[0])
text="python"
print(text[5])
num = int(input("Enter a number: "))
if num>0:
    print("positive number")
elif num<0:
    print("negative number")
a=4
b=5
c=8
sum=a+b+c
print(sum)
a=input("enter : ")
print(a)        
