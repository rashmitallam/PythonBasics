#WAP to demonstrate queue datastructure

def Enqueue(q,e):
    if isQueueFull(q):
        print('Queue is Full!')
    else:
        return q.append(e)

def Dequeue(q):
    if isQueueEmpty(q):
        print('Queue is Empty!')
    else:
        return q.pop(0)

def isQueueFull(q):
    if len(q) >= 5:
        return True
    else:
        return False

def isQueueEmpty(q):
    if len(q) == 0:
        return True
    else:
        return False

def SimulateQueueOperations():
    q=input("Enter the Queue elements:")
    while(True):
        print("Menu:")
        print("1.Enqueue\n2.Dequeue\nPress any other number to exit!")
        ch=input("Enter your choice:")
        if ch == 1:
            e=input("Enter element to be added to the queue:")
            Enqueue(q,e)
            print q
        elif ch == 2:
            Dequeue(q)
            print q
        else:
            break

def main():
    SimulateQueueOperations()

if __name__ == '__main__':
    main()


'''
>>> 
 RESTART: C:/Users/Admin/Desktop/Python_2019/Lists/hw_16_2/queue_operations_list.py 
Enter the Queue elements:[1,4,2,5]
Menu:
1.Enqueue
2.Dequeue
Press any other number to exit!
Enter your choice:1
Enter element to be added to the queue:8
[1, 4, 2, 5, 8]
Menu:
1.Enqueue
2.Dequeue
Press any other number to exit!
Enter your choice:1
Enter element to be added to the queue:3
Queue is Full!
[1, 4, 2, 5, 8]
Menu:
1.Enqueue
2.Dequeue
Press any other number to exit!
Enter your choice:2
[4, 2, 5, 8]
Menu:
1.Enqueue
2.Dequeue
Press any other number to exit!
Enter your choice:2
[2, 5, 8]
Menu:
1.Enqueue
2.Dequeue
Press any other number to exit!
Enter your choice:2
[5, 8]
Menu:
1.Enqueue
2.Dequeue
Press any other number to exit!
Enter your choice:2
[8]
Menu:
1.Enqueue
2.Dequeue
Press any other number to exit!
Enter your choice:2
[]
Menu:
1.Enqueue
2.Dequeue
Press any other number to exit!
Enter your choice:2
Queue is Empty!
[]
Menu:
1.Enqueue
2.Dequeue
Press any other number to exit!
Enter your choice:6
>>> 
'''
