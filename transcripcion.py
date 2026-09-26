import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
if not os.getenv("GROQ_API_KEY"):
    st.error("Falta GROQ_API_KEY en el archivo .env")
    st.stop()
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY"),
)

st.set_page_config(page_title="Transcripción de Audios", page_icon="🎤")
st.title("🎤 Transcripción de Audios con Whisper")
st.write("Sube un archivo de audio (máx. 25 MB) y obtén su transcripción textual.")

archivo = st.file_uploader("Sube un archivo de audio", type=["mp3", "wav", "m4a", "ogg"])
if archivo is not None:
    st.audio(archivo, format=archivo.type)
    if st.button("Transcribir"):
        try:
            with st.spinner("Transcribiendo..."):
                transcripcion = client.audio.transcriptions.create(
                    model="whisper-large-v3-turbo",
                    file=archivo,
                    language="es",
                )
            st.success("Transcripción completada:")
            st.write(transcripcion.text)
        except Exception as e:
            st.error(f"Error: {e}")
            st.info("Verifica tu API key o el formato del archivo.")
