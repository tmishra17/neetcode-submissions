class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> sum = new HashMap<>();
        // go through array and see if the difference of target - nums[i]
        // is in sum
        // if its in sum, then return an array with sum.get(diff) and i
        // that means the diff/comp is in the array, this is also much
        // more efficient
        for(int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];
            if (sum.containsKey(diff)) {
                return new int[] {sum.get(diff), i};
            }
            else {
                sum.put(nums[i], i);
            }
        }
    return new int[]{0, 0};
    // TC O(n)
    // SC O(n)
    }
}
