"""
Vulgar word encoding/decoding for bypassing Gemini content policy.
Gemini is told to output base64-like codes instead of actual words.
We decode them before displaying to the user.
"""

# Use simple short alphanumeric codes instead of base64 strings.
# Gemini mangles base64 padding (== / =). Codes are random-looking 4-6 char strings.
CODES = {
    "xk7mQ": "madarchod",
    "pL9nR": "bhenchod",
    "qW2bX": "bhenaloda",
    "vH8jT": "bhosdina",
    "gF4kY": "bhosbhangi",
    "mN6zE": "hijdu",
    "jD1wS": "naidu",
    "tR5uA": "gandu",
    "sB3cP": "randi",
    "hK7dM": "chutiya",
    "wX9fG": "lowde",
    "yL2nV": "landur",
    "aQ6kJ": "ganduk",
    "eU8rZ": "bhen",
    "iF3oC": "maa",
    "rT5bH": "baap",
    "nW1mK": "randis",
    "xP4sL": "gandu",
    "cV7gQ": "chod",
    "zM9jR": "choda",
    "bN2kT": "chaale",
    "dY6wE": "madar",
}

def decode_vulgar(text):
    """Replace all encoded vulgar codes in text with their original words."""
    if not text:
        return text
    for code, word in CODES.items():
        text = text.replace(code, word)
    return text
