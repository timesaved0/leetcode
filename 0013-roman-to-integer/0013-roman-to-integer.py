class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        for i in range(len(s) - 1):
            # If the current value is less than the next value, subtract it
            if roman_map[s[i]] < roman_map[s[i + 1]]:
                total -= roman_map[s[i]]
            else:
                total += roman_map[s[i]]
        
        # Add the value of the last character
        total += roman_map[s[-1]]
        
        return total
