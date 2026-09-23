# Promblem - number of 1 bits 
# approach - bit manipulation 
# Time and space complexity - 0(n) & 0(n) 
# Leetcode and  Diffculty level - 191 & easy 
class Solution {
public:
    int hammingWeight(int n) {

        int count = 0;

        while(n != 0) {
            n = n & n-1;
            count++;
        }
        return count++;
    }
};
