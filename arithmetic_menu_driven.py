#Menu driven program for arithmetic operations

#print('Free fall code at begin')

def add(n1,n2):
    sum=n1+n2
    print 'Sum of two numbers is:',sum

def sub(n1,n2):
    diff=n1-n2
    print 'Difference between two numbers is:',diff

def mul(n1,n2):
    prod=n1*n2
    print 'Multiplication of two numbers is:',prod

def div(n1,n2):
    div=n1/n2
    print 'Division of two numbers is:',div

'''def main():
    print('Menu:')
    print('1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit\n')
    ch=input('Enter your choice:')
    n1=input('Enter 1st number:')
    n2=input('Enter 2nd number:')
    if ch == 1:
        add(n1,n2)
    elif ch == 2:
        sub(n1,n2)
    elif ch == 3:
        mul(n1,n2)
    elif ch == 4:
        div(n1,n2)
'''

def ArithmeticOperations():
    ch = 0
    while ch != 5:
        ch = Menu()
        n1=input('Enter 1st number:')
        n2=input('Enter 2nd number:')
        if ch == 1:
            add(n1,n2)
        elif ch == 2:
            sub(n1,n2)
        elif ch == 3:
            mul(n1,n2)
        elif ch == 4:
            div(n1,n2)
        else:
            break

def Menu():
    while(True):
        print("\nMenu:")
        print('''1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit\n''')
        ch=input('Enter your choice:')
        if (ch>0 and ch<5):
            return ch

def main():
    #ch=Menu()
    ArithmeticOperations()

if __name__ == '__main__':
    main()






























    
