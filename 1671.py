class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        N = len(nums)

        # Step 1: Calculate LIS (Longest Increasing Subsequence) ending at each index
        lis = [1] * N
        for i in range(N):
            for j in range(i):
                if nums[j] < nums[i]:
                    lis[i] = max(lis[i], lis[j] + 1)

        # Step 2: Calculate LDS (Longest Decreasing Subsequence) starting from each index
        lds = [1] * N
        for i in range(N - 1, -1, -1):
            for j in range(i + 1, N):
                if nums[j] < nums[i]:
                    lds[i] = max(lds[i], lds[j] + 1)

        # Step 3: Find the minimum number of elements to remove
        res = N
        for i in range(1, N - 1):
            # Ensure there is a peak by checking lis[i] > 1 and lds[i] > 1
            if lis[i] > 1 and lds[i] > 1:
                # Calculate the number of elements to remove to make it a mountain array
                res = min(res, N - (lis[i] + lds[i] - 1))

        return res