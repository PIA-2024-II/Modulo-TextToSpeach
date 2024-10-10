from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from app.tts_service import synthesize_speech

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/synthesize/")
async def synthesize(text_input: TextInput):
    """
    Convierte texto a audio.

    Args:
        text_input (TextInput): Texto en Mapudungun para sintetizar.

    Returns:
        FileResponse: Archivo de audio en formato WAV.
    """
    try:
        audio_path = synthesize_speech(text_input.text)
        return FileResponse(audio_path, media_type="audio/wav")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def read_root():
    """
    Endpoint raíz de bienvenida.

    Returns:
        dict: Mensaje de bienvenida.
    """
    return {"message": "Bienvenido al servicio TTS"}