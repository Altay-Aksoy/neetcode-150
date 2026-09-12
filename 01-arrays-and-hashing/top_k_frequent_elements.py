"""
LeetCode / NeetCode: Top K Frequent Elements
Difficulty: Medium
Link: https://neetcode.io/problems/top-k-elements-in-list
"""

from collections import Counter, defaultdict


# ==============================================================================
# Approach 1: Frequency Map with Counter (most_common)
# Time Complexity:  O(N log K)
# Space Complexity: O(N)
# ==============================================================================
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counting_dict = Counter(nums)
        answer = []
        for v in counting_dict.most_common(k):
            answer.append(v[0])
        return answer


# ==============================================================================
# Approach 2: DefaultDict with Iterative Max Extraction
# Time Complexity:  O(K * M) where M is unique elements
# Space Complexity: O(M)
# ==============================================================================
class AlternativeSolution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        answerer = defaultdict(int)
        for n in nums:
            answerer[n] += 1

        answer = []
        for i in range(k):
            m = max(answerer.values())
            n = list(answerer.values()).index(m)
            nth = list(answerer.keys())[n]
            answer.append(nth)
            answerer.pop(nth)
        return answer


# ==============================================================================
# Tests
# ==============================================================================
if __name__ == "__main__":
    solution = Solution()
    alt_solution = AlternativeSolution()

    test_cases = [
        ([1, 2, 2, 3, 3, 3], 2, [3, 2]),
        ([7, 7], 1, [7]),
        ([1, 2], 2, [1, 2]),
    ]

    print("--- Approach 1 (Counter.most_common) ---")
    for nums, k, expected in test_cases:
        result = solution.topKFrequent(nums, k)
        print(f"nums={nums}, k={k} -> {result} (Expected: {expected})")

    print("\n--- Approach 2 (DefaultDict Max Extraction) ---")
    for nums, k, expected in test_cases:
        # Alt çözüm orijinal sözlüğü küçülttüğü için her seferinde listeyi temiz gönderiyoruz
        result = alt_solution.topKFrequent(list(nums), k)
        print(f"nums={nums}, k={k} -> {result} (Expected: {expected})")
