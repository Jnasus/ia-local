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

st.set_page_config(page_title="Chatbot de Comida Peruana", page_icon="🍲")
st.title("🍲 Chatbot de Comida Peruana")
st.write("Pregúntame sobre platos típicos, ingredientes, historia y más.")

if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "system",
        "content": "Eres un experto en comida peruana. Respondes de forma amable, "
                   "con datos históricos y curiosidades. Si no sabes algo, lo dices."
    }]

for m in st.session_state.messages:
    if m["role"] != "system":
        with st.chat_message(m["role"]):
            st.write(m["content"])

if prompt := st.chat_input("¿Qué quieres saber sobre la comida peruana?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    try:
        with st.chat_message("assistant"):
            stream = client.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=st.session_state.messages,
                stream=True,
            )
            respuesta = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": respuesta})
    except Exception as e:
        st.session_state.messages.pop()  # no dejar la pregunta sin respuesta en el historial
        st.error(f"Error: {e}")
        st.info("Verifica tu API key o tu conexión a internet.")
