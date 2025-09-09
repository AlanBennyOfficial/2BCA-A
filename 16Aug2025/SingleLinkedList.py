# Linked list = Node = Data and Address / Pointer to another node / Reference

# Linked List Operations
# Menu 
# 1. Insert
# 2. Delete
# 3. Update
# 4. Display
# 5. Exit
# ENter your Choice: 1
# Enter your Data: 100

# Menu 
# 1. Insert
# 2. Delete
# 3. Update
# 4. Display
# 5. Exit
# ENter your Choice: 4
#100 -> None

# Menu 
# 1. Insert
# 2. Delete
# 3. Update
# 4. Display
# 5. Exit
# ENter your Choice:1
# Enter your Data: 200

# Menu 
# 1. Insert
# 2. Delete
# 3. Update
# 4. Display
# 5. Exit
# ENter your Choice:4
# 100 -> 200 -> None

# Menu 
# 1. Insert
# 2. Delete
# 3. Update
# 4. Display
# 5. Exit
# ENter your Choice:3
# Enter the data to be updated: 400
# 400 is not in the list

# Menu 
# 1. Insert
# 2. Delete
# 3. Update
# 4. Display
# 5. Exit
# ENter your Choice:3
# Enter the data to be updated:200
# Enter a New value for 200: 500

# Menu 
# 1. Insert
# 2. Delete
# 3. Update
# 4. Display
# 5. Exit
# ENter your Choice:4
# 100 -> 500 -> None

# Menu 
# 1. Insert
# 2. Delete
# 3. Update
# 4. Display
# 5. Exit
# ENter your Choice:2
# Enter the data to be deleted: 500

# Menu 
# 1. Insert
# 2. Delete
# 3. Update
# 4. Display
# 5. Exit
# ENter your Choice:4
# 100 -> None


100 -> 200 -> 300 -> 400 -> None
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
        
    def insert(self, data):
        if self.head == None:
            print('No Values in the linked List')
            
            new_node = Node(data)  # object creation by node = Node()
            self.head = new_node
            print('{data} is inserted') # First NOde is created
            current = self.head
            
            while current.next:
                current = current.next
            current.next = new_node
                
    def delete(self, data):
        if self.head is None:
            print(f"ENtered {data} is not in the Linkedlist")
        if self.head.data == data:
            
        
    def update():
        print()
        
    def display():
        print()
        
        
def main():
    print("Menu")
    while choice:
        print("1. Insert")
        print("2. Delete")
        print("3. Update")
        print("4. Display")
        print("5. Exit")
        choice = int(input("Enter Your Choice:"))
        
        
if __name__ == "__main__":
    main()