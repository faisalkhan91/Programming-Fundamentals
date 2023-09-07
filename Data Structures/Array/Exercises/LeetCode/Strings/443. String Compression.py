"""
443. String Compression
https://leetcode.com/problems/string-compression/?envType=study-plan-v2&envId=leetcode-75
"""

class Solution:
    def compress(self, chars: List[str]) -> int:
        s = []
        current_char = ""
        next_char = ""
        count = 0

        for i in range(len(chars)):
            print(current_char, next_char)
            if current_char == "" or current_char != next_char:
                if current_char != "":
                    s.append(current_char)
                    s.append(str(count))
                current_char = chars[i]
                count = 0
            elif current_char == next_char:
                count += 1
            next_char = chars[i]
        s.append(current_char)
        s.append(str(count))
        print(s)