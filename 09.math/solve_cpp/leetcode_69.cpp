/**
 * 개선 포인트 ? binary search 
 * sqrt = y * y 입장에서 0 과 x 사이이다. 
 * mid * mid < x -> left = mid
 * mid * mid > x -> right = mid
 * mid * mid == x -> return mid
 */
#include <iostream>

using namespace std;

class Solution {
    public:
        int sqrt(int x) {
            int left = 0;
            int right = x;

            while (left <= right) {
                int mid = (left + right) / 2;
                // long long square = (long long) mid * mid;
                int root = x;
                if (mid > 0) {
                    root /= mid;
                }

                if (mid < root) {
                    left = mid + 1;
                } else if (mid > root) {
                    right = mid - 1;
                } else {
                    return mid;
                }

                /**
                 * 아래 코드가 더 직관적이긴 함. 
                 * mid * mid 로 작성하면 integer overflow 발생 가능함.
                 * long long square = (long long) mid * mid;
                
                    if (square < x) {
                        left = mid + 1;
                    } else if (square > x) {
                        right = mid - 1;
                    } else {
                        return mid;
                    }
                 */
                
            }

            return right;
        }
};

int main() {
    Solution solution;

    for (int i = 0; i <= 30; i++) {
        printf("x = %d : %d\n", i, solution.sqrt(i));
    }

    return 0;
}