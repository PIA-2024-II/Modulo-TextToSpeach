import torch
import numpy as np
from scipy.io.wavfile import write
from app.models.tacotron2 import Tacotron2
from app.models.wavenet import WaveNet

def synthesize_speech(text: str) -> str:
    """
    Genera un archivo de audio a partir de texto usando Tacotron 2 y WaveNet.

    Args:
        text (str): Texto para convertir a audio.

    Returns:
        str: Ruta del archivo de audio generado.
    """
    # Instancia modelos (simulación para este ejemplo)
    tacotron2 = Tacotron2()
    wavenet = WaveNet()

    # Genera espectrograma mel
    mel_spectrogram = tacotron2.generate_mel(text)
    
    # Convierte mel a audio
    audio = wavenet.generate_audio(mel_spectrogram)

    # Guarda el audio
    audio_path = "output.wav"
    write(audio_path, 22050, audio)
    return audio_path