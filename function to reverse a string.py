def rev(s):
    return s==s[::-1]

s=input("Enter a string=")
res=rev(s)
if res:
    print("Palindrome")
else:
    print("Not a Palindrome")
print("Reversed string=",rev(s))


