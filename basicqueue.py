# Implement Queue using python List
# Invokation: python3 basicqueue.py

from typing import List
from os import system


class Queue:
    def __init__(self, arr: List[int]) -> None:
        self.queue = arr

    def enqueue(self, x: int) -> None:
        self.queue.append(x)

    def dequeue(self) -> int:
        if(len(self.queue) > 0):
            deleted_val = self.queue.pop(0)
            return deleted_val
        else:
            print("Queue is empty!!")

    def print_queue(self) -> None:
        if(len(self.queue) > 0):
            queue_list = list(map(str, self.queue))
            print("Front [", " <- ".join(queue_list), "] Rear")
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
        print("3. Print Queue")
        print("4. Exit")
        x = int(input("Enter your choice: "))
        if(x == 1):
            system('clear')
            v = int(input("Enter value to insert: "))
            obj.enqueue(v)
            print(f'{v} inserted in queue.')
            input('\nPress any key to continue...')
        elif(x == 2):
            system('clear')
            v = obj.dequeue()
            print(f'{v} deleted from queue.')
            input('\nPress any key to continue...')
        elif(x == 3):
            system('clear')
            obj.print_queue()
            input('\nPress any key to continue...')
        elif(x == 4):
            print("\nExiting...")
            break
        else:
            print("\nInvalid Input. Exiting...")
            break
except:
    print("\nInvalid Input. Exiting...")
