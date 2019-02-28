#WAP to accept a string from user, and check if it is palindrome or not

def palindrome(s1):
    #s1=str(n1)
    rev_s1=reversed(s1)
    if list(s1) == list(rev_s1):
        print s1+' is a palindrome'
    else:
        print s1+' is not a palindrome'

def main():
    str1=input('Enter a string:')
    palindrome(str1)


if __name__ == '__main__':
    main()
    

'''
>>> 
 RESTART: C:\Users\Admin\Desktop\Python_2019\Funtions\hw_26_27_1\palindrome_string_func.py 
Enter a string:'rashmi'
rashmi is not a palindrome
>>> 
 RESTART: C:\Users\Admin\Desktop\Python_2019\Funtions\hw_26_27_1\palindrome_string_func.py 
Enter a string:'madam'
madam is a palindrome
>>> 
'''
