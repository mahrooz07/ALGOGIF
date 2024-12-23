from data_structures.linked_list import LinkedList
from data_structures.stack import Stack
from data_structures.queue import Queue
from data_structures.binary_tree import BinaryTree

from gif_module.gif_generator import visualize_linked_list
from gif_module.gif_generator import visualize_stack
from gif_module.gif_generator import visualize_queue
from gif_module.gif_generator import visualize_binary_tree

from flask import Flask,request,send_file
from nlp_module.nlp_engine import parse_query


# Instances
app = Flask(__name__)
linked_list = LinkedList()
stack = Stack()
queue = Queue()
binary_tree = BinaryTree()

@app.route('/')

def home():
    return "Hello, ALGOGIF"

@app.route('/query',methods = ['POST'])

def handle_query():
    #json request just to test out model...sumaa work aagudha nu pakuradhuku (to ensure connection)
    user_query = request.json['query'] #Assuming that the user sends a requestion as json
    operation, structure = parse_query(user_query)
    value = request.json.get('value',None)

    # Linked List
    if structure == "linked list":
        if operation == "insert":
            if value:
                linked_list.insert_at_end(value)
                gif_path = visualize_linked_list(linked_list)
                return send_file(gif_path, mimetype = "image/gif")
            else:
                return "No value provided for insertion.",400
            
        elif operation == "delete":
            if value:
                deleted = linked_list.delete_by_value(value)
                if deleted:
                    gif_path = visualize_linked_list(linked_list)
                    return send_file(gif_path, mimetype="image/gif")
                else:
                    return f"Value {value} not found in the linked list.", 404
            else:
                return "No value provided for deletion.", 400
        
    # Stack
    elif structure == "stack":
        if operation == "push":
            if value:
                stack.push(value)
                gif_path = visualize_stack(stack)
                return send_file(gif_path, mimetype="image/gif")
            
            else:
                return "No value provided for push operation.", 400

        elif operation == "pop":
            print(f"Stack before pop: {stack.stack}")  # Log stack state
            popped_value = stack.pop()
            print(f"Popped value: {popped_value}")
            print(f"Stack after pop: {stack.stack}")  # Log stack state after pop
            if popped_value:
                gif_path = visualize_stack(stack)
                return send_file(gif_path, mimetype="image/gif")
            else:
                return "The stack is empty. Nothing to pop.", 400

        elif operation == "peek":
            top_value = stack.peek()
            return f"Top element of the stack is {top_value}" if top_value else "The stack is empty."

        elif operation == "size":
            size = stack.stack_size()
            return f"Stack size is {size}."

        elif operation == "display":
            stack_elements = stack.display()
            return f"Stack elements: {stack_elements}"  
    # Queue
    elif structure == "queue":
        if operation == "enqueue":
            if value:
                queue.enqueue(value)
                gif_path = visualize_queue(queue)
                return send_file(gif_path, mimetype="image/gif")
            else:
                return "No value provided for enqueue operation.", 400

        elif operation == "dequeue":
            dequeued_value = queue.dequeue()
            if dequeued_value is not None:
                gif_path = visualize_queue(queue)
                return send_file(gif_path, mimetype="image/gif")
            else:
                return "Queue is empty.", 400

        elif operation == "peek":
            front_value = queue.peek()
            return f"Front element of the queue is {front_value}" if front_value else "The queue is empty."

        elif operation == "size":
            size = queue.size()
            return f"Queue size is {size}."

        elif operation == "display":
            queue_elements = queue.display()
            return f"Queue elements: {queue_elements}"                 

    # Binary Tree
    elif structure == "binary tree":
        if operation == "insert":
            if value:
                binary_tree.insert(int(value))
                gif_path = visualize_binary_tree(binary_tree)
                return send_file(gif_path, mimetype="image/gif")
            else:
                return "No value provided for insertion.", 400

        elif operation == "delete":
            if value:
                success = binary_tree.delete(int(value))
                if success:
                    gif_path = visualize_binary_tree(binary_tree)
                    return send_file(gif_path, mimetype="image/gif")
                else:
                    return f"Value {value} not found in the binary tree.", 404
            else:
                return "No value provided for deletion.", 400

        elif operation == "display":
            elements = binary_tree.inorder_traversal()
            return f"In-order traversal: {elements}"

        else:
            return "Unsupported operation for this data structure.", 400    


    else:
        return "Could not understand the operation or unsupported operation for the given data structure.", 400
    



if __name__ == "__main__":
    app.run(debug = True)
