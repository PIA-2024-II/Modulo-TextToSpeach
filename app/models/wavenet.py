import numpy as np

class WaveNet:
    def generate_audio(self, mel_spectrogram):
        """
        Genera un audio a partir de un espectrograma mel.

        Args:
            mel_spectrogram (np.ndarray): Espectrograma mel de entrada.

        Returns:
            np.ndarray: Señal de audio simulada.
        """
        return np.random.rand(22050 * 5).astype(np.float32)