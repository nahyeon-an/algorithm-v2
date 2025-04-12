import java.util.Arrays;
import java.util.Stack;

public class Leetcode32 {
    public static class Pair {
        int idx;
        char c;

        public Pair(int idx, char c) {
            this.idx = idx;
            this.c = c;
        }
    }

    public int improvedSolution(String s) {
        /**
         * 내가 생각하지 못했던 부분 : stack 에 index 를 넣자
         * - ) 가 등장했을 때 max length 계산이 어려웠던 이유가 연결된 케이스 (()) 때문이었음. 그래서 pair 로 idx 까지 정의해버림.
         * - stack 에 저장되는 index 는 substring ( 의 시작점이 아닌 마지막으로 unmatched 인 인덱스를 저장. (내가 한 방식에서는 +1 을 해줘야함)
         */
        int maxLength = 0;
        Stack<Integer> stack = new Stack<>();
        stack.push(-1);

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                stack.push(i);
            } else {
                stack.pop(); // (1) last ( index (2) last unmatched ) index
                if (stack.isEmpty()) {
                    stack.push(i);  // new starting index
                }
                maxLength = Math.max(maxLength, i - stack.peek());
            }
        }

        return maxLength;
    }

    public int longestValidParentheses(String s) {
        boolean[] popArray = new boolean[s.length()];
        Stack<Pair> stack = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                stack.push(new Pair(i, c));
                popArray[i] = false;
            } else {
                if (stack.isEmpty()) continue;

                Pair top = stack.pop();
                if (top.c == '(') {
                    popArray[top.idx] = true;
                    popArray[i] = true;
                } else {
                    popArray[i] = false;
                }
            }
        }

        System.out.println(Arrays.toString(popArray));

        int startIdx = -1;
        int maxLength = 0;
        for (int i = 0; i < popArray.length; i++) {
            if (popArray[i] && startIdx < 0) {
                startIdx = i;
            }
            if (!popArray[i] && startIdx >= 0) {
                maxLength = Math.max(i - startIdx, maxLength);
                startIdx = -1;
            }
        }

        // startIdx >= 0, popArray[-1] = true
        if (startIdx >= 0 && popArray[popArray.length - 1]) {
            maxLength = Math.max(popArray.length - startIdx, maxLength);
        }

        return maxLength;
    }

    public static void main(String[] args) {
        /**
         * ( 와 ) 로 구성된 문자열이 주어짐
         * => 가장 긴 valid 한 괄호 substring 의 길이를 리턴
         * 0 <= s.length <= 3 * 10^4
         */
        Leetcode32 app = new Leetcode32();

        System.out.println(app.longestValidParentheses("(()")); // 2
        System.out.println(app.longestValidParentheses(")()())")); // 4
        System.out.println(app.longestValidParentheses("(())")); // 4
        System.out.println(app.longestValidParentheses(""));
        System.out.println(app.longestValidParentheses("()(()")); // 2
    }
}
