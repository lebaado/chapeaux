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
