import java.util.Arrays;


public class Leetcode654 {
    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode() {
        }

        TreeNode(int val) {
            this.val = val;
        }

        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }

        public String toString() {
            return String.format("TreeNode(val=%d, left=%s, right=%s)", val, left, right);
        }
    }

    public TreeNode constructMaximumBinaryTree(int[] nums) {
        /**
         * 1. 최대값을 root 로 생성
         * 2. 최대값을 기준으로 왼쪽 nums 로 left sub tree 를 똑같이 만듦
         * 3. 최대값을 기준으로 오른쪽 nums 로 right sub tree 를 만듦
         */
        if (nums.length == 0) {
            return null;
        }

        // nums 에서 최대값 찾기
        int maxValue = -1;
        int maxIdx = -1;
        for (int i = 0; i < nums.length; i++) {
           if (maxValue < nums[i]) {
               maxValue = nums[i];
               maxIdx = i;
           }
        }

        TreeNode root = new TreeNode(maxValue);

        System.out.println("Max Value : " + maxValue);
        System.out.println("nums : " + Arrays.toString(nums));

        int[] leftNums = new int[maxIdx];
        for (int i = 0; i < maxIdx; i++) {
            leftNums[i] = nums[i];
        }
        root.left = constructMaximumBinaryTree(leftNums);

        int[] rightNums = new int[nums.length - maxIdx - 1];
        for (int i = maxIdx + 1; i < nums.length; i++) {
            rightNums[i - maxIdx - 1] = nums[i];
        }
        root.right = constructMaximumBinaryTree(rightNums);

        return root;
    }

    public static void main(String[] args) {
        Leetcode654 app = new Leetcode654();

        int[] nums = {3,2,1,6,0,5};
        System.out.println(app.constructMaximumBinaryTree(nums));
    }
}
