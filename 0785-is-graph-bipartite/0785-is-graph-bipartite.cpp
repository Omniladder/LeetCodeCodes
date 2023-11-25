class Solution {
public:
    bool isBipartite(vector<vector<int>>& graph) {
        unsigned char color[graph.size()];
        for(int i =0; i<graph.size(); i++)
        {
            color[i] = 0;
        }
        for(int i = 0; i < graph.size(); i++)
        {
            if(color[i] == 0)
            {
                
                if(!search(graph, color, i,1))
                {
                    return false;
                }
            }
        }
        return true;
    }

    bool search(vector<vector<int>>& graph, unsigned char color[], int index, int setColor)
    {
        color[index] = setColor;
        for(int i = 0 ; i < graph[index].size(); i++)
        {
            if(color[graph[index][i]] == 0)
            {
                if(!search(graph, color, graph[index][i], ((setColor%2)+1)))
                {
                    
                    return false;
                }
            }
            else
            {
                if(color[graph[index][i]] == color[index])
                {
                    return false;
                }
            }
        }
        return true;

    }
};