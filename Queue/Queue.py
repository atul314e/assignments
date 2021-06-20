class Queue():
    """
    Queue datastructure adds element at end and removes from front, Last In First Out(LIFO)\n
    Queue has following operations:\n
    1 > enqueue(number) - inserts in Queue\n
    2 > dequeue() - delete element from queue\n
    3 > reverse() - reverses the Queue\n
    4 > show() - shows the Queue\n
    5 > clear() - empty the Queue\n
    6 > min() - returns the minimum element from Queue\n
    """
    def __init__(self):
        self._QUEUE = []

    def show(self):
        '''
        INFO: returns the queue, [] if Queue is empty.
        '''
        return self._QUEUE

    def min(self):
        '''
        INFO: returns minimum, None if Queue is empty
        '''
        length = len(self._QUEUE)
        if length==0:
            return None
        else:
            return min(self._QUEUE)

    def clear(self):
        '''
        INFO: empty the complete Queue
        '''
        self._QUEUE.clear()
        return 

    def enqueue(self, num: int):
        '''
        INFO: inserts element in Queue from end.
        '''
        self._QUEUE.append(num)
    
    def dequeue(self):
        '''
        INFO: removes element from Queue from start.
        '''        
        if len(self._QUEUE)==0:
            print("Queue is empty!!")
        else:
            self._QUEUE.pop(0)
    
    def reverse(self, start):
        '''
        INFO: reverse method revere the QUEUE using a recursive method.\n
        example:-\n
        [1, 2, 3]\n
        [1, 3, 2] - 2 is popped and pushed into queue\n
        [3, 2, 1] - 1 is popped and pushed into queue\n
        '''
        length = len(self._QUEUE)
        
        if length==0:
            return
        
        def reverse_queue(i):
            if i==length:
                return
            else:
                reverse_queue(i+1)
                element=self._QUEUE.pop(i-1) # picks element from end of queue to start of queue
                self._QUEUE.append(element)
                return
        reverse_queue(start)

def queue_operation(queue):

    valid=["1", "2", "3", "4", "5","6", "-1"]
    inp=0

    while inp != -1:
        inp = input("Enter choice '1' for add, '2' for remove, '3' for reverse, '4' for show, '5' for clear,'6' for min, '-1' for quit >> ")
        while inp not in valid:
            inp = input("Enter valid input, 1' for add, '2' for remove, '3' for reverse, '4' for show, '5' for clear,'6' for min, '-1' for quit >> ")

        inp=int(inp)
        if inp==1:
            while(1):
                try:
                    num = int(input("Enter number to add in queue >> "))
                    break
                except:
                    print("Only numeric input allowed!!")
            queue.enqueue(num)
        elif inp==2:
            queue.dequeue()
        elif inp==3:
            queue.reverse(1)
        elif inp==4:
            lst = queue.show()
            print(lst)
        elif inp==5:
            queue.clear()
        elif inp==6:
            Min=queue.min()
            print("Minimum element in queue is ", Min)
        elif inp==-1:
            break