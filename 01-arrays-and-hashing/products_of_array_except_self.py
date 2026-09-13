"""
LeetCode / NeetCode: Products of Array Except Self
Difficulty: Medium
Link: https://neetcode.io/problems/products-of-array-discluding-self
"""


# ==============================================================================
# Optimal Solution (Prefix & Postfix in Output Array)
# Time Complexity:  O(N)
# Space Complexity: O(1) auxiliary space (output array does not count)
# ==============================================================================
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer = []
        length = len(nums)

        # Prefix çarpımlarını doğrudan answer dizisine yazıyoruz
        product = 1
        for i in range(length):
            answer.append(product)
            product *= nums[i]

        # Postfix çarpımlarını sondan başa answer elemanlarıyla çarpıyoruz
        product = 1
        for i in range(length):
            answer[-i - 1] *= product
            product *= nums[-i - 1]

        return answer


# ==============================================================================
# Alternative Solution 1 (Explicit Prefix & Postfix Arrays)
# Time Complexity:  O(N)
# Space Complexity: O(N)
# ==============================================================================
class PrefixPostfixSolution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefixes = []
        postfixes = []
        length = len(nums)

        product = 1
        for i in range(length):
            prefixes.append(product)
            product *= nums[i]

        product = 1
        for i in range(length):
            postfixes.append(product)
            product *= nums[-i - 1]
        postfixes.reverse()

        return [postfixes[i] * prefixes[i] for i in range(length)]


# ==============================================================================
# Alternative Solution 2 (Division with Zero-Handling)
# Time Complexity:  O(N)
# Space Complexity: O(1) auxiliary space
# Note: Division is typically restricted in interview constraints, but serves
#       as an intuitive baseline.
# ==============================================================================
class DivisionSolution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # Orijinal girdiyi bozmamak için kopyasını kullanıyoruz
        arr = list(nums)
        product = 1
        zero_num = arr.count(0)

        if zero_num > 1:
            return [0] * len(arr)

        elif zero_num == 1:
            index_of_zero = arr.index(0)
            arr.remove(0)
            for n in arr:
                product *= n
            answer = [0] * len(arr)
            answer.insert(index_of_zero, product)
            return answer

        for n in arr:
            product *= n

        answer = []
        for n in arr:
            answer.append(product // n)
        return answer


# ==============================================================================
# Tests
# ==============================================================================
if __name__ == "__main__":
    solution = Solution()
    prefix_solution = PrefixPostfixSolution()
    div_solution = DivisionSolution()

    test_cases = [
        [1, 2, 4, 6],
        [-1, 0, 1, 2, 3],
        [0, 4, 0],
    ]

    print("--- Optimal Solution (O(1) Auxiliary Space) ---")
    for nums in test_cases:
        print(f"nums={nums} -> {solution.productExceptSelf(list(nums))}")

    print("\n--- Alternative Solution 1 (Prefix & Postfix Arrays) ---")
    for nums in test_cases:
        print(f"nums={nums} -> {prefix_solution.productExceptSelf(list(nums))}")

    print("\n--- Alternative Solution 2 (Division Baseline) ---")
    for nums in test_cases:
        print(f"nums={nums} -> {div_solution.productExceptSelf(list(nums))}")
