# IA local con Groq

Dos apps en Streamlit que usan la API de [Groq](https://console.groq.com) a través del cliente de OpenAI:

- **`chatbot.py`**: chatbot experto en comida peruana (platos, ingredientes, historia y curiosidades). Usa el modelo `openai/gpt-oss-120b` con respuestas en streaming.
- **`transcripcion.py`**: transcribe al español audios mp3, wav, m4a u ogg (máx. 25 MB) con `whisper-large-v3-turbo`.

## Instalación

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Linux/macOS
pip install -r requirements.txt
```

Crea un archivo `.env` con tu clave de Groq:

```
GROQ_API_KEY=tu_clave_aqui
```

## Uso

```bash
streamlit run chatbot.py
streamlit run transcripcion.py --server.port 8502
```

Abre http://localhost:8501 (chatbot) o http://localhost:8502 (transcripción).
