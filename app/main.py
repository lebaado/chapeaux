def caesar_cipher(text: str, key: int = 1) -> str:
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for letter in text:        
        if letter not in lowercase and letter not in uppercase:
                result += letter
        elif letter in lowercase:
            pos = lowercase.find(letter)
            new_index = (pos + key) % 26
            result += lowercase[new_index]
        elif letter in uppercase:
            pos = uppercase.find(letter)
            new_index = (pos + key) % 26
            result += uppercase[new_index]
        
    return result


FRENCH_FREQUENCIES = {
    "a": 7.6, "b": 0.9, "c": 3.3, "d": 3.7, "e": 14.7, "f": 1.1, "g": 0.9,
    "h": 0.7, "i": 7.5, "j": 0.5, "k": 0.1, "l": 5.5, "m": 3.0, "n": 7.1,
    "o": 5.4, "p": 3.0, "q": 1.4, "r": 6.6, "s": 7.9, "t": 7.2, "u": 6.3,
    "v": 1.6, "w": 0.1, "x": 0.4, "y": 0.3, "z": 0.1,
}


def cesar_decipher(text: str, key: int = None) -> str:
    if key is not None:
        return caesar_cipher(text, -key)

    best_text = text
    best_score = -1.0
    for candidate_key in range(26):
        candidate = caesar_cipher(text, -candidate_key)
        score = 0.0
        for letter in candidate.lower():
            score += FRENCH_FREQUENCIES.get(letter, 0.0)
        if score > best_score:
            best_score = score
            best_text = candidate

    return best_text
