"""
LeetCode / NeetCode: Two Integer Sum II
Difficulty: Medium
Link: https://neetcode.io/problems/two-integer-sum-ii

Description:
Given an array of integers numbers that is sorted in non-decreasing order.
Return the indices (1-indexed) of two numbers, [index1, index2], such that they
add up to a given target number target and index1 < index2.

Constraints:
- Must use O(1) additional space.
- There will always be exactly one valid solution.
"""


# ==============================================================================
# Optimal Solution (Two Pointers - Inward Scan)
# Time Complexity:  O(N) - Single pass with convergent pointers
# Space Complexity: O(1) - Constant auxiliary space
# ==============================================================================
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i1, i2 = 0, len(numbers) - 1
        while numbers[i1] + numbers[i2] != target:
            if numbers[i1] + numbers[i2] < target:
                i1 += 1
            else:
                i2 -= 1

        return [i1 + 1, i2 + 1]


# ==============================================================================
# Driver & Edge-Case Tests
# ==============================================================================
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        {
            "name": "Case 1: Standard Positive Array",
            "numbers": [1, 2, 3, 4],
            "target": 3,
            "expected": [1, 2],
        },
        {
            "name": "Case 2: Array with Negatives and Zero",
            "numbers": [-5, -3, 0, 2, 4, 6, 8],
            "target": 5,
            "expected": [2, 7],  # numbers[1] (-3) + numbers[6] (8) = 5
        },
        {
            "name": "Case 3: Two Elements Minimal",
            "numbers": [2, 7],
            "target": 9,
            "expected": [1, 2],
        },
        {
            "name": "Case 4: Duplicates in Array",
            "numbers": [1, 2, 2, 4, 5],
            "target": 4,
            "expected": [2, 3],  # numbers[1] (2) + numbers[2] (2) = 4
        },
    ]

    print("=" * 70)
    print("Testing Two Integer Sum II (Two Pointers)")
    print("=" * 70)

    for case in test_cases:
        actual = solution.twoSum(case["numbers"], case["target"])
        status = "PASS" if actual == case["expected"] else "FAIL"
        print(f"\n[{case['name']}]")
        print(f"  Numbers : {case['numbers']}")
        print(f"  Target  : {case['target']}")
        print(f"  Expected: {case['expected']}")
        print(f"  Actual  : {actual} -> {status}")

    print("\n" + "=" * 70)
