class Solution:
    def countAndSay(self, n: int) -> str:
        def helper(s):
            result = ""
            count = 1
            for i in range(len(s)):
                # If it's the last character or the next character is different
                if i == len(s) - 1 or s[i] != s[i+1]:
                    # Append the count and the character to result
                    result += str(count) + s[i]
                    # Reset count for the next different character
                    count = 1
                else:
                    # Increment count if the next character is the same
                    count += 1
            return result
        
        ans = "1"
        for i in range(2, n + 1):
            ans = helper(ans)
            
        return ans