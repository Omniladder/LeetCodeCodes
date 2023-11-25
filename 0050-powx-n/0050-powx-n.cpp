class Solution {
    public:
    double myPow(double x, int n) {
        
        double answer = x;
        long int Current_Power = 1;
        long int Temp_Power, Temp_answer ;
        if(n == 0)
        {return 1;}
        if(n > 0)
        {
            while(Current_Power*2 <= n)
            {
                answer*=answer;
                Current_Power*=2;
            }
            if(n == 1)
            {return answer;}

            
            
            answer *= myPow(x, n - Current_Power);
            
            return answer;
        }
        if(n < 0)
        {
            answer = 1/answer;
            long int Current_Power = -1;
            while(Current_Power*2 >= n)
            {
                answer *= answer;
                Current_Power*=2;
            }
            answer *= myPow(x, n - Current_Power);
            
        }
        return answer;

        
    }
};