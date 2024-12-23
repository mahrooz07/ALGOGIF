class Stack:
    """stack class with basic operation which can be later imported in our main app"""
    def __init__(self):
        self.stack = [] #list to store elements of stack

    #Function to push an element in the stack
    def push(self, data):
        self.stack.append(data)
        print(f"Pushed {data} onto the stack.")

    #function to pop an element from the stack
    def pop(self):
        if self.stack:
            popped = self.stack.pop()
            print(f"Popped {popped} from stack.")
            return popped
        print("Pop attempted on empty stack.")
        return None

    def peek(self):
        """Returns the top most element of the stack without removing it from the stack"""
        if self.isEmpty():
            print("Stack is Empty !")
            return None
        print("Top of the stack is {self.stack[-1]}.")
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def stack_size(self):
        return len(self.stack)
    
    def display(self):
        """Display all the elements of the stack"""
        if self.isEmpty():
            print("Stack is empty.")
            return
        print("Stack elements (from top to Bottom)")
        for elements in reversed(self.stack):
            print(elements, end = " ")
        print()    