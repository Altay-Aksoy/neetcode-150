"""
LeetCode / NeetCode: Two Sum
Difficulty: Easy
Link: https://neetcode.io/problems/two-integer-sum
"""


# ==============================================================================
# Optimal Solution (One-pass Hash Map)
# Time Complexity:  O(N)
# Space Complexity: O(N)
# ==============================================================================
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prev_dict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in prev_dict:
                return [prev_dict[diff], i]
            prev_dict[nums[i]] = i


# ==============================================================================
# Alternative Solution (Brute Force)
# Time Complexity:  O(N^2)
# Space Complexity: O(1)
# ==============================================================================
class AlternativeSolution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# ==============================================================================
# Tests
# ==============================================================================
if __name__ == "__main__":
    solution = Solution()
    alt_solution = AlternativeSolution()

    test_cases = [
        ([3, 4, 5, 6], 7, [0, 1]),
        ([4, 5, 6], 10, [0, 2]),
        ([5, 5], 10, [0, 1]),
    ]

    print("--- Optimal Solution (Hash Map) ---")
    for nums, target, expected in test_cases:
        result = solution.twoSum(nums, target)
        print(f"nums={nums}, target={target} -> {result} (Expected: {expected})")

    print("\n--- Alternative Solution (Brute Force) ---")
    for nums, target, expected in test_cases:
        result = alt_solution.twoSum(nums, target)
        print(f"nums={nums}, target={target} -> {result} (Expected: {expected})")
