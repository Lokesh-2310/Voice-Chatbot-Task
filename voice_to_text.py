from groq import Groq
import streamlit as st 
from utils import VOICE_TO_TEXT_MODEL, GROQ_API_KEY

def convert_voice_to_text(stt_model=VOICE_TO_TEXT_MODEL, GROQ_API_KEY=GROQ_API_KEY, audio_filepath="output.wav") -> str:
    """
    Transcribes speech from a WAV audio file into text using GROQ's Whisper model API.

    Args:
        stt_model (str): Name of the speech-to-text model (e.g., "whisper-large").
        GROQ_API_KEY (str): API key for GROQ Whisper transcription.
        audio_filepath (str): Path to the recorded WAV audio file.

    Returns:
        str: Transcribed text from the audio.
    """
    client = Groq(api_key=GROQ_API_KEY)
    try :
        with open(audio_filepath, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                model=stt_model,
                file=audio_file,
                language="en"
            )

        return transcription.text
    
    except : 
        st.error("Audio is too short.")
