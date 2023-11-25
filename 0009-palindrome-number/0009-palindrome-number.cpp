#include <stack>
#include <cmath>
class Solution {
public:
    bool isPalindrome(int x) {
        string number = to_string(x);
        int length = number.length();
        char* char_array = new char[length + 1];
        bool answer = true;
        strcpy(char_array, number.c_str());
        for(int i = 0; i < length/2; i++)
        {
            if(char_array[i] != char_array[length-i-1] )
            {
                answer = false;
                break;
            }
        }
        return answer;
    }
};