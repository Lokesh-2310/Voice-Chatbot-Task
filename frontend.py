import streamlit as st 
from getting_audio import record_audio
from voice_to_text import convert_voice_to_text
from chatbot_response import response_by_chatbot
from speech import speak_response

voice_text=None
prompt=None

st.title("🎙️Voice Assistant Chatbot")
st.markdown("Speak into the mic and get a smart response powered by GROQ Llama Model!")

with st.sidebar:
        status=record_audio()
        if status:
            voice_text = convert_voice_to_text()

prompt = st.chat_input("Say something using voice interaction")
if prompt or voice_text:
    if prompt is not None:
        with st.chat_message("human"):
            st.write(prompt)

        response = response_by_chatbot(prompt)
        
        
        with st.chat_message("ai"):
            speak_response(response_text=response)
            st.write(response)
            
    elif voice_text is not None: 
        with st.chat_message("human"):
            st.write(voice_text)
            
        response = response_by_chatbot(voice_text)

        with st.chat_message("ai"):
            speak_response(response_text=response)
            st.write(response)
            
    else:
        st.error("Provide me the query.")
        
