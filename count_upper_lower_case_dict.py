#WAP to accept a sentence which contains upper and lower case characters, return a dict containing count of total no. of upper and lower case chars


def CountUpperLowerDict(s1):
    res=dict()
    u_count=l_count=0

    for ch in s1:
        if ch != ' ':
            if ch.isupper():
                if res.get(ch) != None:
                    res[ch] += 1
                else:
                    res[ch] = 1
                u_count += 1
            else:
                if res.get(ch) != None:
                    res[ch] += 1
                else:
                    res[ch] = 1
                l_count += 1
    return(res,l_count,u_count)
        
    
def main():
    s=input('Enter a sentence having upper and lower case characters:')
    (res,l,u)=CountUpperLowerDict(s)
    print 'Count of Lower case chars: {}\nCount of Upper case chars: {}'.format(l,u)
    for x in res:
        print(x,res[x])

    #print 'Count of Upper case chars: '+str(u)
    

if __name__ == '__main__':
    main()

'''
>>> 
 RESTART: C:\Users\Admin\Desktop\Python_2019\Dictionary\hw_2_3\count_upper_lower_case.py 
Enter a sentence having upper and lower case characters:'Hi. My name is Rashmi Tallam. I like Programming!'
Count of Lower case chars: 35
Count of Upper case chars: 6
('a', 5)
('!', 1)
('r', 2)
('e', 2)
('g', 2)
('P', 1)
('i', 5)
('H', 1)
('k', 1)
('M', 1)
('m', 5)
('o', 1)
('n', 2)
('I', 1)
('s', 2)
('R', 1)
('T', 1)
('h', 1)
('y', 1)
('.', 2)
('l', 3)
>>> 
'''
