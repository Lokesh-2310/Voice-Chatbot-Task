import streamlit as st
from audio_recorder_streamlit import audio_recorder
import time
import os

def record_audio(file_path="output.wav"):
    """
    Records audio using Streamlit's browser-based recorder and saves it as a WAV file.

    Args:
        file_path (str): Path to save the recorded audio (default: 'output.wav')

    Returns:
        bytes: The raw audio bytes recorded from the browser, or None if no recording
    """
    
    if os.path.exists(file_path):
        os.remove(file_path)
    
    st.info("Click the mic icon and start speaking...")

    audio_bytes = audio_recorder(text="Click and Speak", pause_threshold=1, sample_rate=44100, icon_size="2x",recording_color="#e8b62c",
    neutral_color="#6aa36f")
    
    time.sleep(1)
    
    st.info("Click the mic icon again to stop recording manually...")

    if audio_bytes:
        st.success("Recording received!")
        # Save directly as WAV file
        with open(file_path, "wb") as f:
            f.write(audio_bytes)
        return True
    
    return None
