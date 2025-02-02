#include<iostream>
#include<fstream>

using namespace std;

class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> chosen;
        vector<vector<int>> answer;
        recursive(candidates, target, chosen, answer);
        return answer;
    }

    vector<int> recursive(vector<int>& candidates, int target, vector<int>& chosen, vector<vector<int>>& results) {
        if (target == 0)
            return chosen;

        for (int i = 0; i < candidates.size(); i++) {
            if (candidates[i] > target)
                continue;

            if (!chosen.empty() && chosen.back() > candidates[i]) 
                continue;

            vector<int> selected = chosen;
            selected.push_back(candidates[i]);
            
            vector<int> result = recursive(candidates, target - candidates[i], selected, results);
            if (!result.empty()) {
                results.push_back(result);
            }
        }

        return {};
    }
};

int main() {
    Solution solution;

    // read test cases
    ifstream inputFile("../inputs/leetcode_39.txt");
    if (!inputFile) {
        cerr << "can't open a file" << endl;
        return 1;
    }

    int testcase;
    inputFile >> testcase;

    while (testcase-- > 0) {
        vector<int> candidates;
        int num;

        while (inputFile >> num) {
            candidates.push_back(num);

            if (inputFile.peek() == '\n') 
                break;
        }

        int target;
        inputFile >> target;

        vector<vector<int>> output = solution.combinationSum(candidates, target);

        cout << "solution #" << testcase << endl;
        for (int i = 0; i < output.size(); i++) {

            cout << "[ ";

            for (int j = 0; j < output[i].size(); j++) {
                cout << output[i][j] << " ";
            }

            cout << "]" << endl;
        }
        cout << endl;
    }

    inputFile.close();

    return 0;
}