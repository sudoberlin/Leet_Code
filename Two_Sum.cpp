class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int i;
        int j;
        int k;
        int length;
        vector<int> indices;
        length = nums.size();
        
        for (i = 0; i<length; i++)
        {
            k = target - nums[i];
            
            for (j=i+1; j<length; j++)
            {
                
                if (k == nums[j])
                {
                    indices.push_back(i);
                    indices.push_back(j);
                        break;
                    
                } 
            }
            if (indices.size() == 2)
            {
                break;
            }
        }return indices;
    }
};