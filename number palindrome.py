n=int(input("Enter a number="))
rev=0
temp=n
while temp>0:
    rem=temp%10
    rev=rev*10+rem
    temp//=10
if temp==rev:
    print(n,"is a Palindrome")
else:
    print(n,"is not a Palindrome")
