
class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> un_vals = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            if (un_vals.contains(nums[i])) {
                return true;
            }
            else {
                un_vals.add(nums[i]);
            }
        }
        return false;
    }
}
