# translator.py
import requests
from iso639 import to_name
from config import DEEPL_API_KEY, DEEPL_API_URL

# Cache for supported languages to avoid repeated API calls
SUPPORTED_LANGUAGES = None


def get_supported_languages():
    global SUPPORTED_LANGUAGES
    if SUPPORTED_LANGUAGES is None:
        try:
            response = requests.get(f"{DEEPL_API_URL.replace('/translate', '/languages')}?type=target",
                                    headers={'Authorization': f'DeepL-Auth-Key {DEEPL_API_KEY}'})
            response.raise_for_status()
            SUPPORTED_LANGUAGES = [{"code": lang["language"], "name": lang["name"]} for lang in response.json()]
        except requests.RequestException as e:
            print(f"Error retrieving supported languages: {e}")
            SUPPORTED_LANGUAGES = [{"code": "EN", "name": "English"}, {"code": "FR", "name": "French"}]  # Fallback
    return SUPPORTED_LANGUAGES


def is_valid_language_code(code):
    supported_languages = {lang["code"] for lang in get_supported_languages()}
    return code.upper() in supported_languages

def display_supported_languages():
    languages = get_supported_languages()
    print("\nSupported Languages:")
    for lang in languages:
        print(f"{lang['name']} ({lang['code']})")
    print()  # Blank line for readability


def translate_with_deepl(text, target_lang):
    """
    Translates text using DeepL API with automatic language detection.

    Args:
        text (str): The text to translate.
        target_lang (str): The target language code.

    Returns:
        tuple: Translated text and detected/source language name.
    """
    if not is_valid_language_code(target_lang):
        print(f"Invalid language code '{target_lang}'. Please enter a valid code.")
        return None, None

    headers = {
        'Authorization': f'DeepL-Auth-Key {DEEPL_API_KEY}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'text': text,
        'target_lang': target_lang.upper()
    }

    try:
        response = requests.post(DEEPL_API_URL, headers=headers, data=data)
        response.raise_for_status()
        result = response.json()
        translated_text = result['translations'][0]['text']
        detected_source_lang = result['translations'][0].get('detected_source_language', 'unknown')
        language_name = to_name(detected_source_lang.lower())
        print(f"Debug: Detected source language - '{detected_source_lang}'")
        return translated_text, language_name
    except requests.RequestException as e:
        print(f"Translation failed: {e}")
        return None, None
