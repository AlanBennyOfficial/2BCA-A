class StackQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def enqueue(self, item):
        self.stack1.append(item)
        print(f'{item} enqueued to the queue')

    def dequeue(self):
        if not self.stack1 and not self.stack2:
           print('Queue is empty! cannot dequeue!')
           
        if not self.stack2:
             while self.stack1:
                 self.stack2.append(self.stack1.pop())
            
        removed = self.stack2.pop()
        print(f'{removed} is dequeued from the queue')
        return removed
        
    def peek(self):
        if not self.stack1 and not self.stack2:
           print('Queue is empty! cannot dequeue!')
           return 
       
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            
        print(f'Front element is {self.stack2[-1]}')
        return self.stack2[-1]    
            
    def is_empty(self):
        return not self.stack1 and not self.stack2
    
    def display(self):
        if self.is_empty():
            print('Queue is Empty')
            return
         
        temp = self.stack2[::-1] + self.stack1
        print(f'Queue Contents : {temp}')
        
if __name__ == "__main__":
    q = StackQueue()
    
    while (True):
        print('---Stack based queue Operation---')
        
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
     