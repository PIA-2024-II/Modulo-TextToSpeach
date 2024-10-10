from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    """
    Prueba el endpoint raíz.

    Verifica que el mensaje de bienvenida sea correcto.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenido al servicio TTS"}

def test_synthesize():
    """
    Prueba el endpoint de síntesis.

    Envía texto y verifica que el tipo de respuesta sea audio WAV.
    """
    response = client.post("/synthesize/", json={"text": "Hola mundo"})
    assert response.status_code == 200
    assert response.headers["content-type"] == "audio/wav"