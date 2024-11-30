class Node:
    # Class to represent a single node in the linked list.
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueUsingLinkedList:
    # Class to represent a queue implemented using a linked list.
    def __init__(self):
        self.front = None  # Points to the front of the queue
        self.rear = None   # Points to the rear of the queue

    def is_empty(self):
        # Check if the queue is empty.
        return self.front is None

    def enqueue(self, data):
        # Add an element to the rear of the queue
        new_node = Node(data)
        if self.rear is None:  # If the queue is empty
            self.front = self.rear = new_node
            print(f"Enqueued {data} to the queue.")
            return
        self.rear.next = new_node
        self.rear = new_node
        print(f"Enqueued {data} to the queue.")

    def dequeue(self):
        # Remove an element from the front of the queue.
        if self.is_empty():
            print("Queue underflow! Cannot dequeue from an empty queue.")
            return None
        dequeued_data = self.front.data
        self.front = self.front.next
        if self.front is None:  # If the queue becomes empty
            self.rear = None
        print(f"Dequeued {dequeued_data} from the queue.")
        return dequeued_data

    def peek(self):
        # Get the front element without removing it.
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self.front.data

    def display(self):
        # Display all the elements in the queue.
        if self.is_empty():
            print("Queue is empty.")
            return
        print("Queue elements (front to rear):")
        temp = self.front
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Example usage
if __name__ == "__main__":
    queue = QueueUsingLinkedList()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.display()
    print(f"Front element is: {queue.peek()}")
    queue.dequeue()
    queue.display()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()  # Attempt to dequeue from an empty queue
