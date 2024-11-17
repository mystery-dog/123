def print_board(board):
    for row in board:
        print(" ".join(str(num) for num in row))


def is_valid(board, row, col, num):
    # 檢查行
    for j in range(9):
        if board[row][j] == num:
            return False

    # 檢查列
    for i in range(9):
        if board[i][col] == num:
            return False

    # 檢查3x3子格
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True


def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # 找到一個空白格子
                for num in range(1, 10):  # 嘗試填入1到9
                    if is_valid(board, row, col, num):
                        board[row][col] = num  # 填入數字
                        if solve_sudoku(board):  # 繼續解決
                            return True
                        board[row][col] = 0  # 回溯
                return False  # 如果沒有數字有效
    return True  # 所有格子都已填滿


def input_sudoku():
    print("請輸入數獨的題目，每行用空格分隔數字 (0 代表空白格)：")
    board = []
    for i in range(9):
        row = list(map(int, input(f"輸入第 {i + 1} 行: ").split()))
#list():將字符串分割 ex:list('Hello') output(['H','e','l','l','o'])
#.split():將字符串以空格分割 ex:('Hello World') output(['Hello', 'World'])
#map(int):將內容形態轉成int
#順序:input->,split()->map(int)->list()
        if len(row) != 9:
            raise ValueError("每行必須包含 9 個數字")
        board.append(row)
    return board


# 輸入數獨板
sudoku_board = input_sudoku()

if solve_sudoku(sudoku_board):
    print("解答如下：")
    print_board(sudoku_board)
else:
    print("不存在解答")