class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        def search(arr, target, FirstIndex):
            start = 0
            end = len(arr) - 1

            ans = -1

            while start <= end:
                mid = start + (end - start) / 2

                if arr[mid] < target:
                    start = mid + 1
                elif arr[mid] > target:
                    end = mid - 1
                else:
                    ans = mid
                    if FirstIndex:
                        end = mid - 1
                    else:
                        start = mid + 1
            return ans

        start = search(nums, target, True)
        end = search(nums, target, False)

        return [start, end]