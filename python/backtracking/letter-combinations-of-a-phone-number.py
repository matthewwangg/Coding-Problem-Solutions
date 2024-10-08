class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nums = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"],
                "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        answer = []

        def backtracker(remaining, current):
            if not remaining:
                if current:
                    answer.append(current)
                return

            for i in nums[remaining[0]]:
                backtracker(remaining[1:], current + i)

        backtracker(digits, "")
        return answer