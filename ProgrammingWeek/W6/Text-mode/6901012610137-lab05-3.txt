# ============================================
# Program: String Search and Palindrome Checker
# ============================================

# a. search for a character in a string (return index)
#    starting from the LEFT-hand side (index = 0)
def search_from_left(s, char):
    i = 0
    while i < len(s):
        if s[i] == char:
            return i
        i = i + 1
    return -1   # not found


# b. search for a character in a string (return index)
#    starting from the RIGHT-hand side (index = length-1)
def search_from_right(s, char):
    i = len(s) - 1
    while i >= 0:
        if s[i] == char:
            return i
        i = i - 1
    return -1   # not found


# e. boolean function to check whether a string is a palindrome
#    (using while loop)
def is_palindrome(s):
    # normalize: remove spaces and convert to lowercase
    # so that "An na" is treated the same as "anna"
    normalized = ""
    i = 0
    while i < len(s):
        if s[i] != " ":
            normalized = normalized + s[i].lower()
        i = i + 1

    left = 0
    right = len(normalized) - 1
    while left < right:
        if normalized[left] != normalized[right]:
            return False
        left = left + 1
        right = right - 1
    return True


# ============================================
# Main program
# ============================================
def main():
    # --- Part a & b: search for a character ---
    text = input("Enter a string to search in: ")
    ch = input("Enter a character to search for: ")

    left_index = search_from_left(text, ch)
    right_index = search_from_right(text, ch)

    print()
    print("String entered:", text)
    if left_index == -1:
        print("Character '" + ch + "' not found (searching from left).")
    else:
        print("First occurrence from LEFT  -> index:", left_index)

    if right_index == -1:
        print("Character '" + ch + "' not found (searching from right).")
    else:
        print("First occurrence from RIGHT -> index:", right_index)

    # --- Part e: palindrome check ---
    print()
    print("=== Palindrome Test ===")
    test_strings = ["Deed", "An na", "BKKrotorKKB", "25/8/52"]

    i = 0
    while i < len(test_strings):
        s = test_strings[i]
        result = is_palindrome(s)
        print('"' + s + '"', "-> Palindrome:", result)
        i = i + 1

    # allow user to test their own string too
    print()
    user_string = input("Enter your own string to test for palindrome: ")
    print('"' + user_string + '"', "-> Palindrome:", is_palindrome(user_string))


main()
#6901012610137
#Lab06-3