#WAP to print different patterns

def Pattern1(n):
    for i in range(1,n+1):
        var=i
        for _ in range(1,n-i+1):
            print ' ',
        for j in range(1,i*2):
            print(chr(var+64)),
            if j<i:
                var=var-1
            else:
                var=var+1
        print(' ')

def Pattern2(n):
    for i in range(1,n+1):
        for _ in range(1,n-i+3):
            print ' ',
        for j in range(1,i+1):
            print '*',
        print(' ')
            
        
def main():
    num=input('Enter a number:')
    Pattern1(num)
    Pattern2(num)

if __name__ == '__main__':
    main()
    

'''
>>> 
 RESTART: C:\Users\Admin\Desktop\Python_2019\Funtions\hw_2_3_feb\Patterns_eg.py 
Enter a number:4
      A  
    B A B  
  C B A B C  
D C B A B C D  
>>> 
'''
