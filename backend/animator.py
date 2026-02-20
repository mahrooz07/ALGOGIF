import os
import uuid
import traceback

GENERATED_DIR = "generated_animations"
os.makedirs(GENERATED_DIR, exist_ok=True)

def execute_and_render(code_str: str):
    """
    Executes the string of python code. 
    The code is expected to save a file named 'animation.gif' in the current working dir.
    We will move that file to our static folder with a unique name.
    """
    unique_filename = f"{uuid.uuid4()}.gif"
    output_path = os.path.join(GENERATED_DIR, unique_filename)
    
    # We run the code in a specific context to capture the output file
    try:
        # 1. Execute the AI generated code
        # We modify the code slightly to save to our specific path if possible, 
        # or we rely on the prompt ensuring it saves to 'animation.gif'
        
        # A trick to force the save path in the executed code:
        code_str = code_str.replace("animation.gif", output_path)
        
        exec_globals = {}
        exec(code_str, exec_globals)
        
        # 2. Verify file was created
        if os.path.exists(output_path):
            return output_path
        else:
            print("File not found at expected path.")
            return None
            
    except Exception as e:
        print(f"Error executing animation code: {e}")
        traceback.print_exc()
        return None