class QueueUsingArray:
    # Class to represent a queue implemented using an array.
    def __init__(self, capacity):
        self.capacity = capacity  # Maximum capacity of the queue
        self.queue = []           # Underlying list to store queue elements

    def is_empty(self):
        # Check if the queue is empty.
        return len(self.queue) == 0

    def is_full(self):
        # Check if the queue is full.
        return len(self.queue) == self.capacity

    def enqueue(self, data):
        # Add an element to the rear of the queue.
        if self.is_full():
            print("Queue overflow! Cannot enqueue to a full queue.")
            return
        self.queue.append(data)
        print(f"Enqueued {data} to the queue.")

    def dequeue(self):
        # Remove an element from the front of the queue.
        if self.is_empty():
            print("Queue underflow! Cannot dequeue from an empty queue.")
            return None
        dequeued_data = self.queue.pop(0)
        print(f"Dequeued {dequeued_data} from the queue.")
        return dequeued_data

    def peek(self):
        # Get the front element without removing it.
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self.queue[0]

    def display(self):
        # Display all the elements in the queue.
        if self.is_empty():
            print("Queue is empty.")
            return
        print("Queue elements (front to rear):", " -> ".join(map(str, self.queue)))

# Example usage
if __name__ == "__main__":
    queue = QueueUsingArray(capacity=5)
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
