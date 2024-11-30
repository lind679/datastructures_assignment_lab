class CircularQueue:
    # Class to represent a circular queue.
    def __init__(self, capacity):
        self.capacity = capacity  # Maximum capacity of the queue
        self.queue = [None] * capacity  # Fixed-size array to store queue elements
        self.front = -1  # Points to the front element in the queue
        self.rear = -1   # Points to the rear element in the queue

    def is_empty(self):
        # Check if the queue is empty.
        return self.front == -1

    def is_full(self):
        # Check if the queue is full.
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, data):
        # Add an element to the rear of the queue.
        if self.is_full():
            print("Queue overflow! Cannot enqueue to a full queue.")
            return
        if self.is_empty():
            self.front = self.rear = 0  # First element
        else:
            self.rear = (self.rear + 1) % self.capacity  # Circular increment
        self.queue[self.rear] = data
        print(f"Enqueued {data} to the queue.")

    def dequeue(self):
        # Remove an element from the front of the queue.
        if self.is_empty():
            print("Queue underflow! Cannot dequeue from an empty queue.")
            return None
        dequeued_data = self.queue[self.front]
        if self.front == self.rear:  # Only one element was in the queue
            self.front = self.rear = -1  # Reset queue
        else:
            self.front = (self.front + 1) % self.capacity  # Circular increment
        print(f"Dequeued {dequeued_data} from the queue.")
        return dequeued_data

    def peek(self):
        # Get the front element without removing it.
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self.queue[self.front]

    def display(self):
        # Display all the elements in the queue.
        if self.is_empty():
            print("Queue is empty.")
            return
        print("Queue elements (front to rear):", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.capacity  # Circular increment
        print()

# Example usage
if __name__ == "__main__":
    queue = CircularQueue(capacity=5)
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.display()
    print(f"Front element is: {queue.peek()}")
    queue.dequeue()
    queue.dequeue()
    queue.display()
    queue.enqueue(50)
    queue.enqueue(60)
    queue.enqueue(70)  # Queue becomes full
    queue.display()
    queue.dequeue()
    queue.enqueue(80)  # Demonstrates circular nature
    queue.display()
