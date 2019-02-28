#WAP to print various patterns

def Pattern1(n):
    print 'Pattern1:'
    for i in range(1,n+1):
        if i <= 4:
            for j in range(1,i+1):
                print j,
        else:
            for j in range(1,n-i+2):
                print j,
        print('')

def Pattern2(n):
    print 'Pattern2:'
    for i in range(1,n+1):
        var=i
        for j in range(1,i+2):
            print var,
            var += i
        print('')

def Pattern3(n):
    print 'Pattern 3:'
    for i in range(1,n+1):
        var=n-i
        for j in range(1,n-i+2):
            if j <= var:
                print var,
                var -= 1
            else:
                print '*',  
        print('')
    

def main():
    Pattern1(7)
    Pattern2(4)
    Pattern3(5)


if __name__ == '__main__':
    main()

'''
>>> 
== RESTART: C:\Users\Admin\Desktop\Python_2019\patterns\hw_9_2\patterns2.py ==
Pattern1:
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 
1 2 
1 
Pattern2:
1 2 
2 4 6 
3 6 9 12 
4 8 12 16 20 
>>>  
'''
