class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class NodeQueue:
    def __init__(self):
        self.front = self.rear = None
    
    def enqueue(self, item ):
        new_node = Node(item)
        if self.rear == None:
            self.rear = self.front = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f'{item} enqueued to the queue')
            
    def dequeue(self):
        if self.front == None:
            print('Queue is empty, can\'t dequeue')
            return None
        temp = self.front 
        self.front = temp.next
        if self.front is None:
            self.rear = None
        print(f'{temp.data} dequeued from the queue')           
        return temp.data 
    
    def peek(self):
        if self.front is None:
            print('Queue is empty')
            return None
        print(f'Front element is {self.front.data}')
        return self.front.data
    
    def display(self):
        if self.front is None:
            print('Queue is empty')
            return None
        temp = self.front
        elements = []
        while temp:
            elements.append(temp.data)
            temp = temp.next
        print('Queue Contents: ', elements)
    
    def is_empty(self):
        return self.front is None
    
if __name__ == "__main__":
    q = NodeQueue()
    
    while (True):
        print('---Node based queue Operation---')
        
        print('1. Enqueue')
        print('2. Dequeue')
        print('3. Peek')
        print('4. Display')
        print('5. is Empty')
        print('6. Exit')
   
        choice = input('Enter your choice:')
        
        if choice == '1':
            item = input("Enter element to enqueue: ")
            q.enqueue(item)

        elif choice == '2':
            q.dequeue()

        elif choice == '3':
            q.peek()

        elif choice == '4':
            q.display()

        elif choice == '5':
            if q.is_empty():
                print("Queue is empty.")
            else:
                print("Queue is not empty.")

        elif choice == '6':
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please enter between 1-6.")
     