def decimal_to_binary(n):
    if n == 0:
        return "0"
    
    binary_digits = ""
    while n > 0:
        remainder = n % 2
        binary_digits = str(remainder) + binary_digits  # prepend digit
        n = n // 2
    
    return binary_digits

decimal = int(input("Enter a decimal number: "))
result = decimal_to_binary(decimal)
print(f"Binary: {result}")

#6901012610137
#lab03-5