vowels = ["a", "e", "i", "o", "u"]

def piglatin(str):
    if str[0] in vowels:
        return str + "ay"
    elif str[0] not in vowels and str[1] not in vowels:
        return str[2:] + str[0] + str[1] + "ay"
    elif str[0] not in vowels:
        return str[1:] + str[0] + "ay"

def translate(text):
    words = text.split(" ")
    translation = ""
    for word in words:
        new_word = piglatin(word)
        translation = translation + new_word + " "
    return translation

appleay = piglatin("apple")
ananabay = piglatin("banana")
ildchay = piglatin("child")
