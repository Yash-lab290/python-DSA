class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        left, right = 1, num // 2
        while left <= right:
            mid = ( left + right) // 2
            midsqr = mid * mid 
            if midsqr == num:
                return True
            elif midsqr < num: 
                left = mid + 1 
            else: 
                right = mid - 1
        return False
S = Solution()
result = S.isPerfectSquare(13)  
print(result)       

    