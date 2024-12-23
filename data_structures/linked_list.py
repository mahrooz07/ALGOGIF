class Node:
    def __init__(self, data):
        """class Representing a Node in the Linked List"""
        self.data = data
        self.next = None    
    
class LinkedList:
    """Linked List class to define basic linked list operations"""
    def __init__(self):
        self.head = None

    def __iter__(self):
        current = self.head 
        while current:
            yield current
            current = current.next        

    def insert_at_end(self, data):
        """Function to insert a Node with the given data at the end of the Linked List"""
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            print(f"Inserted {data} as the head node.")

        else:
            temp = self.head
            while temp.next:
                temp = temp.next

            temp.next = new_node   
            print(f"Inserted {data} at the end of the linked list.")

    def delete_by_value(self, value):
        """Deletes the first node with the given value."""
        if not self.head:  # If the list is empty
            print("The linked list is empty.")
            return False

        # If the head node is the one to be deleted
        if self.head.data == value:
            self.head = self.head.next
            return True

        # Traverse the list to find the node to delete
        current = self.head
        while current.next and current.next.data != value:
            current = current.next

        # If the node was found, delete it
        if current.next and current.next.data == value:
            current.next = current.next.next
            return True

        # Value not found
        print(f"Value {value} not found in the list.")
        return False
