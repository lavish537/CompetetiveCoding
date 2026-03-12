class Solution {
public:
    int numSubarrayBoundedMax(vector<int>& nums, int left, int right) {
        int count = 0;
        int leftValid = -1;
        int rightInvalid = -1;

        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] >= left) {
                leftValid = i;
            }
            if (nums[i] > right) {
                rightInvalid = i;
            }
            count += max(0, leftValid - rightInvalid);
        }
        return count;
    }
};