size=int(input("Enter the size of the pattern: "))
rem=size
while rem>0:
    for i in range(size):
        print("*",end="")
    print()
    rem-=1


