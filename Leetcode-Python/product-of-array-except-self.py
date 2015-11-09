class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        #if n <= 1:
        #    return []
        products = [1] * (n-1) + [nums[-1]]
        for i in range(n-2, -1, -1):
            products[i] = products[i+1] * nums[i]
        mul = 1
        for i in range(n-1):
            products[i] = mul * products[i+1]
            mul *= nums[i]
        products[n-1] = mul
        return products

sol = Solution()
print(sol.productExceptSelf([5]))