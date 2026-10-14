def countChar(A, B):
    i, count = 0, 0
    while(i < len(B)):
        if(B[i].lower() == A.lower()):
            count += 1
        i += 1
    return count

def countVowels(A):
    i, count, V = 0, 0, ['a','e','i','o','u']
    while(i < len(V)):
        count += countChar(V[i], A)
        i += 1
    return count

def countWords(A):
    count = 1
    count += countChar(" ", A)
    return count

word = """Human and Ai can make mistake"""
letter = "a"

print(f"The letter '{letter}' appears {countChar(letter, word)} times in '{word}'")
print(f"There are {countVowels(word)} vowels in '{word}'")
print(f"There are {countWords(word)} words in '{word}'")

#6901012610137
#Lab06-6