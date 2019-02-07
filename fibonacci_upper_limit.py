#WAP to accept a number from the user and print the fibonacci series considering the number as the upper bound

def fibo(n):
    a=1
    b=1
    print a,b,
    c = a+b
    while c<n:
        c=a+b
        print c,
        a=b
        b=c
        
def main():
    num=input('Enter a number:')
    fibo(num)

if __name__ == '__main__':
    main()

'''
>>> 
 RESTART: C:/Users/Admin/Desktop/Python_2019/Funtions/hw_2_3_feb/fibonacci_upper_limit.py 
Enter a number:55
1 1 2 3 5 8 13 21 34 55
>>>
'''
