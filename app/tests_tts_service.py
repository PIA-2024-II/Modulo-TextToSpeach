from gtts import gTTS
import os

def test_synthesize_speech(text: str) -> str:
    # Definir el nombre del archivo de salida
    audio_path = "output.mp3"
    
    # Crear el objeto gTTS
    tts = gTTS(text=text, lang='es')

    # Guardar el archivo de audio como MP3
    tts.save(audio_path)

    # Verificar si el archivo MP3 fue creado
    if not os.path.exists(audio_path):
        raise RuntimeError(f"Error: {audio_path} no fue creado.")

    return audio_path