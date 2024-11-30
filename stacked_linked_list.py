class Node:
    # Class to represent a single node in the linked list.
    def __init__(self, data):
        self.data = data
        self.next = None

class StackUsingLinkedList:
    # Class to represent a stack implemented using a linked list.
    def __init__(self):
        self.top = None  # Points to the top of the stack

    def is_empty(self):
        # Check if the stack is empty.
        return self.top is None

    def push(self, data):
        # Push a new element onto the stack.
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(f"Pushed {data} onto the stack.")

    def pop(self):
        # Pop the top element from the stack.
        if self.is_empty():
            print("Stack underflow! Cannot pop from an empty stack.")
            return None
        popped_data = self.top.data
        self.top = self.top.next
        print(f"Popped {popped_data} from the stack.")
        return popped_data

    def peek(self):
        # Return the top element without removing it.
        if self.is_empty():
            print("Stack is empty.")
            return None
        return self.top.data

    def display(self):
        # Display all the elements in the stack.
        if self.is_empty():
            print("Stack is empty.")
            return
        print("Stack elements:")
        temp = self.top
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Example usage
if __name__ == "__main__":
    stack = StackUsingLinkedList()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()
    print(f"Top element is: {stack.peek()}")
    stack.pop()
    stack.display()
    stack.pop()
    stack.pop()
    stack.pop()  # Attempt to pop from an empty stack
