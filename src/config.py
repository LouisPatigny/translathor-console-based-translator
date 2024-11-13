# config.py
"""
Configuration management for the translation and TTS application.
Handles loading of environment variables and default settings.
"""

import os
from dotenv import load_dotenv, find_dotenv

# Load environment variables from .env file
dotenv_path = find_dotenv('../.env', raise_error_if_not_found=True)
load_dotenv(dotenv_path=dotenv_path, override=True)

# API Keys and URLs
DEEPL_API_KEY = os.getenv('DEEPL_API_KEY')
DEEPL_API_URL = os.getenv('DEEPL_API_URL', 'https://api-free.deepl.com/v2/translate')
ELEVENLABS_API_KEY = os.getenv('ELEVENLABS_API_KEY')

# Default Settings
DEFAULT_TARGET_LANGUAGE = os.getenv('DEFAULT_TARGET_LANGUAGE', 'FR')
OUTPUT_AUDIO_PATH = os.getenv('OUTPUT_AUDIO_PATH', 'audio_output')
VOICE_ID = os.getenv('VOICE_ID', 'Your_Default_Voice_ID')
