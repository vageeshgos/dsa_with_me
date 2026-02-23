#while loop
'''
n=int(input("enter a number(n): "))
i=1
while i<=n:
    print(i)
    i=i+1
print()
#calculates the sum of all integers from 1 to n
m=int(input("enter a number(m): "))
sum=0
j=1
while j<=m:
    sum=sum+j
    j=j+1
print("sum=",sum)

#sum of  all  even numbers  

o=int(input("enter a umber(o): "))
sum1=0
k=1
while k<=o:
    if k%2==0:
        sum1=sum1+k
    k=k+1
print("sum of even numbers=",sum1)
#od 
while k<=o:
    if k%2!=0:
        sum1=sum1+k
    k=k+1
print("sum of odd numbers=",sum1)

#Fahrenheit to Celsius Conversion
print("Fahrenheit to Celsius Conversion")
p= int(input("how many temp"))
i=1
while i<=p:
    F=float(input("enter temp in f"))
    c=(5/9.0)*(F-32)
    print(f"{F}={c:.2f}")
    i=i+1


#Prime Number Checker
print("Prime Number Checker") '''
n = int(input("Enter an integer: "))
if n <= 1:
    print("Not Prime")
else:
    i = 2
    is_prime = True
    while i < n:
        if n % i == 0:
            is_prime = False
            break
        i = i + 1
    if is_prime:
        print("Prime!")
        temp = n
        digit_sum = 0
        while temp > 0:
            digit = temp % 10
            digit_sum = digit_sum + digit
            temp = temp // 10
        print("Sum of digits =", digit_sum)
    else:
        print("Not Prime")

        #You want Sum of all Prime Numbers up to N?
m= int(input("Enter an integer: "))
ii=2
sum1=0
while ii<=m:
    j=2
    prime_1=True
    while j<ii:
        if ii%j==0:
            prime_1=False
            break
        j=j+1
    if prime_1:
        sum1=sum1+ii
    ii=ii+1
print("sum of prime numbers=",sum1)