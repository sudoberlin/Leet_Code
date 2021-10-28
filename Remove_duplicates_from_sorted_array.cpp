/*
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
*/

// Time complexity = O(n)
// Space complexity = O(1)

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        // check the length of the given array 
        int len = nums.size();
        
        // check if the array is null.
        if (len ==0){
            return 0;
        }
        
        // make another pointer to comapare and insert. 
        int insert_index = 1;
        for (int i=1; i<len; i++){
            if (nums[i] != nums[i-1]){
                nums[insert_index] = nums[i];
                insert_index++;
            }
        }
        return insert_index;
    }
};