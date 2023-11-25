class Solution {
public:
    vector<int> findSmallestSetOfVertices(int n, vector<vector<int>>& edges) {
        vector<int> found;
        bool isAnswer[n];

        for(int i = 0; i < n; i++)
        {isAnswer[i] = true;}

        for(int i = 0; i < edges.size(); i++)
        {isAnswer[edges[i][1]] = false;}

        for(int i = 0 ; i < n; i++)
        {if(isAnswer[i])
            {found.push_back(i);}}
            
        return found;
    }
};