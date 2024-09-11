import re
from config import CHAR_REPLACEMENTS, FORBIDDEN_WORDS, FORBIDDEN_PHRASES

def normalize_word(word):
    normalized = word.lower()
    for char, replacement in CHAR_REPLACEMENTS.items():
        normalized = normalized.replace(char, replacement)
    return normalized

def contains_forbidden_word(text):
    text_lower = text.lower()
    for word in FORBIDDEN_WORDS:
        pattern = normalize_word(word).replace(r'\s*', r'\s*')  # игнорировать пробелы
        if re.search(pattern, text_lower):
            return True
    return False

def contains_forbidden_phrase(text):
    text_lower = text.lower()
    for phrase in FORBIDDEN_PHRASES:
        pattern = normalize_word(phrase).replace(r'\s*', r'\s*')  # игнорировать пробелы
        if re.search(pattern, text_lower):
            return True
    return False
