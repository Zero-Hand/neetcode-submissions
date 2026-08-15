class Solution:
    
    import re
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^a-zA-Z0-9]', '', s)

        x = s[::-1]

        if x == s:
            return True
        else:
            return False