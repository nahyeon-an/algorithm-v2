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
