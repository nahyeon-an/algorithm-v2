#include <iostream>

using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int pivot = findMinimumIndex(nums);

        if (pivot == 0) 
            return binarySearch(nums, target, 0, nums.size() - 1);

        if (target >= nums[0])
            return binarySearch(nums, target, 0, pivot - 1);
        else {
            return binarySearch(nums, target, pivot, nums.size() - 1);
        }
    }

    int findMinimumIndex(vector<int>& nums) {
        int left = 0;
        int right = nums.size() - 1;

        while (left < right) {
            if (nums[left] < nums[right]) 
                break;

            int mid = (left + right) / 2;

            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } 
            else {
                right = mid;
            }
        }

        return left;
    }

    // arr 에서 조회 범위를 인자로 전달 받아서 추가 메모리 할당을 없앨 수 있음
    int binarySearch(vector<int>& nums, int target, int start, int end) {
        int left = start;
        int right = end;

        while (left <= right) {
            int mid = (left + right) / 2;

            if (nums[mid] == target) 
                return mid;
            else if (nums[mid] > target) 
                right = mid - 1;
            else 
                left = mid + 1;
        }

        return -1;
    }
};

int main() {
    Solution solution;

    vector<int> case1 = {4, 5, 6, 7, 0, 1, 2};
    cout << "input : {4, 5, 6, 7, 0, 1, 2}, target : 0 => answer : " << solution.search(case1, 0) << endl;
    cout << "input : {4, 5, 6, 7, 0, 1, 2}, target : 4 => answer : " << solution.search(case1, 4) << endl;
    cout << "input : {4, 5, 6, 7, 0, 1, 2}, target : 3 => answer : " << solution.search(case1, 3) << endl;

    vector<int> case2 = {1};
    cout << "input : {1}, target : 0 => answer : " << solution.search(case2, 0) << endl;
    cout << "input : {1}, target : 1 => answer : " << solution.search(case2, 1) << endl;

    vector<int> case3 = {1, 3};
    cout << "input : {1, 3}, target : 1 => answer : " << solution.search(case3, 1) << endl;

    return 0;
}