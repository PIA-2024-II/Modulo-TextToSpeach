# TTS Microservice

Este microservicio es un prototipo que convierte texto en mapudungun a audio utilizando Tacotron 2 y WaveNet.

## Ejecutar entorno virtual

```bash
venv\Scripts\activate
```

## Si no ejecutar -> para crear uno nuevo

```bash
python -m venv venv
pip install -r requirements.txt
```

## Uso
Ejecuta el servicio con:

```bash
uvicorn app.main:app --reload
```
Esto levantará el servidor en http://localhost:8000 y se podrá acceder a la documentación automática en http://localhost:8000/docs.

## Notas

Para esta versión del prototipo se utilizan modelos preentrenados en español como punto de partida.