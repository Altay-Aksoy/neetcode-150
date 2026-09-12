"""
LeetCode / NeetCode: Encode and Decode Strings
Difficulty: Medium
Link: https://neetcode.io/problems/string-encode-and-decode
"""


# ==============================================================================
# Optimal Solution (Length-Prefix Encoding)
# Time Complexity:  O(N) for both encode and decode (N = total character count)
# Space Complexity: O(N)
# ==============================================================================
class Solution:
    def encode(self, strs: list[str]) -> str:
        answer = ""
        for s in strs:
            answer = answer + str(len(s)) + " " + s
        return answer

    def decode(self, s: str | None) -> list[str]:
        if not s:
            return []

        answer = []
        while s != "":
            word = ""
            first_num = ""
            for i in s:
                if i == " ":
                    break

            first_num += s[: s.index(i)]
            s = s.removeprefix(first_num + " ")

            for l in range(int(first_num)):
                word += s[l]

            s = s.removeprefix(word)
            answer.append(word)

        return answer


# ==============================================================================
# Tests
# ==============================================================================
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ["neet", "code", "love", "you"],
        ["we", "say", ":", "yes"],
        [""],
        ["hello world", " ", "4#test"],
    ]

    for words in test_cases:
        encoded = solution.encode(words)
        decoded = solution.decode(encoded)
        print(f"Original: {words}")
        print(f"Encoded : {repr(encoded)}")
        print(f"Decoded : {decoded}")
        print(f"Match   : {words == decoded}\n")
