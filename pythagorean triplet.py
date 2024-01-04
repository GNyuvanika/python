limit=int(input("Enter the end limit="))
for a in range(1,limit+1):
    for b in range(a+1,limit+1):
        c=(a**2+b**2)**0.5
        print(f"Pythagorean triplet: ({a}, {b}, {int(c)})")
