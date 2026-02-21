from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from llm_service import generate_animation_code
from animator import execute_and_render
import os

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, change this to your React app's domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Mount the generated folder so the frontend can access the GIFs via URL
app.mount("/animations", StaticFiles(directory="generated_animations"), name="animations")

class PromptRequest(BaseModel):
    domain: str
    query: str

@app.post("/generate")
async def generate_visual(request: PromptRequest):
    print(f"Received request: {request.domain} - {request.query}")
    
    # 1. Get Code from Groq
    print("Asking Groq for code...")
    try:
        code = generate_animation_code(request.domain, request.query)
        print("Code generated successfully.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM Error: {str(e)}")

    # 2. Execute Code to create GIF
    print("Rendering animation...")
    gif_path = execute_and_render(code)
    
    if not gif_path:
        raise HTTPException(status_code=500, detail="Failed to generate animation file. The AI code might be buggy.")

    # 3. Return the URL
    # Assuming running locally on port 8000
    filename = os.path.basename(gif_path)
    return {
        "status": "success",
        "url": f"http://localhost:8000/animations/{filename}",
        "code_snippet": code # Optional: send code back if you want to show it to user
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)