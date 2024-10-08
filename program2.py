def romanToInt(s: str) -> int:

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
    
    # Iterate over each character in the string
    for i in range(n):
        # Check if we're in a subtraction case
        if i < n - 1 and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
            total -= roman_to_int[s[i]]
        else:
            total += roman_to_int[s[i]]
    
    return total
