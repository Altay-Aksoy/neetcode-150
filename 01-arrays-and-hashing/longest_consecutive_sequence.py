"""
LeetCode / NeetCode: Longest Consecutive Sequence
Difficulty: Medium
Link: https://neetcode.io/problems/longest-consecutive-sequence

Description:
Given an unsorted array of integers nums, return the length of the longest
consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""


# ==============================================================================
# Optimal Solution (Hash Set Sequence Boundary Checking)
# Time Complexity:  O(N) - Her eleman en fazla iki kez ziyaret edilir
# Space Complexity: O(N) - Hash set depolama alanı
# ==============================================================================
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set = set(nums)
        max_len = 0
        for n in nums_set:
            counter = 1
            if (n - 1) not in nums_set:
                while (n + 1) in nums_set:
                    n += 1
                    counter += 1
                max_len = max(max_len, counter)

        return max_len


# ==============================================================================
# Driver & Edge-Case Tests
# ==============================================================================
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        {
            "name": "Case 1: Standard Unsorted Sequence",
            "nums": [2, 20, 4, 10, 3, 4, 5],
            "expected": 4,  # [2, 3, 4, 5]
        },
        {
            "name": "Case 2: Classic NeetCode/LeetCode Case",
            "nums": [0, 3, 2, 5, 4, 6, 1, 1],
            "expected": 7,  # [0, 1, 2, 3, 4, 5, 6]
        },
        {
            "name": "Case 3: Empty Array",
            "nums": [],
            "expected": 0,
        },
        {
            "name": "Case 4: Single Element",
            "nums": [10],
            "expected": 1,
        },
        {
            "name": "Case 5: All Duplicate Elements",
            "nums": [7, 7, 7, 7],
            "expected": 1,
        },
        {
            "name": "Case 6: Negative and Zero Values",
            "nums": [-3, -2, -1, 0, 100],
            "expected": 4,  # [-3, -2, -1, 0]
        },
    ]

    print("=" * 70)
    print("Testing Longest Consecutive Sequence")
    print("=" * 70)

    for case in test_cases:
        actual = solution.longestConsecutive(case["nums"])
        status = "PASS" if actual == case["expected"] else "FAIL"
        print(f"\n[{case['name']}]")
        print(f"  Input   : {case['nums']}")
        print(f"  Expected: {case['expected']}")
        print(f"  Actual  : {actual} -> {status}")

    print("\n" + "=" * 70)
