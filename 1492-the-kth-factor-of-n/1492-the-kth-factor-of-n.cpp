class Solution {
public:
    int kthFactor(int n, int k) {
        int j = 0;
        for(int i = 1; i <= n/2; i++)
        {
            if(n % i == 0)
            {
                j++;
            }
            if(j == k)
            {
                return i;
            }
        }
        if(k == j+1)
        {
            return n;
        }
        else
        {
            return -1;
        }
    }
};