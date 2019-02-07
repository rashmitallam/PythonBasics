#WAP to print various patterns of stars

def Pattern1(n):
    for i in range(1,n+1):
        for _ in range(1,i):
            print ' ',
        for _ in range(1,n-i+2):
            print '*',
        print(' ')


def Pattern2(n):
    for i in range(1,n+1):
        for _ in range(1,n-i-3):
            print ' ',
        for _ in range(1,n-i+2):
            print '*',
        print(' ')

def Pattern3(n):
    for i in range(1,n+1):
        var=i
        for _ in range(1,n-i+1):
            print ' ',
        for j in range(1,2*i):
            print (chr(var+64)),
            if j<i:
                var -= 1
            else:
                var += 1
        print(' ')
            
def Pattern5(n):
    for i in range(1,n+1):
        if i <=3:
            for _ in range(1,n-i-1):
                print ' ',
        else:
            for _ in range(1,i-2):
                print ' ',
        if i <=3 :
            for _ in range(1,(i*2)):
                print '*',
        else:
            for _ in range(1,n-i+3):
                print '*',
        print (' ')
    
                       


def main():
    Pattern1(4)
    Pattern2(4)
    Pattern3(4)
    Pattern5(5)

if __name__ == '__main__':
    main()
