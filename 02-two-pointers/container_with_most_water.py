"""
LeetCode / NeetCode: Container With Most Water
Difficulty: Medium
Link: https://neetcode.io/problems/max-water-container

Description:
You are given an integer array heights where heights[i] represents the height
of the i-th bar.

You may choose any two bars to form a container. Return the maximum amount of
water a container can store.
"""


# ==============================================================================
# Optimal Solution (Two Pointers - Inward Greedy Shrink)
# Time Complexity:  O(N) - Single pass inward scan
# Space Complexity: O(1) - Constant auxiliary space
# ==============================================================================
class Solution:
    def maxArea(self, heights: list[int]) -> int:
        len_heights = len(heights)
        i = 0
        j = len_heights - 1
        max_area = 0
        while i < j:
            exp = (j - i) * min(heights[j], heights[i])
            if max_area < exp:
                max_area = exp

            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1

        return max_area


# ==============================================================================
# Alternative Solution 1 (Brute Force - Nested Loops)
# Time Complexity:  O(N^2) - Checks all possible pairs
# Space Complexity: O(1)
# Note: Leads to Time Limit Exceeded (TLE) on large inputs.
# ==============================================================================
class NestedLoopsSolution:
    def maxArea(self, heights: list[int]) -> int:
        len_heights = len(heights)
        product = 0
        for i in range(len_heights):
            for j in range(i + 1, len_heights):
                exp = (j - i) * min(heights[j], heights[i])
                if exp > product:
                    product = exp

        return product


# ==============================================================================
# Alternative Solution 2 (Brute Force - Single While with Manual Reset)
# Time Complexity:  O(N^2) - Simulates nested iterations manually
# Space Complexity: O(1)
# ==============================================================================
class ManualResetSolution:
    def maxArea(self, heights: list[int]) -> int:
        len_heights = len(heights)
        product = 0
        i = 0
        j = len_heights - 1
        while True:
            trying = min(heights[i], heights[j]) * (j - i)
            if trying > product:
                product = trying
            i += 1
            if i == j:
                i = 0
                j -= 1
            if j == 0:
                break
        return product


# ==============================================================================
# Driver & Edge-Case Tests
# ==============================================================================
if __name__ == "__main__":
    solution = Solution()
    nested_solution = NestedLoopsSolution()
    manual_solution = ManualResetSolution()

    test_cases = [
        {
            "name": "Case 1: Standard Multi-Height Array",
            "heights": [1, 7, 2, 5, 4, 7, 3, 6],
            "expected": 36,
        },
        {
            "name": "Case 2: Minimal Array (Two Heights)",
            "heights": [2, 2, 2],
            "expected": 4,
        },
        {
            "name": "Case 3: Strictly Decreasing Heights",
            "heights": [9, 8, 7, 6, 5, 4, 3, 2, 1],
            "expected": 20,
        },
        {
            "name": "Case 4: Uniform Heights",
            "heights": [5, 5, 5, 5, 5],
            "expected": 20,
        },
        {
            "name": "Case 5: Peak in Center",
            "heights": [1, 2, 10, 10, 2, 1],
            "expected": 10,
        },
    ]

    print("=" * 70)
    print("Testing Container With Most Water")
    print("=" * 70)

    for case in test_cases:
        actual_opt = solution.maxArea(case["heights"])
        actual_nested = nested_solution.maxArea(case["heights"])
        actual_manual = manual_solution.maxArea(case["heights"])

        status_opt = "PASS" if actual_opt == case["expected"] else "FAIL"
        status_nested = "PASS" if actual_nested == case["expected"] else "FAIL"
        status_manual = "PASS" if actual_manual == case["expected"] else "FAIL"

        print(f"\n[{case['name']}]")
        print(f"  Input       : {case['heights']}")
        print(f"  Expected    : {case['expected']}")
        print(f"  Optimal O(N): {actual_opt} -> {status_opt}")
        print(f"  Nested O(N^2): {actual_nested} -> {status_nested}")
        print(f"  Manual O(N^2): {actual_manual} -> {status_manual}")

    print("\n" + "=" * 70)
