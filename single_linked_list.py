class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        print(f"Inserted {data} at the end of the list.")

    def insert_at_beginning(self, data):
        new_node = Node(data) 
        new_node.next = self.head
        self.head = new_node
        print(f"Inserted {data} at the beginning of the list.")

    def delete_node(self, key):
        temp = self.head
        prev = None

        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            print(f"Deleted node with value {key}.")
            return

        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print(f"Node with value {key} not found.")
            return

        prev.next = temp.next
        temp = None
        print(f"Deleted node with value {key}.")

    def display(self):
        """Display the elements in the list."""
        if not self.head:
            print("The list is empty.")
            return

        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Example usage
if __name__ == "__main__":
    linked_list = SinglyLinkedList()
    linked_list.insert_at_end(10)
    linked_list.insert_at_end(20)
    linked_list.insert_at_beginning(5)
    linked_list.display()
    linked_list.delete_node(20)
    linked_list.display()
    linked_list.delete_node(30)  # Node not in the list
    linked_list.display()
