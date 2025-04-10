import java.util.*;

public class Leetcode200 {
    public int getParent(int[] parent, int x) {
        if (parent[x] != x) {
            getParent(parent, parent[x]);
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

    public int numIslands(char[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[] parent = new int[m * n];
        boolean[][] visited = new boolean[m][n];

        // initialize every nodes' parents are themselves
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == '1') {
                    parent[r * n + c] = r * n + c;
                    visited[r][c] = false;
                } else {
                    parent[r * n + c] = -1;
                    visited[r][c] = true;
                }
            }
        }

        Queue<int[]> queue = new LinkedList<>();
        // 상하좌우의 1 인 노드들끼리 union
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (visited[r][c]) {
                    continue;
                }
                queue.add(new int[]{r, c});
                // visit adjacent nodes starting from (r, c)
                while (!queue.isEmpty()) {
                    int[] cur = queue.poll();
                    int nX = cur[0];
                    int nY = cur[1];
                    if (visited[nX][nY]) {
                        continue;
                    }
                    visited[nX][nY] = true;
                    System.out.println(String.format("(%d, %d) => %d", nX, nY, nX * n + nY));

                    if (nX - 1 >= 0 && !visited[nX - 1][nY] && grid[nX - 1][nY] == '1') {
                        queue.add(new int[]{nX - 1, nY});
                        union(parent, nX * n + nY, (nX - 1) * n + nY);
                    }
                    if (nX + 1 < m && !visited[nX + 1][nY] && grid[nX + 1][nY] == '1') {
                        queue.add(new int[]{nX + 1, nY});
                        union(parent, nX * n + nY, (nX + 1) * n + nY);
                    }
                    if (nY - 1 >= 0 && !visited[nX][nY - 1] && grid[nX][nY - 1] == '1') {
                        queue.add(new int[]{nX, nY - 1});
                        union(parent, nX * n + nY, nX * n + nY - 1);
                    }
                    if (nY + 1 < n && !visited[nX][nY + 1] && grid[nX][nY + 1] == '1') {
                        queue.add(new int[]{nX, nY + 1});
                        union(parent, nX * n + nY, nX * n + nY + 1);
                    }
                }
            }
        }

        System.out.println(Arrays.toString(parent));

        Set<Integer> groups = new HashSet<>();
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == '1') {
                    groups.add(getParent(parent, r * n + c));
                }
            }
        }

        return groups.size();
    }

    public static void main(String[] args) {
        /**
         * m * n 크기의 grid
         * 1 => island
         * 0 => water
         * island 수를 리턴해라
         * 1 이 연결되어 있으면 섬임
         */
        Leetcode200 app = new Leetcode200();

        char[][] grid = {
                {'1', '1', '1', '1', '0'},
                {'1', '1', '0', '1', '0'},
                {'1', '1', '0', '0', '0'},
                {'0', '0', '0', '0', '0'},
        };
        System.out.println(app.numIslands(grid));
    }
}
