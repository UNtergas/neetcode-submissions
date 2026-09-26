class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalized = ''.join(c.lower() for c in s if c.isalnum())
        right = len(normalized) - 1
        left= 0 
        while left < right:
            if normalized[left] != normalized[right]:
                return False
            left+=1
            right-=1
        return True


