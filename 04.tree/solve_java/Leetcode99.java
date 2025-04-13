import java.util.Stack;

public class Leetcode99 {
    public TreeNode prev, firstMismatched, secondMismatched;

    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }

        public String toString() {
            StringBuilder sb = new StringBuilder();
            sb.append("Node(" + val + ", left=");
            if (left != null) {
                sb.append(left.toString());
            } else {
                sb.append("null");
            }
            sb.append(", right=");
            if (right != null) {
                sb.append(right.toString());
            } else {
                sb.append("null");
            }
            sb.append(")");
            return sb.toString();
        }
    }

    public void inOrderTree(TreeNode node) {
        if (node == null) {
            return;
        }

        inOrderTree(node.left);
        if (prev != null && prev.val > node.val) {
            if (firstMismatched == null) {
                firstMismatched = prev;
            }
            secondMismatched = node;
        }
        prev = node;
        inOrderTree(node.right);
    }

    public void bruteForce(TreeNode root) {
        boolean isChanged = false;
        Stack<TreeNode> stack = new Stack<>();

        // left
        stack.add(root.left);
        while (!stack.isEmpty()) {
            TreeNode node = stack.pop();
            if (node == null) {
                continue;
            }

            if (node.val > root.val) { // change value
                int tmp = node.val;
                node.val = root.val;
                root.val = tmp;
                isChanged = true;
            }
            stack.add(node.left);
            stack.add(node.right);
        }

        // right
        stack.add(root.right);
        while (!stack.isEmpty()) {
            TreeNode node = stack.pop();
            if (node == null) {
                continue;
            }

            if (node.val < root.val) { // change value
                int tmp = node.val;
                node.val = root.val;
                root.val = tmp;
                isChanged = true;
            }
            stack.add(node.left);
            stack.add(node.right);
        }

        if (isChanged) {
            recoverTree(root);
        }
        if (root.left != null) {
            recoverTree(root.left);
        }
        if (root.right != null) {
            recoverTree(root.right);
        }
    }

    public void recoverTree(TreeNode root) {
        inOrderTree(root);
        // swap two mis-matched nodes
        int temp = firstMismatched.val;
        firstMismatched.val = secondMismatched.val;
        secondMismatched.val = temp;
    }

    public static void main(String[] args) {
        /**
         * Binary Search Tree 의 root 가 주어짐
         * 이 tree 에서 정확히 2개의 노드만 잘못 삽입되어 있음
         * 구조 변경없이 이를 복구하라.
         */
        Leetcode99 app = new Leetcode99();

        TreeNode root = new TreeNode(1, new TreeNode(3, null, new TreeNode(2)), null);
        app.recoverTree(root);
        System.out.println(root);

        TreeNode root2 = new TreeNode(3, new TreeNode(1, null, null), new TreeNode(4, new TreeNode(2), null));
        app.recoverTree(root2);
        System.out.println(root2);

        TreeNode root3 = new TreeNode(2, new TreeNode(3, null, null), new TreeNode(1, null, null));
        app.recoverTree(root3);
        System.out.println(root3);
    }
}
