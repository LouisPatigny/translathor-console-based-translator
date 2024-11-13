# main.py
"""
Main module to run the translation and TTS application.
"""

from translator import translate_with_deepl, is_valid_language_code, display_supported_languages
from tts import text_to_speech
from utils import display_banner, get_user_input
import config


def main():
    display_banner()
    while True:
        print("\nOptions:")
        print("1. Translate text")
        print(f"2. Set default target language (current: {config.DEFAULT_TARGET_LANGUAGE})")
        print("3. Display supported languages")
        print("4. Exit")

        choice = get_user_input("Enter your choice (1-4): ")
        if choice == '1':
            handle_translation()
        elif choice == '2':
            set_default_language()
        elif choice == '3':
            display_supported_languages()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def handle_translation():
    input_text = get_user_input("\nEnter the text to translate: ")
    if not input_text:
        print("No text entered. Returning to main menu.")
        return

    target_lang = get_user_input(
        f"Enter target language code (default: {config.DEFAULT_TARGET_LANGUAGE}): "
    ) or config.DEFAULT_TARGET_LANGUAGE

    while not is_valid_language_code(target_lang):
        print(f"'{target_lang}' is not a valid language code. Please enter a valid one.")
        target_lang = get_user_input("Enter a valid target language code: ").strip() or config.DEFAULT_TARGET_LANGUAGE

    translated_text, language_name = translate_with_deepl(input_text, target_lang)

    if translated_text:
        print(f"\nTranslated from {language_name} to {target_lang.upper()}:\n{translated_text}")
        if get_user_input("\nDo you want to hear the translation? (y/n): ").lower() == 'y':
            text_to_speech([translated_text])
    else:
        print("Translation failed. Please try again.")


def set_default_language():
    new_lang = get_user_input("Enter new default target language code: ")
    if new_lang:
        config.DEFAULT_TARGET_LANGUAGE = new_lang.upper()
        print(f"Default target language set to {config.DEFAULT_TARGET_LANGUAGE}")
    else:
        print("No language code entered. Default target language unchanged.")


if __name__ == "__main__":
    main()
