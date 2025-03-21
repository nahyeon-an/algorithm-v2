"""
Quite difficult to solve...
I tried it for 5 days
Make it more efficient with Bit masking and Memo
"""

def print_board(board: list[list[str]]):
    for b in board:
        print(b)
    print()


empty_cells: list = None
rows: list = None
cols: list = None
boxes: list = None


def backtracking(board: list[list[str]], visit_idx):
    if visit_idx == len(empty_cells):
        return True

    x, y = empty_cells[visit_idx]

    candidates = 0b111111111
    candidates &= rows[x]
    candidates &= cols[y]
    candidates &= boxes[x // 3 * 3 + y // 3]

    for n in range(1, 10):
        # not found in candidates
        if (1 << (n - 1)) & candidates:
            board[x][y] = str(n)
            rows[x] &= ~(1 << (n - 1))
            cols[y] &= ~(1 << (n - 1))
            boxes[x // 3 * 3 + y // 3] &= ~(1 << (n - 1))

            if backtracking(board, visit_idx + 1):
                return True

            board[x][y] = '.'
            rows[x] |= (1 << (n - 1))
            cols[y] |= (1 << (n - 1))
            boxes[x // 3 * 3 + y // 3] |= (1 << (n - 1))

    return False


def solve(board: list[list[str]]):
    """
    1. 숫자 n (1~9) 을 본다
    2. n 이 존재하는 가로, 세로, square 에 mark (사용 불가 = x 표시)
    3. 남아 있는 칸 중에서 하나의 가능한 칸 "." 이 남은 곳에 n 을 적는다.
    1~3 을 반복한다.
    """
    global empty_cells, rows, cols, boxes
    # empty_cells = [(i, j) for i in range(9) for j in range(9) if board[i][j] == '.']
    empty_cells = []
    # 1 이면 후보 (존재하지 않는 숫자)
    # 0 이면 탈락 (이미 존재하는 숫자)
    rows = [0b111111111 for _ in range(9)]
    cols = [0b111111111 for _ in range(9)]
    boxes = [0b111111111 for _ in range(9)]

    # candidate 도 메모
    for i in range(9):
        for j in range(9):
            # 후보 칸 찾음
            if board[i][j] == '.':
                empty_cells.append((i, j))
            else:
                # 1 -> 0 변환 필요
                num = int(board[i][j])
                rows[i] &= ~(1 << (num - 1))
                cols[j] &= ~(1 << (num - 1))
                boxes[(i // 3) * 3 + (j // 3)] &= ~(1 << (num - 1))

    backtracking(board, 0)
    print_board(board)


if __name__ == '__main__':
    # board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    #          [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    #          ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    #          [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    #          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    # solve(board)

    time_limit_exceeded_board = [[".", ".", ".", ".", ".", ".", ".", ".", "."],
                                 [".", "9", ".", ".", "1", ".", ".", "3", "."],
                                 [".", ".", "6", ".", "2", ".", "7", ".", "."],
                                 [".", ".", ".", "3", ".", "4", ".", ".", "."],
                                 ["2", "1", ".", ".", ".", ".", ".", "9", "8"],
                                 [".", ".", ".", ".", ".", ".", ".", ".", "."],
                                 [".", ".", "2", "5", ".", "6", "4", ".", "."],
                                 [".", "8", ".", ".", ".", ".", ".", "1", "."],
                                 [".", ".", ".", ".", ".", ".", ".", ".", "."]]
    solve(time_limit_exceeded_board)
