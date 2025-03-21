import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

public class Leetcode37 {
    private final int BOARD_SIZE;
    private final int BOX_SIZE;
    private static final int DEFAULT_BIT = 0b111111111;
    private static final List<Integer> emptyX = new LinkedList<>();
    private static final List<Integer> emptyY = new LinkedList<>();
    private static final int[] rows = new int[9];
    private static final int[] cols = new int[9];
    private static final int[] boxes = new int[9];

    public Leetcode37(int boardSize) {
        this.BOARD_SIZE = boardSize;
        this.BOX_SIZE = boardSize / 3;
    }

    public void solveSudoku(char[][] board) {
        Arrays.fill(rows, DEFAULT_BIT);
        Arrays.fill(cols, DEFAULT_BIT);
        Arrays.fill(boxes, DEFAULT_BIT);

        for (int i = 0; i < BOARD_SIZE; i++) {
            for (int j = 0; j < BOARD_SIZE; j++) {
                if (board[i][j] == '.') {
                    emptyX.add(i);
                    emptyY.add(j);
                } else {
                    int n = board[i][j] - '0';
                    rows[i] &= ~(1 << (n - 1));
                    cols[j] &= ~(1 << (n - 1));
                    boxes[(i / BOX_SIZE) * BOX_SIZE + (j / BOX_SIZE)] &= ~(1 << (n - 1));
                }
            }
        }

        backtracking(board, 0);
        printBoard(board);
    }

    public boolean backtracking(char[][] board, int idx) {
        if (idx == emptyX.size()) {
            return true;
        }

        int x = emptyX.get(idx);
        int y = emptyY.get(idx);

        int candidates = DEFAULT_BIT;
        candidates &= rows[x];
        candidates &= cols[y];
        candidates &= boxes[(x / BOX_SIZE) * BOX_SIZE + y / BOX_SIZE];

        for (int n = 1; n <= BOARD_SIZE; n++) {
            if (((1 << (n - 1)) & candidates) > 0) {
                board[x][y] = (char) ('0' + n);
                rows[x] &= ~(1 << (n - 1));
                cols[y] &= ~(1 << (n - 1));
                boxes[(x / BOX_SIZE) * BOX_SIZE + y / BOX_SIZE] &= ~(1 << (n - 1));

                if (backtracking(board, idx + 1)) {
                    return true;
                }

                board[x][y] = '.';
                rows[x] |= (1 << (n - 1));
                cols[y] |= (1 << (n - 1));
                boxes[(x / BOX_SIZE) * BOX_SIZE + y / BOX_SIZE] |= (1 << (n - 1));
            }
        }

        return false;
    }

    public void printBoard(char[][] board) {
        for (int i = 0; i < board.length; i++) {
            StringBuilder row = new StringBuilder("[");
            for (int j = 0; j < board[0].length; j++) {
                row.append(" " + board[i][j] + " ");
            }
            row.append("]");
            System.out.println(row);
        }
    }

    public static void main(String[] args) {
        Leetcode37 app = new Leetcode37(9);

        char[][] board = {
                {'5', '3', '.', '.', '7', '.', '.', '.', '.'},
                {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
                {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
                {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
                {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
                {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
                {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
                {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
                {'.', '.', '.', '.', '8', '.', '.', '7', '9'}
        };

        app.solveSudoku(board);
    }
}