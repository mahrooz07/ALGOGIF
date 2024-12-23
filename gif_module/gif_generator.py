from PIL import Image, ImageDraw
import os

def create_gif(frames, output_path, duration=500):
    """Creates a GIF from a list of frames."""
    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=duration,
        loop=0
    )

#Function to visualize LinkedList
def visualize_linked_list(linked_list, message=""):
    """Visualizes the linked list and creates a GIF with a pointer on the right side."""
    frames = []
    current = linked_list.head
    step = 1

    while current:
        # Create an image frame
        frame = Image.new("RGB", (500, 150), "white")
        draw = ImageDraw.Draw(frame)

        # Draw the linked list nodes
        x = 20
        temp = linked_list.head
        while temp:
            # Draw rectangle for the node
            draw.rectangle([x, 60, x + 60, 100], outline="black", width=2)
            # Draw the data in the node
            draw.text((x + 20, 70), str(temp.data), fill="black")
            # Draw a pointer (arrow) for the current node
            if temp == current:
                draw.line([x + 60, 80, x + 90, 80], fill="red", width=3)  # Horizontal line
                draw.polygon(
                    [(x + 90, 75), (x + 100, 80), (x + 90, 85)], 
                    fill="red"
                )  # Arrowhead pointing right
            x += 80
            temp = temp.next

        # Add step label and message
        draw.text((20, 10), f"Step {step}: {message}", fill="blue")
        frames.append(frame)
        step += 1

        current = current.next

    # Save GIF
    output_path = os.path.join("static", "gifs", "linked_list_updated.gif")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    create_gif(frames, output_path)
    return output_path


# Function to visulize Stack

def visualize_stack(stack):
    """Visualizes the stack and creates GIF"""
    frames = []
    step = 1

    for i in range(len(stack.stack) + 1):
        # Image frame Create panrom
        frame = Image.new("RGB", (200, 300), "white")
        draw = ImageDraw.Draw(frame)

        # Draw the stack Elements from bottom to top
        x, y = 80, 250
        for value in stack.stack[:i]:  # Start from the bottom to the top
            draw.rectangle([x, y - 40, x + 80, y], outline="black", width=2)
            draw.text((x + 30, y - 30), str(value), fill="black")
            y -= 50

        draw.text((10, 10), f"Step {step}", fill="blue")
        frames.append(frame)
        step += 1

    # Save GIF
    output_path = os.path.join("static", "gifs", "stack.gif")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    create_gif(frames, output_path)
    return output_path

# Function to visualize Queue

def visualize_queue(queue):
    """Visualizes the queue and creates a GIF."""
    frames = []
    current = queue.front
    step = 1

    while current:
        # Create an image frame
        frame = Image.new("RGB", (500, 150), "white")
        draw = ImageDraw.Draw(frame)

        # Draw the queue elements
        x = 20
        temp = queue.front
        while temp:
            draw.rectangle([x, 50, x + 60, 100], outline="black", width=2)
            draw.text((x + 20, 60), str(temp.data), fill="black")
            x += 80
            temp = temp.next

        draw.text((20, 20), f"Step {step}", fill="blue")
        frames.append(frame)
        step += 1

        current = current.next

    # Save GIF
    output_path = os.path.join("static", "gifs", "queue.gif")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    create_gif(frames, output_path)
    return output_path


# Function to visualize Binary Tree

def visualize_binary_tree(tree):
    """Visualize the binary tree with lines connecting parent and child nodes."""
    frames = []
    nodes = []

    def traverse(node, x, y, level=1):
        """Helper function to traverse and store node positions."""
        if node:
            nodes.append((x, y, node.data, node))
            traverse(node.left, x - 120 // level, y + 70, level + 1)
            traverse(node.right, x + 120 // level, y + 70, level + 1)

    traverse(tree.root, 250, 50)

    for step in range(1, len(nodes) + 1):
        frame = Image.new("RGB", (500, 300), "white")
        draw = ImageDraw.Draw(frame)

        for i in range(step):
            x, y, data, node = nodes[i]

            # Draw lines to children
            if node.left:
                child_x, child_y, _, _ = next(n for n in nodes if n[3] == node.left)
                draw.line([(x, y), (child_x, child_y)], fill="black", width=2)
            if node.right:
                child_x, child_y, _, _ = next(n for n in nodes if n[3] == node.right)
                draw.line([(x, y), (child_x, child_y)], fill="black", width=2)

            # Draw node
            draw.ellipse([x - 20, y - 20, x + 20, y + 20], outline="black", fill="lightblue")
            draw.text((x - 10, y - 10), str(data), fill="black")

        frames.append(frame)

    output_path = os.path.join("static", "gifs", "binary_tree.gif")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=500,
        loop=0
    )

    return output_path


