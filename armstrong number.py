n=int(input("Enter a number="))
sums=0
temp=n
while temp>0:
    rem=temp%10
    sums=sums+(rem**3)
    temp//=10
if(sums==n):
    print("Armstrong number")
else:
    print("Not an armstrong number")
