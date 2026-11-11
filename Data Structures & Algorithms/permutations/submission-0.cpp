class Solution {
    vector<bool> used;
    vector<vector<int>> res;
    int n;
public:
    vector<vector<int>> permute(vector<int>& nums) {
        n = nums.size();
        used = vector<bool>(nums.size());
        vector<int> curr;
        dfs(curr, nums);
        return res;
    }

    void dfs(vector<int> curr, vector<int>& nums) {
        if (curr.size() == n) {
            res.push_back(curr);
            return;
        }

        for (int i = 0; i < n; i++) {
            if (used[i]) {
                continue;
            }
            curr.push_back(nums[i]);
            used[i] = true;
            dfs(curr, nums);
            curr.pop_back();
            used[i] = false;
        }
    }
};
