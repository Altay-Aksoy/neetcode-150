"""
LeetCode / NeetCode: Valid Anagram
Difficulty: Easy
Link: https://neetcode.io/problems/is-anagram
"""


# ==============================================================================
# Optimal Solution (Hash Map / Frequency Counter)
# Time Complexity:  O(N)
# Space Complexity: O(1)
# ==============================================================================
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}

        for letter in s:
            s_dict[letter] = s_dict.get(letter, 0) + 1

        for letter in t:
            t_dict[letter] = t_dict.get(letter, 0) + 1

        return s_dict == t_dict


# ==============================================================================
# Alternative Solution (Sorting)
# Time Complexity:  O(N log N)
# Space Complexity: O(N)
# ==============================================================================
class AlternativeSolution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        else:
            return False


# ==============================================================================
# Driver & Tests
# ==============================================================================
if __name__ == "__main__":
    solution = Solution()
    alt_solution = AlternativeSolution()

    test_cases = [
        ("racecar", "carrace", True),
        ("jar", "jam", False),
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("a", "ab", False),
    ]

    print("--- Optimal Solution (Hash Map) ---")
    for s, t, expected in test_cases:
        result = solution.isAnagram(s, t)
        print(f"s='{s}', t='{t}' -> {result} (Expected: {expected})")

    print("\n--- Alternative Solution (Sorting) ---")
    for s, t, expected in test_cases:
        result = alt_solution.isAnagram(s, t)
        print(f"s='{s}', t='{t}' -> {result} (Expected: {expected})")
