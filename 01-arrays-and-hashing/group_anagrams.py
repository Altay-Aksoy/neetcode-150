"""
LeetCode / NeetCode: Group Anagrams
Difficulty: Medium
Link: https://neetcode.io/problems/anagram-groups
"""


# ==============================================================================
# Optimal Solution (Categorize by Sorted String / Hash Map)
# Time Complexity:  O(M * N log N) - M = len(strs), N = max string length
# Space Complexity: O(M * N)
# ==============================================================================
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        str_dict = {}
        for s in strs:
            sorted_s = "".join(sorted(s))

            if sorted_s in str_dict:
                str_dict[sorted_s].append(s)
            else:
                str_dict[sorted_s] = [s]
        return list(str_dict.values())


# ==============================================================================
# Alternative Solution (Iterative Anagram Matching with Helper)
# Time Complexity:  O(M^2 * N)
# Space Complexity: O(M * N)
# ==============================================================================
class AlternativeSolution:
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

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        answer = []
        # Orijinal girdi listesini bozmamak için kopya alıyoruz
        words = list(strs)

        while words != []:
            group = [words[0]]
            words_0 = words[0]
            words.remove(words[0])
            i = 0
            while i < len(words):
                words_i = words[i]
                if self.isAnagram(words_0, words_i):
                    group.append(words_i)
                    words.pop(i)
                    i -= 1
                i += 1
            answer.append(group)
        return answer


# ==============================================================================
# Tests
# ==============================================================================
if __name__ == "__main__":
    solution = Solution()
    alt_solution = AlternativeSolution()

    test_cases = [
        ["act", "pots", "tops", "cat", "stop", "hat"],
        ["x"],
        [""],
    ]

    print("--- Optimal Solution (Sorted String Hash Map) ---")
    for test in test_cases:
        result = solution.groupAnagrams(test)
        print(f"Input: {test}\nOutput: {result}\n")

    print("--- Alternative Solution (Iterative Matching) ---")
    for test in test_cases:
        result = alt_solution.groupAnagrams(test)
        print(f"Input: {test}\nOutput: {result}\n")
