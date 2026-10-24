class Solution {
    public int missingNumber(int[] nums) {
        Arrays.sort(nums);
        int s = 0;
        while(s<nums.length){
            if (nums[s] != s){
                return s;
            }
            s +=1;
        }
        return s;
        
    }
}