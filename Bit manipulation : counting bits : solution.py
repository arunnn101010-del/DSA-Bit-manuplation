# Prombelm - counting bits 
# Approach - bit manipulation 
# Time and space complexity -  0(n) & 0(n) 
# leetcode and diffculty level - 338 & easy 
class Solution {
public:
    vector<int> countBits(int n) {

        vector<int> ans(n + 1, 0);

        for(int i = 1; i <= n; i++) {

            ans[i] = ans[i & (i - 1)] + 1;
        }

        return ans;
    }
};
