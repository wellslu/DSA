class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x>=0:
            return int(str(x)[::-1])==x
        else:
            return False
