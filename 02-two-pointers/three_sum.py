"""
LeetCode / NeetCode: 3Sum
Difficulty: Medium
Link: https://neetcode.io/problems/three-integer-sum

Description:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""


# ==============================================================================
# Optimal Solution (Sorting + Two Pointers with Inward Scan)
# Time Complexity:  O(N^2) - O(N log N) sorting + O(N^2) two-pointer scans
# Space Complexity: O(1) auxiliary space (ignoring sorting/output space)
# ==============================================================================
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        answer = []
        nums.sort()

        len_nums = len(nums)
        for i in range(len_nums - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            i1, i2 = i + 1, len_nums - 1
            while i1 < i2:
                if nums[i1] + nums[i2] < -nums[i]:
                    i1 += 1
                elif nums[i1] + nums[i2] > -nums[i]:
                    i2 -= 1
                else:
                    answer.append([nums[i1], nums[i2], nums[i]])
                    i1 += 1
                    while nums[i1] == nums[i1 - 1] and i1 < i2:
                        i1 += 1

        return answer


# ==============================================================================
# Driver & Edge-Case Tests
# ==============================================================================
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        {
            "name": "Case 1: Standard Mixed Positive & Negative",
            "nums": [-1, 0, 1, 2, -1, -4],
            "expected": [[-1, 2, -1], [0, 1, -1]],  # Distinct sets of triplets
        },
        {
            "name": "Case 2: No Triplets Sum to Zero",
            "nums": [0, 1, 1],
            "expected": [],
        },
        {
            "name": "Case 3: All Zeros (Duplicate Elimination)",
            "nums": [0, 0, 0, 0],
            "expected": [[0, 0, 0]],
        },
        {
            "name": "Case 4: Array with Multiple Identical Non-Zero Triplets",
            "nums": [-2, 0, 0, 2, 2],
            "expected": [[0, 2, -2]],
        },
        {
            "name": "Case 5: Minimal Valid Length Array",
            "nums": [-1, -1, 2],
            "expected": [[-1, 2, -1]],
        },
    ]

    print("=" * 70)
    print("Testing 3Sum (Two Pointers)")
    print("=" * 70)

    for case in test_cases:
        actual = solution.threeSum(list(case["nums"]))

        # Sort internal triplets and external list for order-agnostic comparison
        normalized_actual = sorted([sorted(t) for t in actual])
        normalized_expected = sorted([sorted(t) for t in case["expected"]])

        status = "PASS" if normalized_actual == normalized_expected else "FAIL"

        print(f"\n[{case['name']}]")
        print(f"  Input   : {case['nums']}")
        print(f"  Expected: {case['expected']}")
        print(f"  Actual  : {actual} -> {status}")

    print("\n" + "=" * 70)
