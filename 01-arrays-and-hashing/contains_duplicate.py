"""
LeetCode / NeetCode: Contains Duplicate
Difficulty: Easy
Link: https://neetcode.io/problems/duplicate-integer
"""


# ==============================================================================
# Optimal Solution (Hash Set)
# Time Complexity:  O(N)
# Space Complexity: O(N)
# ==============================================================================
class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        once_set = set()
        for n in nums:
            if n in once_set:
                return True
            else:
                once_set.add(n)
        return False


# ==============================================================================
# Alternative Solution (List Lookup - Suboptimal)
# Time Complexity:  O(N^2) - List lookup takes O(N) inside O(N) loop
# Space Complexity: O(N)
# ==============================================================================
class AlternativeSolution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        once_list = []
        for n in nums:
            if n in once_list:
                return True
            else:
                once_list.append(n)
        return False


# ==============================================================================
# Driver & Tests
# ==============================================================================
if __name__ == "__main__":
    solution = Solution()
    alt_solution = AlternativeSolution()

    test1 = [1, 2, 3, 3]
    test2 = [1, 2, 3, 4]
    test3 = []

    print("--- Optimal Solution (Set) ---")
    print(f"Test 1 ([1, 2, 3, 3]): {solution.hasDuplicate(test1)}")  # True
    print(f"Test 2 ([1, 2, 3, 4]): {solution.hasDuplicate(test2)}")  # False
    print(f"Test 3 ([]):           {solution.hasDuplicate(test3)}")  # False

    print("\n--- Alternative Solution (List) ---")
    print(f"Test 1 ([1, 2, 3, 3]): {alt_solution.hasDuplicate(test1)}")  # True
    print(f"Test 2 ([1, 2, 3, 4]): {alt_solution.hasDuplicate(test2)}")  # False
    print(f"Test 3 ([]):           {alt_solution.hasDuplicate(test3)}")  # False
