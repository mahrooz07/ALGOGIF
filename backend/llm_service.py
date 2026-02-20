import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# Ensure you have set this env var: export GROQ_API_KEY='your_key_here'
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def generate_animation_code(topic: str, specific_query: str):
    system_prompt = """
    You are a Python expert for data visualization. 
    Your goal is to write a COMPLETE, standalone Python script using Matplotlib and NetworkX.
    
    Constraints:
    1. The script MUST generate an animation and save it as 'animation.gif'.
    2. Do NOT use plt.show(). Use animation.save('animation.gif', writer='pillow').
    3. Use 'matplotlib.animation.FuncAnimation'.
    4. Provide ONLY the python code. No markdown, no backticks, no explanations.
    5. The code must be robust and handle errors gracefully.
    """

    user_prompt = f"Create a visual explanation for the domain: {topic}. Specific request: {specific_query}."

    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        model="llama-3.3-70b-versatile", # Strong reasoning model
    )

    # Clean up response to ensure it's pure code
    code = chat_completion.choices[0].message.content
    code = code.replace("```python", "").replace("```", "").strip()
    return code