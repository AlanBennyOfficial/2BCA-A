from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

class Node:
    def __init__(self, data):
        self.data = data  # stores data
        self.next = None  # pointer to next node

class CircularLinkedList:   # CHANGED for CLL
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head   # CHANGED for CLL
            print(Fore.GREEN + f"{data} inserted successfully.")
            return

        current = self.head
        while current.next != self.head:   # CHANGED for CLL
            current = current.next
        current.next = new_node
        new_node.next = self.head   # CHANGED for CLL
        print(Fore.GREEN + f"{data} inserted successfully.")

    def delete(self, data):
        if self.head is None:
            print(Fore.RED + "List is empty. Nothing to delete.")
            return

        # If head node itself is to be deleted
        if self.head.data == data:
            if self.head.next == self.head:   # only one node in CLL
                self.head = None
            else:
                temp = self.head
                current = self.head
                while current.next != self.head:   # CHANGED for CLL
                    current = current.next
                current.next = self.head.next
                self.head = self.head.next
            print(Fore.RED + f"{data} deleted successfully.")
            return

        current = self.head
        while current.next != self.head and current.next.data != data:   # CHANGED for CLL
            current = current.next

        if current.next == self.head:   # CHANGED for CLL
            print(Fore.RED + f"{data} not found in the list.")
        else:
            current.next = current.next.next
            print(Fore.RED + f"{data} deleted successfully.")

    def update(self, old_value, new_value):
        if self.head is None:
            print(Fore.RED + "List is empty.")
            return

        current = self.head
        while True:   # CHANGED for CLL
            if current.data == old_value:
                current.data = new_value
                print(Fore.CYAN + f"Updated {old_value} to {new_value}.")
                return
            current = current.next
            if current == self.head:   # CHANGED for CLL
                break
        print(Fore.RED + f"{old_value} not in the list.")

    def display(self):
        if self.head is None:
            print(Fore.RED + "List is empty.")
            return
        current = self.head
        print(Fore.MAGENTA + "Circular Linked List: ", end="")
        while True:   # CHANGED for CLL
            print(Fore.WHITE + str(current.data), end=" -> ")
            current = current.next
            if current == self.head:   # CHANGED for CLL
                break
        print(Fore.MAGENTA + "(back to head)")

# Menu-driven program
if __name__ == "__main__":
    ll = CircularLinkedList()   # CHANGED for CLL

    while True:
        print(Fore.BLUE + "\nMenu:")
        print("1. Insert")
        print("2. Delete")
        print("3. Update")
        print("4. Display")
        print("5. Exit")
        choice = input(Fore.YELLOW + "Enter your choice: ")

        if choice == "1":
            data = int(input("Enter value to insert: "))
            ll.insert(data)

        elif choice == "2":
            data = int(input("Enter value to delete: "))
            ll.delete(data)

        elif choice == "3":
            old_value = int(input("Enter value to update: "))
            new_value = int(input("Enter new value: "))
            ll.update(old_value, new_value)

        elif choice == "4":
            ll.display()

        elif choice == "5":
            print(Fore.GREEN + "Exiting program. Goodbye!")
            break

        else:
            print(Fore.RED + "Invalid choice. Please try again.")
