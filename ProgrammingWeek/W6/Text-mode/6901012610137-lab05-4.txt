def countChar(A, B):
    i, count = 0, 0
    while(i < len(B)):
        if(B[i].lower() == A.lower()):
            count += 1
        i += 1
    return count

word = "Thailand"
letter = "a"

print(f"The letter '{letter}' appears {countChar(letter, word)} times in '{word}'")
#6901012610137
#Lab06-4