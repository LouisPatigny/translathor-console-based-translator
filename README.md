# Translathor - Technical Documentation

_A technical guide for Translathor built with Python, integrating DeepL and ElevenLabs APIs for multilingual translation and text-to-speech functionality.  
This documentation provides developers with a detailed understanding of the system architecture, supported features, and integration points._

---

## Table of Contents
- [Technologies Used](#technologies-used)
- [Project Structure Summary](#project-structure-summary)
- [Required Environment Variables](#required-environment-variables)
- [Technical Details](#technical-details)
- [Dependencies Glossary](#dependencies-glossary)
- [API Integration Notes](#api-integration-notes)
- [Contact](#contact)

---

## Technologies Used

- **Python** (3.9+)
- **DeepL API** (for translation)
- **ElevenLabs API** (for text-to-speech)
- **python-dotenv** (environment variable management)
- **requests** (HTTP requests handling)
- **deep-translator** (DeepL API integration)
- **iso639** (language code conversion)
- **httpx** (required by ElevenLabs API client)

---

## Project Structure Summary

```
translation-tool/
├── src/
│   ├── config.py
│   ├── main.py
│   ├── translator.py
│   ├── tts.py
│   └── utils.py
├── tmp/
│   └── ... (temporary audio files)
├── .env
├── .gitignore
├── README.md
├── requirements.txt
```

- **src/**: Contains all source code modules.
- **tmp/**: Directory for storing temporary audio files during playback.
- **.env**: Environment configuration file for sensitive keys.
- **requirements.txt**: Lists all Python dependencies required for the project.
- **README.md**: Project documentation.

---

## Required Environment Variables

To run this tool, create a `.env` file in the root directory with the following variables:

```
DEEPL_API_KEY=[YOUR DEEPL API KEY]           # Obtain from DeepL API
ELEVENLABS_API_KEY=[YOUR ELEVENLABS API KEY] # Obtain from ElevenLabs
VOICE_ID=[YOUR ELEVENLABS VOICE ID]          # Choose or create a voice in ElevenLabs
DEFAULT_TARGET_LANGUAGE=FR                   # Default language code (e.g., 'FR' for French)
OUTPUT_AUDIO_PATH=tmp                        # Folder to store audio files
```

---

## Usage

To use Translathor, follow these steps:

1. **Install Dependencies**:
   Install the required dependencies by running:

```bash
pip install -r requirements.txt
```

**Set Up Environment Variables**: Make sure you have configured your `.env` file with the necessary API keys and settings (see [Required Environment Variables](#required-environment-variables)).

**Run the Application**: Start the tool by running the `main.py` file:

```bash
python src/main.py
```

**Using the Menu**: The application will present a menu with the following options:

1. **Translate text**: Enter text and select a target language for translation.
2. **Set default target language**: Change the default target language.
3. **Display supported languages**: Shows a list of languages supported by DeepL.
4. **Exit**: Quit the application.

**Text-to-Speech Option**: After a successful translation, you’ll be prompted to play the translated text using ElevenLabs. Select "y" to hear the translation or "n" to skip.


## Technical Details

### `src/config.py`
Handles the loading of environment variables and provides configuration settings for the project.

### `src/main.py`
Acts as the main entry point for the tool, providing a CLI for translation and TTS functionalities.

#### Key Responsibilities:
- **Command Menu**: Provides options to translate text, set a default language, display supported languages, and exit.
- **Translation Handling**: Uses DeepL for detecting and translating language.
- **Text-to-Speech**: Utilizes ElevenLabs to convert translations into audio.

### `src/translator.py`
Handles translation functionality, including:

- **Language Validation**: Verifies language codes supported by DeepL.
- **DeepL Integration**: Translates text via DeepL’s API for supported languages.

### `src/tts.py`
Provides text-to-speech functionality using the ElevenLabs API.

#### Key Functions:
- **Audio Generation**: Converts translated text into audio and saves it in the specified path.
- **Audio Playback**: Plays the generated audio files and removes temporary files if cleanup is enabled.

### `src/utils.py`
Contains utility functions for displaying the command-line banner and managing user input.

---

## Dependencies Glossary

### Production Dependencies
- `requests`: Used for making HTTP requests to the DeepL and ElevenLabs APIs.
- `python-dotenv`: Manages environment variables securely.
- `deep-translator`: Enables translation functionality using the DeepL API.
- `iso639`: Provides language code to language name conversions.
- `elevenlabs`: Handles text-to-speech functionality using the ElevenLabs API.
- `httpx`: Required by the ElevenLabs API client for HTTP requests.

---

## API Integration Notes

### DeepL API
The DeepL API is the primary translation service, supporting a wide range of language codes. It dynamically fetches the list of supported languages from DeepL’s `/languages` endpoint to stay up-to-date.

### ElevenLabs API
Handles TTS by converting translated text into audio. The tool uses the provided `VOICE_ID` to generate audio with the ElevenLabs TTS engine.

---

## Contact

For any questions or support, feel free to reach out:

- **GitHub**: [LouisPatigny](https://github.com/LouisPatigny)
- **Email**: patignylouis@gmail.com

---

Thank you for using Translathor! 🌍🔊
