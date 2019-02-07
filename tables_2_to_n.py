#WAP to accept an integer 'n' from user and print tables from 2 to n

n=input('Enter an integer:')

for x in range(2,n+1):
    print("Table of "+str(x)+":\n")
    for y in range(1,11):
        z = x*y
        print(str(x)+"*"+str(y)+"="+str(z))
    print('\n')
