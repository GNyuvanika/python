n=int(input("Enter a number="))
sums=0
while n!=0:
    rem=n%10
    sums=sums+rem
    n//=10
print("Sum of Digits=",sums)
