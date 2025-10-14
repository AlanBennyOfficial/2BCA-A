# Infix to Postfix Conversion and Evaluation

class InfixPostfix:
    def __init__(self):
        # Operator precedence
        self.precedence = {'^': 3, '*': 2, '/': 2, '%': 2, '+': 1, '-': 1}
        self.right_associative = {'^'}
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
    # Function to check if a character is an operand
    def is_operand(self, ch):
        return ch.isalnum()  # allows letters & digits

    # Function to get precedence
    def get_precedence(self, op):
        return self.precedence.get(op, 0)

    # Convert infix to postfix
    def infix_to_postfix(self, expression):
        stack = []  # operator stack
        output = []  # postfix output list

        for ch in expression.replace(" ", ""):
            if self.is_operand(ch):
                output.append(ch)
            elif ch == '(':
                stack.append(ch)
            elif ch == ')':
                # Pop until '('
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                if stack and stack[-1] == '(':
                    stack.pop()
            else:
                # Operator
                while (stack and stack[-1] != '(' and
                       (self.get_precedence(stack[-1]) > self.get_precedence(ch) or
                        (self.get_precedence(stack[-1]) == self.get_precedence(ch)
                         and ch not in self.right_associative))):
                    output.append(stack.pop())
                stack.append(ch)

        # Pop remaining operators
        while stack:
            output.append(stack.pop())

        return ''.join(output)

    # Evaluate postfix expression (numbers only)
    def evaluate_postfix(self, expression):
        stack = []
        for ch in expression:
            if ch.isdigit():
                stack.append(int(ch))
            else:
                b = stack.pop()
                a = stack.pop()
                if ch == '+':
                    stack.append(a + b)
                elif ch == '-':
                    stack.append(a - b)
                elif ch == '*':
                    stack.append(a * b)
                elif ch == '/':
                    stack.append(a / b)
                elif ch == '^':
                    stack.append(a ** b)
        return stack.pop() if stack else None


# Menu-driven interface
if __name__ == "__main__":
    converter = InfixPostfix()

    while True:
        print("\n--- Infix to Postfix Conversion Menu ---")
        print("1. Convert Infix to Postfix")
        print("2. Evaluate Postfix Expression")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            infix = input("Enter infix expression: ")
            postfix = converter.infix_to_postfix(infix)
            print(f"Postfix Expression: {postfix}")

        elif choice == '2':
            postfix = input("Enter postfix expression (digits only): ")
            result = converter.evaluate_postfix(postfix)
            print(f"Evaluated Result: {result}")

        elif choice == '3':
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please enter between 1–3.")
