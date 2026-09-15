"""
LeetCode / NeetCode: Valid Sudoku
Difficulty: Medium
Link: https://neetcode.io/problems/valid-sudoku

Description:
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be
validated according to the following rules:
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9
   without repetition.

Note:
- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.
"""

from collections import Counter, defaultdict


# ==============================================================================
# Optimal Solution (One-Pass Hash Sets with Block Coordinate Mapping)
# Time Complexity:  O(1) - Board size is fixed at 9x9 (81 cell iterations)
# Space Complexity: O(1) - Sets store at most 81 characters combined
# ==============================================================================
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        def_dict = defaultdict(set)
        for i in range(9):
            line_container = set()
            column_container = set()
            for j in range(9):

                element = board[j][i]
                if element in column_container and element != ".":
                    return False
                else:
                    column_container.add(element)

                element = board[i][j]

                if element == ".":
                    continue

                if element in line_container:
                    return False
                else:
                    line_container.add(element)

                if element in def_dict[(i // 3, j // 3)]:
                    return False
                else:
                    def_dict[(i // 3, j // 3)].add(element)

        return True


# ==============================================================================
# Alternative Solution (Modular Checking with Counter)
# Time Complexity:  O(1) - Fixed 9x9 iterations across lines, columns, subgrids
# Space Complexity: O(1) - Auxiliary lists and frequency counters capped at 9
# ==============================================================================
class AlternativeSolution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Line Checking
        for i in board:
            if self.checkList(i) != None:
                return False

        # Column Checking
        for i in range(9):
            columns = []
            for element in board:
                columns.append(element[i])

            if self.checkList(columns) != None:
                return False

        for k in range(3):
            for l in range(3):
                if self.check3x3(board, k, l) != None:
                    return False
        return True

    def checkList(self, isContainSame):
        counter_dict = Counter(isContainSame)
        counter_dict["."] = 1
        for v in counter_dict.values():
            if v > 1:
                return False

    def check3x3(self, willCheckList, i_range, j_range):
        # 3x3 Checking
        check = []
        for i in range(3 * i_range, 3 * i_range + 3):
            for j in range(3 * j_range, 3 * j_range + 3):
                check.append(willCheckList[i][j])
        if self.checkList(check) != None:
            return False


# ==============================================================================
# Driver & Edge-Case Tests
# ==============================================================================
if __name__ == "__main__":
    solution = Solution()
    alt_solution = AlternativeSolution()

    test_cases = [
        {
            "name": "Case 1: Standard Valid Partially-Filled Board",
            "board": [
                ["1", "2", ".", ".", "3", ".", ".", ".", "."],
                ["4", ".", ".", "5", ".", ".", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", ".", "3"],
                ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
                [".", ".", ".", "8", ".", "3", ".", ".", "5"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", ".", ".", ".", ".", ".", "2", ".", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "8"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ],
            "expected": True,
        },
        {
            "name": "Case 2: Invalid Row (Duplicate '8' in Row 0)",
            "board": [
                ["8", "3", ".", ".", "7", ".", ".", ".", "8"],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ],
            "expected": False,
        },
        {
            "name": "Case 3: Invalid 3x3 Subgrid (Duplicate '3' in Top-Left Box)",
            "board": [
                [".", ".", "3", ".", ".", ".", ".", ".", "."],
                ["3", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", "."],
            ],
            "expected": False,
        },
        {
            "name": "Case 4: Empty Board (All dots)",
            "board": [["."] * 9 for _ in range(9)],
            "expected": True,
        },
    ]

    print("=" * 70)
    print("Testing Valid Sudoku Implementations")
    print("=" * 70)

    for case in test_cases:
        actual_opt = solution.isValidSudoku(case["board"])
        actual_alt = alt_solution.isValidSudoku(case["board"])

        status_opt = "PASS" if actual_opt == case["expected"] else "FAIL"
        status_alt = "PASS" if actual_alt == case["expected"] else "FAIL"

        print(f"\n[{case['name']}]")
        print(f"  Expected Result     : {case['expected']}")
        print(f"  Optimal (One-Pass)  : {actual_opt} -> {status_opt}")
        print(f"  Alternative (Modular): {actual_alt} -> {status_alt}")

    print("\n" + "=" * 70)
