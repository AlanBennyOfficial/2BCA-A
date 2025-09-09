from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

class Node:
    def __init__(self, data):
        self.data = data  # stores data
        self.next = None  # pointer to next node

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print(Fore.GREEN + f"{data} inserted successfully.")
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        print(Fore.GREEN + f"{data} inserted successfully.")

    def delete(self, data):
        if self.head is None:
            print(Fore.RED + "List is empty. Nothing to delete.")
            return

        if self.head.data == data:
            self.head = self.head.next
            print(Fore.RED + f"{data} deleted successfully.")
            return

        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        if current.next is None:
            print(Fore.RED + f"{data} not found in the list.")
        else:
            current.next = current.next.next            
            print(Fore.RED + f"{data} deleted successfully.")

    def update(self, old_value, new_value):
        current = self.head
        while current:
            if current.data == old_value:
                current.data = new_value
                print(Fore.CYAN + f"Updated {old_value} to {new_value}.")
                return
            current = current.next
        print(Fore.RED + f"{old_value} not in the list.")

    def display(self):
        if self.head is None:
            print(Fore.RED + "List is empty.")
            return
        current = self.head
        print(Fore.MAGENTA + "Linked List: ", end="")
        while current:
            print(Fore.WHITE + str(current.data), end=" -> ")
            current = current.next
        print(Fore.MAGENTA + "None")

# Menu-driven program
if __name__ == "__main__":
    ll = LinkedList()

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
