'''n=int(input("Enter a number="))
for i in range(2,n):
    if(n%i==0):
        print("Not Prime")
        break
    else:
        print("Prime")
        break'''

def prime(n):
    for i in range(2,n):
        if n%i==0:
            print("Not prime")
            break
        else:
            print("Prime")
            break
n=int(input("Enter a number="))
prime(n)
