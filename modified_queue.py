# Write following additional methods for Queue: method to reverse a Queue using recursion, method which returns minimum(smallest) element in the queue(considering all elements in the queue are of same datatype)
# Invokation: python3 modified_queue.py

from typing import List
from os import system


class Queue:
    def __init__(self, arr: List[int]) -> None:
        self.queue = arr

    def isEmpty(self) -> bool:
        return len(self.queue) == 0

    def enqueue(self, x: int) -> None:
        self.queue.append(x)

    def dequeue(self) -> int:
        if(not self.isEmpty()):
            deleted_val = self.queue.pop(0)
            return deleted_val
        else:
            print("Queue is empty!!")

    def print_queue(self) -> None:
        if(not self.isEmpty()):
            # Join works only on strings
            queue_list = list(map(str, self.queue))
            print("Front [", " <- ".join(queue_list), "] Rear")
        else:
            print("Queue is empty!!")

    def reverseQueue(self) -> None:
        if (self.isEmpty()):
            return
        data = self.dequeue()
        self.reverseQueue()
        self.enqueue(data)

    def get_min(self) -> int:
        if(not self.isEmpty()):
            return min(self.queue)
        else:
            print("Queue is empty!!")


try:
    N = int(input("Enter number of elements: "))
    print("Enter the elements (front to rear) as space separated integers:")
    l = list(map(int, input().split()))
    obj = Queue(l)
    print("Queue Created!")
    input('\nPress any key to continue...')

    while(1):
        system('clear')
        print("Choices:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Reverse Queue")
        print("4. Get Minimum Element")
        print("5. Print Queue")
        print("6. Exit")
        x = int(input("Enter your choice: "))
        if(x == 1):
            system('clear')
            v = int(input("Enter value to insert: "))
            obj.enqueue(v)
            print(f'{v} inserted in queue.')
            input('\nPress any key to continue...')
        elif(x == 2):
            system('clear')
            val = obj.dequeue()
            if(val):
                print(f'{v} deleted from queue.')
            input('\nPress any key to continue...')
        elif(x == 3):
            system('clear')
            obj.reverseQueue()
            print("Queue Reversed!")
            input('\nPress any key to continue...')
        elif(x == 4):
            system('clear')
            val = obj.get_min()
            if(val):
                print(f"The minimum value in queue is {val}.")
            input('\nPress any key to continue...')
        elif(x == 5):
            system('clear')
            obj.print_queue()
            input('\nPress any key to continue...')
        elif(x == 6):
            print("\nExiting...")
            break
        else:
            print("\nInvalid Input. Exiting...")
            break
except:
    print("\nInvalid Input. Exiting...")
