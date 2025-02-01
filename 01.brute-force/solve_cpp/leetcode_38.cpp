#include <iostream>

using namespace std;

class Solution {
public:
    string countAndSay(int n) {
        string target = "1";

        for (int i = 1; i < n; i++) {
            string next = "";
            char prev = target[0];
            int count = 0;

            for (int j = 0; j < target.length(); j++) {
                if (target[j] != prev) {
                    next += to_string(count) + prev;
                    prev = target[j];
                    count = 1;
                } else {
                    count += 1;
                }
            }

            target = next + to_string(count) + prev;
        }

        return target;
    }
};

int main() {
    Solution solution;

    cout << "n = 1, " << solution.countAndSay(1) << endl;
    cout << "n = 2, " << solution.countAndSay(2) << endl;
    cout << "n = 3, " << solution.countAndSay(3) << endl;
    cout << "n = 4, " << solution.countAndSay(4) << endl;
    cout << "n = 5, " << solution.countAndSay(5) << endl;
    cout << "n = 30, " << solution.countAndSay(30) << endl;

    return 0;
}