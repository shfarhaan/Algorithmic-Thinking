def is_anagram(first_string, second_string):
    letters1 = ""
    letters2 = ""
    for letter in first_string.lower():
        letters1 += letter if letter.isalpha() else ""
    for letter in second_string.lower():
        letters2 += letter if letter.isalpha() else ""
    return (sorted(letters1) == sorted(letters2))



str1 = "Eleven plus two?"
str2 = "One plus twelve!"
str3 = "A cinnamon roll?"
str4 = "No canola oil, Mr.!"
is_anagram(str1, str2)
is_anagram(str3, str4)