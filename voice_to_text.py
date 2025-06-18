from groq import Groq
from utils import VOICE_TO_TEXT_MODEL, GROQ_API_KEY

def convert_voice_to_text(stt_model=VOICE_TO_TEXT_MODEL, GROQ_API_KEY=GROQ_API_KEY, audio_filepath="output.mp3") -> str:
    """
    Transcribes speech from an audio file into text using GROQ's Whisper model API.

    Parameters:
    - stt_model (str): The name of the speech-to-text model to use (e.g., "whisper-large").
    - GROQ_API_KEY (str): API key for authenticating with the GROQ service.
    - audio_filepath (str): Path to the recorded audio file (must be in a supported format like MP3).

    Returns:
    - str: The transcribed text from the audio file.
    """

    # Initialize the Groq client with the provided API key
    client = Groq(api_key=GROQ_API_KEY)
    
    # Open the audio file in binary read mode
    audio_file = open(audio_filepath, "rb")

    # Call the transcription API
    transcription = client.audio.transcriptions.create(
        model=stt_model,    # The STT model to use (e.g., whisper)
        file=audio_file,    # The uploaded audio file
        language="en"       # Language of the audio content
    )

    # Return only the transcribed text
    return transcription.text

