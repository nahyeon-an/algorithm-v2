/*
 * 내가 푼 방식 : O(n). zero padding 이 걸림
 * 개선 포인트 : 각 string 별로 pointer 를 부여
 */
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    string addBinary(string a, string b) {
        int a_index = a.size() - 1;
        int b_index = b.size() - 1;
        int c = 0;

        string ans;

        // 마지막 올림수(c=1)가 존재할 때, ans 에 추가하기 위해 c>0 조건 필요함
        while (a_index >= 0 || b_index >= 0 || c > 0) {
            if (a_index >= 0) 
                // 문자 0의 ASCII 코드 값을 빼서 int 형으로 변환할 수 있다
                c += a[a_index--] - '0';
            if (b_index >= 0) 
                c += b[b_index--] - '0';

            ans += c % 2 + '0';
            c /= 2;
        }

        reverse(ans.begin(), ans.end());

        return ans;
    }
};

int main() {
    Solution solution;

    cout << "1010 + 1111 = " << solution.addBinary("1010", "1111") << endl;
    cout << "1010 + 1 = " << solution.addBinary("1010", "1") << endl;
    cout << "1010 + 11110000000 = " << solution.addBinary("1010", "11110000000") << endl;

    return 0;
}