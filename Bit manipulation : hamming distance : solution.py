# Promblem - hamming distance 
# Approach - bit manipulation
# Time and space complexity - 0(n) & 0(n) 
# Leetcode and diffcu;ty level - 461 & easy 
class Solution {
public:
    int hammingDistance(int x, int y) {

        int n = x ^ y;

        int count = 0;

        while(n != 0) {

            n = n & (n - 1);

            count++;
        }

        return count;
    }
};
