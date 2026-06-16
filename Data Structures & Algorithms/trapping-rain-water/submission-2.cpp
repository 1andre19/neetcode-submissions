class Solution {
public:
    int trap(vector<int>& height) {
        int max_height = 0;
        std::vector<int>max_left(height.size());
        for (int i = 0; i < height.size(); i++) {
            max_left[i] = max_height;
            max_height = max(max_height, height[i]);
        }

        max_height = 0;
        std::vector<int>max_right(height.size());
        for (int i = height.size() - 1; i >= 0; i--) {
            max_right[i] = max_height;
            max_height = max(max_height, height[i]);
        }

        int res = 0;
        int water;
        for (int i = 0; i < height.size(); i++) {
            water = min(max_right[i], max_left[i]) - height[i];
            if (water < 0){
                continue;
            }
            res += water;
        }

        return res;
    }
};
