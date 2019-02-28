#WAP to accept a number from user, and check if it is palindrome or not

def palindrome(n1):
    s1=str(n1)
    rev_s1=reversed(s1)
    if list(s1) == list(rev_s1):
        print s1+' is a palindrome'
    else:
        print s1+' is not a palindrome'

def main():
    num1=input('Enter a number:')
    palindrome(num1)


if __name__ == '__main__':
    main()
    
'''
>>> 
 RESTART: C:\Users\Admin\Desktop\Python_2019\Funtions\hw_26_27_1\palindrome_num_func.py 
Enter a number:1234321
1234321 is a palindrome
>>> 
 RESTART: C:\Users\Admin\Desktop\Python_2019\Funtions\hw_26_27_1\palindrome_num_func.py 
Enter a number:435467
435467 is not a palindrome
>>> 
'''
