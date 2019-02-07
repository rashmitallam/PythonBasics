#WAP to accept a number from user and print it in simple word form
#Eg: 543 --> Five Four Three

def ReverseNum(n):
    rem=0
    rev=0
    while(n != 0):
        rem = n%10
        rev=rev*10+rem
        n=int(n//10)
    return rev

def NumToWord(num):
    n=ReverseNum(num)
    #print n
    while(n != 0):
        rem = n%10
        if rem == 0:
            print 'Zero ',
        elif rem == 1:
            print 'One ',
        elif rem == 2:
            print 'Two ',
        elif rem == 3:
            print 'Three ',
        elif rem == 4:
            print 'Four ',
        elif rem == 5:
            print 'Five ',
        elif rem == 6:
            print 'Six ',
        elif rem == 7:
            print 'Seven ',
        elif rem == 8:
            print 'Eight ',
        elif rem == 9:
            print 'Nine ',
        n=int(n//10)
    
def main():
    num=input('Enter a number:')
    NumToWord(num)


if __name__ == '__main__':
    main()


'''RESTART: C:/Users/Admin/Desktop/Python_2019/Funtions/hw_2_3_feb/num_to_word.py 
Enter a number:543
Five  Four  Three 
>>>'''



