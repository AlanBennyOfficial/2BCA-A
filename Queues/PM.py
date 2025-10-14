from collections import deque

def is_balanced(expression):
    q = deque()

    # Step 1: Enqueue all parentheses
    for ch in expression:
        if ch in "()" or ch in "{}" or ch in "[]":
            q.append(ch)

    stack = []
    # Step 2: Process queue
    while q:
        ch = q.popleft()
        if ch in "([{":  # opening
            stack.append(ch)
        else:  # closing
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and ch != ')') or \
               (top == '{' and ch != '}') or \
               (top == '[' and ch != ']'):
                return False

    return not stack


# Example
expr1 = "{[()()]}"
expr2 = "{[(])}"

print(expr1, "-> Balanced?", is_balanced(expr1))
print(expr2, "-> Balanced?", is_balanced(expr2))
