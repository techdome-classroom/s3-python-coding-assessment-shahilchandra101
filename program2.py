function romanToInt(s) {
 
    const romanMap = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    };
    
    let total = 0;
    let prevValue = 0;

    for (let i = s.length - 1; i >= 0; i--) {
        const currentValue = romanMap[s[i]];

        // If the current value is smaller than the previous value, subtract it
        if (currentValue < prevValue) {
            total -= currentValue;
        } else {
            // Otherwise, add the current value
            total += currentValue;
        }

        // Update the previous value for the next iteration
        prevValue = currentValue;
    }

    return total;
}

// Export the function for testing
module.exports = { romanToInt };