import java.util.*;

public class Leetcode133 {
    public static class Node {
        public int val;
        public List<Node> neighbors;
        public Node() {
            val = 0;
            neighbors = new ArrayList<Node>();
        }
        public Node(int _val) {
            val = _val;
            neighbors = new ArrayList<Node>();
        }
        public Node(int _val, ArrayList<Node> _neighbors) {
            val = _val;
            neighbors = _neighbors;
        }
        public String toString() {
            StringBuilder sb = new StringBuilder();
            sb.append("Node([").append(val).append("] -> [");
            for (int i = 0; i < neighbors.size(); i++) {
                sb.append(neighbors.get(i).val);
                if (i < neighbors.size() - 1) {
                    sb.append(", ");
                }
            }
            sb.append("])");
            return sb.toString();
        }
    }

    public Node cloneGraph(Node node) {
        if (node == null) {
            return null;
        }

        Map<Integer, Node> nodeMap = new HashMap<>();
        Set<Integer> visited = new HashSet<>();
        Queue<Node> queue = new LinkedList<>();
        queue.add(node);

        while (!queue.isEmpty()) {
            Node cur = queue.poll();
            if (visited.contains(cur.val)) {
                continue;
            }
            visited.add(cur.val);

            if (!nodeMap.containsKey(cur.val)) {
                nodeMap.put(cur.val, new Node(cur.val));
            }

            Node copiedNode = nodeMap.get(cur.val);

            for(Node near : cur.neighbors) {
                if (!nodeMap.containsKey(near.val)) {
                    nodeMap.put(near.val, new Node(near.val));
                }
                Node copiedNear = nodeMap.get(near.val);
                copiedNode.neighbors.add(copiedNear);

                // 방문하지 않은 노드 추가
                queue.add(near);
            }
        }

        return nodeMap.values().iterator().next();
    }

    public static void main(String[] args) {
        /**
         * 노드의 val == index (1부터 시작)
         * test case 에서는 인접 리스트로 주어짐
         * deepcopy 한 결과를 리턴
         *
         * adjList = [[2,4],[1,3],[2,4],[1,3]]
         * - 1 번 노드의 이웃은 2, 4
         * - 2 번 노드의 이웃은 1, 3
         * - 3 번 노드의 이웃은 2, 4
         * - 4 번 노드의 이웃은 1, 3
         */
        Leetcode133 app = new Leetcode133();

        Node n1 = new Node(1);
        Node n2 = new Node(2);
        Node n3 = new Node(3);
        Node n4 = new Node(4);

        n1.neighbors = new ArrayList<>(Arrays.asList(n2, n4));
        n2.neighbors = new ArrayList<>(Arrays.asList(n1, n3));
        n3.neighbors = new ArrayList<>(Arrays.asList(n2, n4));
        n4.neighbors = new ArrayList<>(Arrays.asList(n1, n3));

        System.out.println(app.cloneGraph(n1));
    }
}
