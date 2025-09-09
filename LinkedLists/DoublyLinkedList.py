from colorama import Fore, Style

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None  # Previous node reference
        self.next = None  # Next node reference

# Doubly Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the end
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print(Fore.GREEN + f"Inserted {data} as head node" + Style.RESET_ALL)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
        print(Fore.GREEN + f"Inserted {data} after {temp.data}" + Style.RESET_ALL)

    # Delete a node
    def delete(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                if temp.prev:
                    temp.prev.next = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                if temp == self.head:  # if deleting head
                    self.head = temp.next
                print(Fore.RED + f"Deleted {key}" + Style.RESET_ALL)
                return
            temp = temp.next
        print(Fore.YELLOW + f"{key} not found in the list" + Style.RESET_ALL)

    # Update a node’s value
    def update(self, old, new):
        temp = self.head
        while temp:
            if temp.data == old:
                temp.data = new
                print(Fore.CYAN + f"Updated {old} → {new}" + Style.RESET_ALL)
                return
            temp = temp.next
        print(Fore.YELLOW + f"{old} not found in the list" + Style.RESET_ALL)

    # Display forward
    def display_forward(self):
        temp = self.head
        if not temp:
            print(Fore.YELLOW + "List is empty" + Style.RESET_ALL)
            return
        print(Fore.MAGENTA + "Forward traversal:", end=" " + Style.RESET_ALL)
        while temp:
            print(temp.data, end=" <-> ")
            last = temp
            temp = temp.next
        print("None")

    # Display backward
    def display_backward(self):
        temp = self.head
        if not temp:
            print(Fore.YELLOW + "List is empty" + Style.RESET_ALL)
            return
        while temp.next:
            temp = temp.next
        print(Fore.MAGENTA + "Backward traversal:", end=" " + Style.RESET_ALL)
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")


# ----------- Menu-driven program -------------
dll = DoublyLinkedList()

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
