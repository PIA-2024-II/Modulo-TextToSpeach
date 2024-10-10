import numpy as np

class Tacotron2:
    def generate_mel(self, text):
        """
        Genera un espectrograma mel a partir del texto.

        Args:
            text (str): Texto para convertir.

        Returns:
            np.ndarray: Espectrograma mel simulado.
        """
        return np.random.rand(80, 400)