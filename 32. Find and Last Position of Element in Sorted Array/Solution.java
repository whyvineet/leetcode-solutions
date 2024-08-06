class Solution {
    public int[] searchRange(int[] nums, int target) {
        int start = search(nums, target, true);
        int end = search(nums, target, false);

        return new int[] {start, end};
    }

    int search(int[] arr, int target, boolean FirstIndex) {
        int start = 0;
…    return ans;
    }
}