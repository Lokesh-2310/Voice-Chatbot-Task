from gtts import gTTS
import streamlit as st
import io

def speak_response(response_text) -> None:
    """
    Converts a given text response into speech and plays it in a Streamlit app using gTTS.

    This function uses the Google Text-to-Speech (gTTS) API to synthesize speech from text.
    Instead of saving the audio to disk, it writes the MP3 data to an in-memory buffer (BytesIO)
    and plays it directly in the Streamlit interface.

    Parameters:
    response_text : str
        The text content to be converted into spoken audio.

    Returns:
    None
        This function does not return any value. It plays the audio directly within the Streamlit UI.
    """
    
    # Generate speech
    tts = gTTS(text=response_text, lang='en')

    # Save to a BytesIO object (in-memory buffer)
    mp3_fp = io.BytesIO()
    tts.write_to_fp(mp3_fp)

    # Reset buffer position to start
    mp3_fp.seek(0)

    # Play in Streamlit
    st.audio(mp3_fp.read(), format='audio/mp3',autoplay=True)
