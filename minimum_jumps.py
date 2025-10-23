# minimum_jumps.py
"""
Minimum Steps to Reach the End
Given an array of non-negative integers where each element
represents the maximum number of steps that can be moved
forward from that position, return the minimum number of jumps
to reach the last index, or -1 if it's not reachable.
Time: O(n), Space: O(1)
"""

from typing import List

def min_jumps(arr: List[int]) -> int:
    n = len(arr)
    if n <= 1:
        return 0
    if arr[0] == 0:
        return -1

    jumps = 0
    current_end = 0  # boundary for current jump
    farthest = 0     # farthest reachable index so far

    # iterate until the second-to-last index (we don't need to step from last)
    for i in range(n - 1):
        # update the farthest we can reach from i
        farthest = max(farthest, i + arr[i])

        # when we reach the end of the current range, we must jump
        if i == current_end:
            jumps += 1
            current_end = farthest
            # if we can't progress further, unreachable
            if current_end <= i:
                return -1
            # early exit if we can already reach the end
            if current_end >= n - 1:
                break

    return jumps

# Simple CLI test harness
if __name__ == "__main__":
    tests = [
        ([2, 3, 1, 1, 4], 2),
        ([1, 0, 3, 2, 1], -1),
        ([0], 0),
        ([1, 2], 1),
        ([2,0,0], 1),
        ([3,2,1,0,4], -1),  # classic unreachable
        ([4,1,1,3,1,1,1], 2) # can jump directly to end
    ]

    for arr, expected in tests:
        out = min_jumps(arr)
        print(f"{arr} -> {out} (expected: {expected})")
