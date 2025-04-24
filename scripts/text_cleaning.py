import re
from spellchecker import SpellChecker


spell = SpellChecker(distance=1)

def clean_text(text):
    """Basic cleanup of OCR output."""
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s.,]', '', text)        # remove special chars
    text = re.sub(r'\s+', ' ', text).strip()          # normalize whitespace
    return text

def correct_spelling(text):
    spell_checker = SpellChecker()  # Initialize SpellChecker
    corrected = []
    for word in text.split():
        corrected_word = spell_checker.correction(word)
        corrected.append(corrected_word)
    return corrected



def preprocess_ocr_output(ocr_text):
    if ocr_text is None or ocr_text.strip() == "":
        raise ValueError("OCR output is empty or invalid.")
    
    # Now clean and correct the text
    cleaned = clean_text(ocr_text)
    corrected = correct_spelling(cleaned)
    return ' '.join(corrected)

