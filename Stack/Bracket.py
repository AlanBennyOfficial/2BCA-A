class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None  # Safe fallback if trying to pop from empty stack

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


def check_brackets(statement):
    stack = Stack()
    for ch in statement:
        if ch in ('{', '[', '('):
            stack.push(ch)
        elif ch in ('}', ']', ')'):
            last = stack.pop()
            if last is None:
                return False
            if last == '{' and ch == '}':
                continue
            elif last == '[' and ch == ']':
                continue
            elif last == '(' and ch == ')':
                continue
            else:
                return False
    return stack.is_empty()


# Example usage:
expression = input("Enter a statement with brackets: ")
if check_brackets(expression):
    print("The brackets are balanced!")
else:
    print("The brackets are NOT balanced.")
