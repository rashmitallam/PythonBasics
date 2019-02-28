#WAP to implement bubble sort

def BubbleSort(l):
    i=0
    for i in range(len(l)):
        already_sorted=True
        for j in range(len(l)-i-1):
            if l[j]>l[j+1]:
                t=l[j]
                l[j]=l[j+1]
                l[j+1]=t
                

def main():
    l=input("Enter the list to be sorted:")
    BubbleSort(l)
    print l

if __name__ == '__main__':
    main()


'''
>>> 
== RESTART: C:\Users\Admin\Desktop\Python_2019\Lists\hw_16_2\bubble_sort.py ==
Enter the list to be sorted:[3,5,8,2,1,7]
[1, 2, 3, 5, 7, 8]
>>> 
'''
