# tts.py
"""
Text-to-Speech module using ElevenLabs API.
"""

import time
import os
import uuid
import webbrowser
from elevenlabs import ElevenLabs, Voice, VoiceSettings
from config import ELEVENLABS_API_KEY, VOICE_ID, OUTPUT_AUDIO_PATH

# Initialize ElevenLabs client
client = ElevenLabs(api_key=ELEVENLABS_API_KEY)


def text_to_speech(texts, voice_id=VOICE_ID, cleanup=True):
    """
    Converts a list of texts to speech and plays them.

    Args:
        texts (list): List of texts to convert to speech.
        voice_id (str): Voice ID to use for TTS.
        cleanup (bool): Whether to delete audio files after playing.

    Returns:
        None
    """
    os.makedirs(OUTPUT_AUDIO_PATH, exist_ok=True)
    audio_files = []

    for text in texts:
        try:
            audio_stream = client.generate(
                text=text,
                voice=Voice(voice_id=voice_id, settings=VoiceSettings(stability=0.5, similarity_boost=0.5)),
                model="eleven_multilingual_v2"
            )

            file_name = f"{uuid.uuid4()}.mp3"
            file_path = os.path.join(OUTPUT_AUDIO_PATH, file_name)
            with open(file_path, 'wb') as f:
                for chunk in audio_stream:
                    f.write(chunk)
            audio_files.append(file_path)

            webbrowser.open(file_path)
            time.sleep(2)  # Allow time to open and play

        except Exception as e:
            print(f"TTS failed for text '{text}': {e}")

    if cleanup:
        for file_path in audio_files:
            if os.path.exists(file_path):
                os.remove(file_path)
