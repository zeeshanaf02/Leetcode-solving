class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()

        n, m = len(robot), len(factory)
        # Initialize DP array, where dp[i][j] is the minimum distance for first i robots and j factories
        dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 0  # No robots, no distance

        for j in range(1, m + 1):  # j is the index for factories
            position, limit = factory[j - 1]
            dp[0][j] = 0  # No robots to repair with this factory

            for i in range(1, n + 1):  # i is the index for robots
                # Carry forward the minimum distance without using the current factory
                dp[i][j] = dp[i][j - 1]

                # Try assigning up to `limit` robots to this factory
                total_distance = 0
                for k in range(1, min(i, limit) + 1):
                    total_distance += abs(robot[i - k] - position)
                    dp[i][j] = min(dp[i][j], dp[i - k][j - 1] + total_distance)

        return dp[n][m]