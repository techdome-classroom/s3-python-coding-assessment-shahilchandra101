def romanToInt(s: str) -> int:
    # Mapping of Roman numerals to integers
    roman_to_int = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    n = len(s)
    
    # Loop through the string s
    for i in range(n):
        # If the current symbol is less than the next one, subtract it
        if i < n - 1 and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
            total -= roman_to_int[s[i]]
        else:
            # Otherwise, add it
            total += roman_to_int[s[i]]
    
    return total
