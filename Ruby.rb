def piglatin(str)
    vowels = ["a", "e", "i", "o", "u"]
    length = str.length()
    if vowels.include? str[0]
        return str + "ay"
        elsif vowels.include? str[0] and vowels.include? str[1]
        return str[2..length-1] + str[0] + str[1] + "ay"
        elsif not vowels.include? str[0]
        return str[1..length-1] + str[0] + "ay"
    end
end

def translate(text)
    words = text.split(" ")
    translation = ""
    for i in 0..words.length()-1
        new_word = piglatin(words[i])
        translation = translation + new_word + " "
    end
    return translation
end
