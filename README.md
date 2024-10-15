# TTS Microservice

Este microservicio es un prototipo que convierte texto a audio utilizando GTTS.

## Crear entorno virtual, para crear uno nuevo:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Uso
Ejecuta el servicio con:

```bash
uvicorn app.main:app --reload
```
Esto levantará el servidor en http://localhost:8000 y se podrá acceder a la documentación automática en http://localhost:8000/docs.