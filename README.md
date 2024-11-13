# Translathor - Technical Documentation

_A technical guide for the Translathor built with Python, integrating DeepL and ElevenLabs APIs for multilingual translation and text-to-speech functionality.  
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
- **dotenv** (environment variable management)
- **requests** (HTTP requests handling)
- **googletrans** (Google Translate integration for additional language support)

---

## Project Structure Summary


- **src/**: Contains all source code modules.
- **tmp/**: Directory for storing temporary audio files during playback.
- **.env**: Environment configuration file for sensitive keys.
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

## Technical Details

### `src/config.py`
Handles the loading of environment variables and provides configuration settings for the project.

### `src/main.py`
Acts as the main entry point for the tool, providing a CLI for translation and TTS functionalities.

#### Key Responsibilities:
- **Command Menu**: Provides options to translate text, set a default language, display supported languages, and exit.
- **Translation Handling**: Uses DeepL for supported languages and falls back to Google Translate for unsupported ones.
- **Text-to-Speech**: Utilizes ElevenLabs to convert translations into audio.

### `src/translator.py`
Handles translation functionality, including:

- **Language Validation**: Verifies language codes supported by DeepL, with Google Translate as a fallback.
- **DeepL Integration**: Translates text via DeepL’s API for supported languages.
- **Google Translate Integration**: Uses Google Translate for additional languages unsupported by DeepL.

### `src/tts.py`
Provides text-to-speech functionality using the ElevenLabs API.

#### Key Functions:
- **Audio Generation**: Converts translated text into audio and saves it in the specified path.
- **Audio Playback**: Plays the generated audio files and removes temporary files if cleanup is enabled.

### `src/utils.py`
Contains utility functions for displaying the command-line banner and managing user input.

---

## Dependencies Glossary
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
```

### Production Dependencies
- `requests`: Used for making HTTP requests to DeepL and ElevenLabs APIs.
- `dotenv`: Manages environment variables securely.
- `googletrans`: Provides fallback translation using Google Translate for unsupported languages in DeepL.

### Development Dependencies
- `pytest`: For testing.
- `flake8`: Linting and code style checks.

---

## API Integration Notes

### DeepL API
The DeepL API is the primary translation service, supporting a wide range of language codes. It dynamically fetches the list of supported languages from DeepL’s `/languages` endpoint to stay up-to-date.

#### Error Handling:
- **Fallback**: If DeepL does not support the target language or encounters an error, the tool automatically falls back to Google Translate.

### Google Translate
Implemented as a fallback using the `googletrans` library, this ensures translation support for additional languages beyond those offered by DeepL.

### ElevenLabs API
Handles TTS by converting translated text into audio. The tool uses the provided `VOICE_ID` to generate audio with the ElevenLabs TTS engine.

---

## Contact

For any questions or support, feel free to reach out:

- **GitHub**: [LouisPatigny](https://github.com/LouisPatigny)
- **Email**: patignylouis@gmail.com

---

Thank you for using Translathor! 🌍🔊
