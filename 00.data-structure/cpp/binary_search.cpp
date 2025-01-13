#include <iostream>
#include <vector>
#include <algorithm>

int binarySearch(const std::vector<int>& arr, int target) {
    int left = 0;
    int right = arr.size() -1;

    while (left <= right) {
        int mid = (left + right) / 2;

        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return -1;
}

int main() {
    std::vector<int> arr = {1, 3, 5, 6, 7, 11, 15, 18, 22, 25};
    int target;

    std::cout << "Enter the number to search: ";
    std::cin >> target;

    int result = binarySearch(arr, target);

    if (result == -1) {
        std::cout << "Element Not Found" << std::endl;
    } else {
        std::printf("Element found at index %d\n", result);
    }

    return 0;
}