#include <string.h>

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int numofprefix = 0;
        if(strs.size()>1)
        {
        while(true)
        {
            numofprefix++;
            for(int i = 1; i < strs.size(); i++)
            {
                if(strs[i].length() < numofprefix)
                {return strs[i];}
                if(strs[i].substr(0,numofprefix) != strs[0].substr(0,numofprefix))
                {return strs[0].substr(0,numofprefix-1);}
                
            }
        }
        }
        else
        {
            return strs[0];
        }
    }
};