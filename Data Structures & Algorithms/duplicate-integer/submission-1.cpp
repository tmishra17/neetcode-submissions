class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        int count = 1;
        for(int i = 0; i < nums.size(); i++) {
            for(int j = i + 1; j < nums.size(); j++) {
                if (nums[i] == nums[j]) {
                    count++;
                    return true;
                }
            }
        }
        return false;

    }
};
