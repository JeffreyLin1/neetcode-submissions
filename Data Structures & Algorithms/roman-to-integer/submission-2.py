class Solution:
    def romanToInt(self, s: str) -> int:
        conversion = {}
        conversion['I'] = 1
        conversion['V'] = 5
        conversion['X'] = 10
        conversion['L'] = 50             
        conversion['C'] = 100
        conversion['D'] = 500
        conversion['M'] = 1000
        number = 0
        i = 0
        while i < len(s):
            c = s[i]
            if i < len(s)-1:
                if c == 'I' and s[i+1] == 'V':
                    number += 4
                elif c == 'I' and s[i+1] == 'X':
                    number += 9
                elif c == 'X' and s[i+1] == 'L':
                    number += 40
                elif c == 'X' and s[i+1] == 'C':
                    number += 90
                elif c == 'C' and s[i+1] == 'D':
                    number += 400
                elif c == 'C' and s[i+1] == 'M':
                    number += 900
                else:
                    number += conversion[c]
                    i -= 1
                i += 1
            else:
                number +=  conversion[c]
            i += 1
        return number
