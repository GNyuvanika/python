def calculate(p,n,r):
    si=(p*n*r)/100
    return si

p=int(input("Enter the principal amount="))
n=int(input("Enter the no.of years="))
g=input("Enter the gender(m/f)=")
sc=input("Senior citizen or not(y/n)=")

if sc=="y" and g=="f":
    r=12
    print("Simple interest",calculate(p,n,r))
elif sc=="y" and g=="m":
    r=10
    print("Simple interest",calculate(p,n,r))
elif sc=="n" and g=="f":
    r=10
    print("Simple interest",calculate(p,n,r))
else:
    r=10
    print("Simple interest",calculate(p,n,r))

    




      
