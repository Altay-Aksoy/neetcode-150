"""
LeetCode / NeetCode: Valid Palindrome
Difficulty: Easy
Link: https://neetcode.io/problems/is-palindrome

Description:
A phrase is a palindrome if, after converting all uppercase letters into lowercase
letters and removing all non-alphanumeric characters, it reads the same forward
and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""


# ==============================================================================
# Optimal Solution (In-Place Two Pointers)
# Time Complexity:  O(N) - String is traversed at most once
# Space Complexity: O(1) - No auxiliary string allocations
# ==============================================================================
class Solution:
    def isPalindrome(self, s: str) -> bool:
        len_s = len(s)
        if len_s == 0:
            return True
        start = 0
        end = 1
        while True:
            if len_s <= start + end:
                return True
            starter = s[start].lower()
            ender = s[-end].lower()
            if starter.isalnum():
                if ender.isalnum():
                    if starter == ender:
                        start += 1
                        end += 1
                    else:
                        return False
                else:
                    end += 1
            else:
                start += 1


# ==============================================================================
# Driver & Edge-Case Tests
# ==============================================================================
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        {
            "name": "Case 1: Standard Palindrome with Mixed Punctuation",
            "s": "Was it a car or a cat I saw?",
            "expected": True,
        },
        {
            "name": "Case 2: Standard Non-Palindrome",
            "s": "tab a cat",
            "expected": False,
        },
        {
            "name": "Case 3: Empty String",
            "s": "",
            "expected": True,
        },
        {
            "name": "Case 4: Only Non-Alphanumeric Characters",
            "s": ".,;:!?",
            "expected": True,
        },
        {
            "name": "Case 5: Single Alphanumeric Character with Symbols",
            "s": " #a. ",
            "expected": True,
        },
        {
            "name": "Case 6: Case Insensitivity and Digits",
            "s": "0P0",
            "expected": True,
        },
    ]

    print("=" * 70)
    print("Testing Valid Palindrome (Two Pointers)")
    print("=" * 70)

    for case in test_cases:
        actual = solution.isPalindrome(case["s"])
        status = "PASS" if actual == case["expected"] else "FAIL"
        print(f"\n[{case['name']}]")
        print(f"  Input   : {repr(case['s'])}")
        print(f"  Expected: {case['expected']}")
        print(f"  Actual  : {actual} -> {status}")

    print("\n" + "=" * 70)
