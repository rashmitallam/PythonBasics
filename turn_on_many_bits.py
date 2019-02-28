#WAP to accept a number from user and number of bits to turn ON from givrn position

def TurnOnBits(n,sp,c):
    x=2**c-1
    x=x<<(sp-c)
    return n|x

def main():
    num=input('Enter a number:')
    print bin(num)
    start_pos=input('Enter a start position from where bits should be turned ON:')
    count=input('Enter the number of bits to be turned ON:')
    res=TurnOnBits(num,start_pos,count)
    print res
    print bin(res)


if __name__ == '__main__':
    main()


'''
>>> 
 RESTART: C:/Users/Admin/Desktop/Python_2019/Funtions/hw_2_3_feb/bitwise/turn_on_many_bits.py 
Enter a number:1024
0b10000000000
Enter a start position from where bits should be turned ON:6
Enter the number of bits to be turned ON:4
1084
0b10000111100
>>> 
'''
