class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        base_n = base_x = 1
        while base_n <= n:
            if (x&base_x) == 0:
                if n&base_n:
                    x |= base_x
                base_n <<= 1
            base_x <<= 1
        return x
