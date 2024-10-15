from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from app.tts_service import synthesize_speech
from app.tests_tts_service import test_synthesize_speech
app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/principal/")
async def synthesize(text_input: TextInput):
    try:
        audio_path = synthesize_speech(text_input.text)
        return FileResponse(audio_path, media_type="audio/mp3")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/prueba/")
async def test_synthesize(text_input: TextInput):
    try:
        audio_path2 = test_synthesize_speech(text_input.text)
        return FileResponse(audio_path2, media_type="audio/mp3")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def read_root():
    return {"message": "Bienvenido al servicio TTS"}