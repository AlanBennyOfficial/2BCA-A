from colorama import Fore, Style

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None  # Previous node reference
        self.next = None  # Next node reference

# Circular Doubly Linked List class
class CircularDoublyLinkedList:   # CHANGED for CDLL (line 11)
    def __init__(self):
        self.head = None

    # Insert at the end
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node   # CHANGED for CDLL (line 20)
            new_node.prev = new_node   # CHANGED for CDLL (line 21)
            print(Fore.GREEN + f"Inserted {data} as head node" + Style.RESET_ALL)
            return

        last = self.head.prev   # CHANGED for CDLL (line 25)
        last.next = new_node
        new_node.prev = last
        new_node.next = self.head   # CHANGED for CDLL (line 28)
        self.head.prev = new_node   # CHANGED for CDLL (line 29)
        print(Fore.GREEN + f"Inserted {data} after {last.data}" + Style.RESET_ALL)

    # Delete a node
    def delete(self, key):
        if self.head is None:
            print(Fore.YELLOW + "List is empty" + Style.RESET_ALL)
            return

        current = self.head
        while True:   # CHANGED for CDLL (line 38)
            if current.data == key:
                if current.next == current:   # only one node left (line 40)
                    self.head = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    if current == self.head:
                        self.head = current.next
                print(Fore.RED + f"Deleted {key}" + Style.RESET_ALL)
                return
            current = current.next
            if current == self.head:   # CHANGED for CDLL (line 49)
                break
        print(Fore.YELLOW + f"{key} not found in the list" + Style.RESET_ALL)

    # Update a node’s value
    def update(self, old, new):
        if self.head is None:
            print(Fore.YELLOW + "List is empty" + Style.RESET_ALL)
            return
        current = self.head
        while True:   # CHANGED for CDLL (line 59)
            if current.data == old:
                current.data = new
                print(Fore.CYAN + f"Updated {old} → {new}" + Style.RESET_ALL)
                return
            current = current.next
            if current == self.head:   # CHANGED for CDLL (line 65)
                break
        print(Fore.YELLOW + f"{old} not found in the list" + Style.RESET_ALL)

    # Display forward
    def display_forward(self):
        if self.head is None:
            print(Fore.YELLOW + "List is empty" + Style.RESET_ALL)
            return
        print(Fore.MAGENTA + "Forward traversal:", end=" " + Style.RESET_ALL)
        current = self.head
        while True:   # CHANGED for CDLL (line 76)
            print(current.data, end=" <-> ")
            current = current.next
            if current == self.head:   # CHANGED for CDLL (line 79)
                break
        print("(back to head)")

    # Display backward
    def display_backward(self):
        if self.head is None:
            print(Fore.YELLOW + "List is empty" + Style.RESET_ALL)
            return
        print(Fore.MAGENTA + "Backward traversal:", end=" " + Style.RESET_ALL)
        current = self.head.prev   # CHANGED for CDLL (line 89)
        while True:   # CHANGED for CDLL (line 90)
            print(current.data, end=" <-> ")
            current = current.prev
            if current == self.head.prev:   # CHANGED for CDLL (line 93)
                break
        print("(back to head)")


# ----------- Menu-driven program -------------
dll = CircularDoublyLinkedList()   # CHANGED for CDLL (line 101)

while True:
    print("\n" + Fore.BLUE + "Menu:" + Style.RESET_ALL)
    print("1. Insert")
    print("2. Delete")
    print("3. Update")
    print("4. Display Forward")
    print("5. Display Backward")
    print("6. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:

        val = int(input("Enter value to insert: "))
        dll.insert(val)
    elif choice == 2:
        val = int(input("Enter value to delete: "))
        dll.delete(val)
    elif choice == 3:
        old = int(input("Enter value to update: "))
        new = int(input("Enter new value: "))
        dll.update(old, new)
    elif choice == 4:
        dll.display_forward()
    elif choice == 5:
        dll.display_backward()
    elif choice == 6:
        print(Fore.GREEN + "Exiting..." + Style.RESET_ALL)
        break
    else:
        print(Fore.YELLOW + "Invalid choice" + Style.RESET_ALL)
