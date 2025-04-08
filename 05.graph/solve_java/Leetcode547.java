import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Set;

public class Leetcode547 {
    public int getParent(int[] parent, int x) {
        if (parent[x] != x) {
            parent[x] = getParent(parent, parent[x]);
        }
        return parent[x];
    }

    public void union(int[] parent, int x, int y) {
        int parentX = getParent(parent, x);
        int parentY = getParent(parent, y);

        if (parentX > parentY) {
            parent[x] = parentY;
        } else {
            parent[y] = parentX;
        }
    }

    public int find(int[] parent, int x, int y) {
        int parentX = getParent(parent, x);
        int parentY = getParent(parent, y);
        if (parentX == parentY) return 1;
        else return 0;
    }

    public int findCircleNum(int[][] isConnected) {
        int n = isConnected.length; // 노드 개수
        Queue<Integer> queue = new LinkedList<>();
        boolean[] visited = new boolean[n];
        int[] parent = new int[n];

        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }

        for (int i = 0; i < n; i++) {
            if (visited[i]) continue;
            queue.add(i);

            while(!queue.isEmpty()) {
                int cur = queue.poll();
                if (visited[cur]) {
                    continue;
                }
                visited[cur] = true;
                System.out.println("visit " + cur);

                for (int j = 0; j < n; j++) {
                    if (isConnected[cur][j] == 1) {
                        union(parent, cur, j);
                        queue.add(j);
                    }
                }
            }
        }

        // counting
        Set<Integer> groups = new HashSet<>();
        for (int i = 0; i < n; i++) {
            groups.add(getParent(parent, i));
        }

        // parent 출력
        for(int i = 0; i < n; i++) {
            System.out.println(String.format("Node(%d) - Parent(%d)", i, parent[i]));
        }

        return groups.size();
    }

    public static void main(String[] args) {
        /**
         * province : 연결된 노드의 그룹 -> 같은 부모를 가지는지 찾으면 됨
         * n * n matrix 가 주어짐
         * isConnected[i][j] = 1 이면 i -> j 연결됨
         * isConnected[i][j] = 0 이면 연결되지 않음
         */
        Leetcode547 app = new Leetcode547();

        int[][] matrix = new int[][] {
                {1, 1, 0},
                {1, 1, 0},
                {0, 0, 1}
        };
//        int[][] matrix = new int[][] {
//                {1,0,0,1},
//                {0,1,1,0},
//                {0,1,1,1},
//                {1,0,1,1}
//        };
        System.out.println(app.findCircleNum(matrix));
    }
}
