class StackUsingArray:
    # Class to represent a stack implemented using an array.
    def __init__(self, capacity):
        self.capacity = capacity  # Maximum capacity of the stack
        self.stack = []           # Underlying list to store stack elements

    def is_empty(self):
        # Check if the stack is empty.
        return len(self.stack) == 0

    def is_full(self):
        # Check if the stack is full.
        return len(self.stack) == self.capacity

    def push(self, data):
        # Push a new element onto the stack.
        if self.is_full():
            print("Stack overflow! Cannot push onto a full stack.")
            return
        self.stack.append(data)
        print(f"Pushed {data} onto the stack.")

    def pop(self):
        # Pop the top element from the stack.
        if self.is_empty():
            print("Stack underflow! Cannot pop from an empty stack.")
            return None
        return self.stack.pop()

    def peek(self):
        # Return the top element without removing it.
        if self.is_empty():
            print("Stack is empty.")
            return None
        return self.stack[-1]

    def display(self):
        # Display all the elements in the stack.
        if self.is_empty():
            print("Stack is empty.")
            return
        print("Stack elements (top to bottom):")
        for i in range(len(self.stack) - 1, -1, -1):
            print(self.stack[i])

# Example usage
if __name__ == "__main__":
    stack = StackUsingArray(capacity=5)
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()
    print(f"Top element is: {stack.peek()}")
    print(f"Popped element is: {stack.pop()}")
    stack.display()
    stack.pop()
    stack.pop()
    stack.pop()  # Attempt to pop from an empty stack
