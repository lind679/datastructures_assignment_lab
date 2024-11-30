class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            print(f"Inserted {data} at the end of the list.")
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
        print(f"Inserted {data} at the end of the list.")

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
        print(f"Inserted {data} at the beginning of the list.")

    def delete_node(self, key):
        temp = self.head

        if not temp:
            print("The list is empty.")
            return

        if temp.data == key:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            print(f"Deleted node with value {key}.")
            return

        while temp and temp.data != key:
            temp = temp.next

        if not temp:
            print(f"Node with value {key} not found.")
            return

        if temp.next:
            temp.next.prev = temp.prev
        if temp.prev:
            temp.prev.next = temp.next

        print(f"Deleted node with value {key}.")

    def display_forward(self):
        if not self.head:
            print("The list is empty.")
            return

        temp = self.head
        print("List in forward order:")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def display_backward(self):
        if not self.head:
            print("The list is empty.")
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        print("List in backward order:")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.prev
        print("None")

# Example usage
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_at_end(10)
    dll.insert_at_end(20)
    dll.insert_at_beginning(5)
    dll.display_forward()
    dll.display_backward()
    dll.delete_node(20)
    dll.display_forward()
    dll.delete_node(30)  # Node not in the list
    dll.display_forward()
