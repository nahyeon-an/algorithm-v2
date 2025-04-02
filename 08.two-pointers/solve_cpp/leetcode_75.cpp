#include<iostream>

using namespace std;

class Solution {
public:
    void sortColors(vector<int>& nums) {
        int left = 0;
        int right = nums.size() - 1;
        int idx = 0;

        while (idx <= right) {
            if (nums[idx] == 0) {
                // left <-> idx
                swap(nums[left++], nums[idx++]);
            } else if (nums[idx] == 2) {
                // right <-> idx
                swap(nums[right--], nums[idx]);
            } else {
                idx++;
            }
        }
    }
};

int main() {
    Solution solution;

    vector<int> nums = {2,0,2,1,1,0};
    // vector<int> nums = {1,2,0};
    solution.sortColors(nums);

    cout << "sorted : ";
    for (int i = 0; i < nums.size(); i++) {
        cout << nums[i] << " ";
    }
    cout << endl;
}