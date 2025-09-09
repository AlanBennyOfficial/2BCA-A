class Stack:
    def __init__(self, capacity):
        self.capacity = capacity            # maximum size of stack
        self.stack = [None] * capacity      # fixed size array
        self.top = -1                       # initialize top at -1 (empty stack)

    # Push operation
    def push(self, x):
        if self.top == self.capacity - 1:   # stack overflow
            print("Stack Overflow! Cannot push", x)
        else:
            self.top += 1
            self.stack[self.top] = x
            print(x, "pushed into stack")

    # Pop operation
    def pop(self):
        if self.top == -1:                  # stack underflow
            print("Stack Underflow! Nothing to pop")
            return None
        else:
            popped = self.stack[self.top]
            self.stack[self.top] = None     # optional: clear the value
            self.top -= 1
            print("Popped:", popped)
            return popped

    # Peek operation
    def peek(self):
        if self.top == -1:
            print("Stack is empty! Nothing to peek")
            return None
        else:
            return self.stack[self.top]

    # Display stack elements
    def display(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            print("Stack elements (top to bottom):", end=" ")
            for i in range(self.top, -1, -1):
                print(self.stack[i], end=" ")
            print()


# Menu-driven program
if __name__ == "__main__":
    capacity = int(input("Enter capacity of stack: "))
    s = Stack(capacity)

    while True:
        print("\n--- Stack Menu ---")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")

        choice = int(input("Enter your choice (1-5): "))

        if choice == 1:
            x = int(input("Enter element to push: "))
            s.push(x)
        elif choice == 2:
            s.pop()
        elif choice == 3:
            val = s.peek()
            if val is not None:
                print("Top element is:", val)
        elif choice == 4:
            s.display()
        elif choice == 5:
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please enter between 1-5.")
