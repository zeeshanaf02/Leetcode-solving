class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        prevSetBits = 0
        prevMax = -math.inf  # the maximum of the previous segment
        currMax = -math.inf  # the maximum of the current segment
        currMin = math.inf
        for num in nums:
            setBits = num.bit_count()
            if setBits != prevSetBits:  # Start a new segment.
                if prevMax > currMin:
                    return False
                prevSetBits = setBits
                prevMax = currMax
                currMax = num
                currMin = num
            else:  # Continue with the current segment.
                currMax = max(currMax, num)
                currMin = min(currMin, num)

        return prevMax <= currMin