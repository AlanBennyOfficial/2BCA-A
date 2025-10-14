# Menu-driven Queue Program in Python

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"{item} enqueued to the queue.")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! Cannot dequeue.")
            return None
        removed = self.queue.pop()
        print(f"{removed} dequeued from the queue.")
        return removed

    def peek(self):
        if self.is_empty():
            print("Queue is empty! No front element.")
            return None
        print(f"Front element is: {self.queue[0]}")
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            print("Queue contents:", self.queue)


# Menu-driven interface
if __name__ == "__main__":
    q = Queue()

    while True:
        print("\n--- Queue Operations Menu ---")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek (Front element)")
        print("4. Display Queue")
        print("5. Check if Empty")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

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
