# Define the dictionary mapping letters to Dancing Men figures
dancing_men = {
    "A": "🕴️🕴️🕴️🕴️🕴️",
    "B": "🕴️🕴️🕴️🕴️💃",
    "C": "🕴️🕴️🕴️💃🕴️",
    "D": "🕴️🕴️🕴️💃💃",
    "E": "🕴️🕴️💃🕴️🕴️",
    "F": "🕴️🕴️💃🕴️💃",
    "G": "🕴️🕴️💃💃🕴️",
    "H": "🕴️🕴️💃💃💃",
    "I": "🕴️💃🕴️🕴️🕴️",
    "J": "🕴️💃🕴️🕴️💃",
    "K": "🕴️💃🕴️💃🕴️",
    "L": "🕴️💃🕴️💃💃",
    "M": "🕴️💃💃🕴️🕴️",
    "N": "🕴️💃💃🕴️💃",
    "O": "🕴️💃💃💃🕴️",
    "P": "🕴️💃💃💃💃",
    "Q": "💃🕴️🕴️🕴️🕴️",
    "R": "💃🕴️🕴️🕴️💃",
    "S": "💃🕴️🕴️💃🕴️",
    "T": "💃🕴️🕴️💃💃",
    "U": "💃🕴️💃🕴️🕴️",
    "V": "💃🕴️💃🕴️💃",
    "W": "💃🕴️💃💃🕴️",
    "X": "💃🕴️💃💃💃",
    "Y": "💃💃🕴️🕴️🕴️",
    "Z": "💃💃🕴️🕴️💃"
}

# Define a function to encode text into Dancing Men cipher
def encode_dancing_men(text):
    encoded_text = ""
    for char in text.upper():
        if char.isalpha():
            encoded_text += dancing_men[char] + " "
        else:
            encoded_text += char
    return encoded_text

user_text = input("Your text: \n")
print(encode_dancing_men(user_text))