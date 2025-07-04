from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from backend.script_generator import generate_script

app = FastAPI()

class ScriptRequest(BaseModel):
    title: str | None = None
    bullet_points: list[str] | None = None
    tone: str = "educational"
    length: str = "medium"
    language: str = "English"

@app.post("/generate-script/")
async def create_script(req: ScriptRequest):
    if not req.title and not req.bullet_points:
        raise HTTPException(status_code=400, detail="Provide either title or bullet points.")
    
    script = generate_script(req.title, req.bullet_points or [], req.tone, req.length, req.language)
    return {"script": script}
