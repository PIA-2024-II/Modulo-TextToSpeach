from app.tts_service import synthesize_speech

def test_synthesize_speech():
    """
    Prueba la función de síntesis de texto a audio.

    Verifica que el archivo de audio se genere correctamente.
    """
    audio_path = synthesize_speech("Hola mundo")
    assert audio_path == "output.wav"