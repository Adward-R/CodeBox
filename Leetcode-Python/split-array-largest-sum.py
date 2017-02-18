class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def valid(target):
            part_cnt, part_sum = 1, 0
            for num in nums:
                part_sum += num
                if part_sum > target:
                    part_sum = num
                    part_cnt += 1
                    if part_cnt > m:
                        return False
            return True

        max_num, sum_num = -1, 0
        for num in nums:
            if num > max_num:
                max_num = num
            sum_num += num

        if m == 1:
            return sum_num

        lo, hi = max_num, sum_num
        while lo <= hi:
            mid = (lo + hi) // 2
            if valid(mid):
                hi = mid - 1
            else:
                lo = mid + 1
        return lo


sol = Solution()
nums = [7,2,5,10,8]
print(sol.splitArray(nums, 2))