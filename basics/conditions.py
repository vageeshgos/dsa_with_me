#conditions  
#if statement
a= int(input("enter a value for a: "))

if a>0:
    print("a is positive")
else:
    print("a is negative")
# if  else statement
b= int(input("enter a value for b: "))
if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")

#elif statement
c= int(input("enter a value for c: "))
if c>0:
    print("c is positive")
elif c<0:
    print("c is negative")
else:    print("c is zero")
#camparing two  numbers  
d=int(input("enter a value for d: "))
e=int(input("enter a value for e: "))
if d>e:
    print("d is greater than e")
#elif d<e:
   # print("d is less than e")
#else:
   # print("d is equal to e")
#else:
 #   print("d is less than e")
if d<e:
    print ("e is  grater ")

    #Character Type Checker (Uppercase, Lowercase, or Digit)
f=input("enter a character: ")
if 'A' <= f <= 'Z':
        print("f is an uppercase letter")
elif 'a' <= f <= 'z':
        print("f is a lowercase letter")
elif '0' <= f <= '9':
        print("f is a digit")
else:
        print("f is a special character") 
