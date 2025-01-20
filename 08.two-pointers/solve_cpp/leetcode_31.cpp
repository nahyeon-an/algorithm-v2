/*
 * Next Permutation
 */
#include <iostream>
#include <algorithm>

using namespace std;

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        // 1. pivot
        int pivot = nums.size() - 2;

        while (pivot >= 0) {
            if (nums[pivot] < nums[pivot + 1]) 
                break;
            pivot--;
        }

        if (pivot == -1) {
            sort(nums.begin(), nums.end());
        }

        // 2. swap point
        int j = pivot + 1;
        int swap_point = j;
        int min_value = nums[j];

        while (j < nums.size()) {
            if ((nums[pivot] < nums[j]) && (nums[j] < min_value)) {
                swap_point = j;
                min_value = nums[j];
            }
            j += 1;
        }

        cout << pivot << endl;
        cout << swap_point << endl;

        // 3. swap
        if (pivot > -1) {
            int tmp = nums[pivot];
            nums[pivot] = nums[swap_point];
            nums[swap_point] = tmp;
        }

        // 4. pivot+1 ~ asc 
        sort(nums.begin() + pivot + 1, nums.end());
    }

    void printVector(vector<int>& nums) {
        for (int num : nums) {
            cout << num << " ";
        }
        cout << endl;
    }
};

int main() {
    Solution solution;

    vector<int> v = {1,3,2,4};
    cout << "input : ";
    solution.printVector(v);

    solution.nextPermutation(v);
    cout << "solution : ";
    solution.printVector(v);

    return 0;
}