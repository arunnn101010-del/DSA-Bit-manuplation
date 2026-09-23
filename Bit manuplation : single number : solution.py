# Promblem - single number
# Approach - bit manuplation 
# Time and space complexity - 0(n) & 0(n) 
# Leetcode and diffculty level - 136 & easy 
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ans = 0;

        for(int i = 0; i < nums.size(); i++) {
            ans ^= nums[i];
        }
        return ans;
    }
};
