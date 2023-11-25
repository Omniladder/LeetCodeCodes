class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        return permute(nums, nums.size());
    }

    vector<vector<int>> permute(vector<int> avai, int add){
        vector<vector<int>> finish, temp;
        if(avai.size() == 1)
        {
            vector<int> IDK;
            IDK.push_back(avai[0]);
            finish.push_back(IDK);
        }
        else
        {
            int push = 0;
            bool triggered = false;
            if(add < avai.size())
            {
                push = avai[add];
                avai.erase(avai.begin() + add);
                triggered = true;
            }

            for(int i = 0; i < avai.size(); i++)
            {
                temp = permute(avai, i);

                for(int j = 0; j < temp.size(); j++)
                {
                    if(triggered)
                    {
                        temp[j].push_back(push);
                    }
                    
                    finish.push_back(temp[j]);
                }
            }
        }
        return finish;
    }
};