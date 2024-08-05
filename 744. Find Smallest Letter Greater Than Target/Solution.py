class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start = 0
        end = len(letters) - 1

        if letters[end] <= target:
            return letters[start]

        while start <= end:
            mid = start + (end - start) // 2
            if letters[mid] <= target:
                start = mid + 1
            else:
                end = mid - 1
        return letters[start]