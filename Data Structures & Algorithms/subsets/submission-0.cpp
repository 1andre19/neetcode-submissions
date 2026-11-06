class Solution {
    vector<vector<int>> res;
    int n;
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<int> curr;
        n = nums.size();
        backtrack(0, curr, nums);
        return res;
    }

    void backtrack(int index, vector<int> curr, vector<int>& nums) {
        res.push_back(curr);

        for (int i = index; i < n; i++) {
            curr.push_back(nums[i]);
            backtrack(i + 1, curr, nums);
            curr.pop_back();
        }
    }
};
