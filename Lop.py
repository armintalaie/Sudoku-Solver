"""kkdffk"""

# Data
full_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
all_square_options = [[] for i in range(9)]
all_cell_options = [[] for _ in range(9) for _ in range(9)]
all_row_options = [full_numbers.copy() for _ in range(9)]
all_col_options = [full_numbers.copy() for _ in range(9)]


# FUNCTIONS
def remove_intersection(list1, list2):
    return list(set(list1) - (set(list1) & set(list2)))


def square_options(sudoku, x, y):
    x -= x % 3
    y -= y % 3
    current_options = full_numbers.copy()
    for i in range(0, 3):
        for j in range(0, 3):
            if current_options.__contains__(sudoku[x + i][y + j]):
                current_options.remove(sudoku[x + i][y + j])
    all_square_options[x + int(y / 3)] = current_options


def row_or_col_options(sudoku, axis, is_col):
    for j in range(9):
        if is_col:
            if sudoku[j][axis] in all_col_options[axis]:
                all_col_options[axis].remove(sudoku[j][axis])
        else:
            if all_row_options[axis].__contains__(sudoku[axis][j]):
                all_row_options[axis].remove(sudoku[axis][j])


def update_sudoku(sudoku):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            square_options(sudoku_input, i, j)
    for i in range(9):
        row_or_col_options(sudoku, i, False)
        row_or_col_options(sudoku, i, True)


def iterate_options(sudoku, num):
    changed = False
    finished = True
    for i in range(9):
        for m in range(9):
            if sudoku[i][m] != 0:
                continue
            if sudoku[i][m] == 0:
                finished = False

            # if i == 1 and m == 4:
            # print(all_row_options[i])
            # print(all_col_options[m])
            # print(all_square_options[(i - i % 3) + int((m - m % 3) / 3)])
            cell_options = list(set(all_row_options[i]) & set(all_col_options[m]) &
                                set(all_square_options[(i - i % 3) + int((m - m % 3) / 3)]))
            # print(str(i) + " tt " + str(m) + "   " + str(cell_options))
            ra = len(cell_options)
            if ra == 0:
                return False

            if 1 <= ra <= num:
                for p in range(ra):
                    all_row_options[i].remove(cell_options[p])
                    all_col_options[m].remove(cell_options[p])
                    all_square_options[(i - i % 3) + int((m - m % 3) / 3)].remove(cell_options[p])
                    sudoku[i][m] = cell_options[p]
                    # print(str(cell_options) + "    " +  str(sudoku[i][m]))

                    if iterate_options(sudoku, num):
                        changed = True
                        return True

                    else:
                        # print(str(cell_options) + "    " + str(sudoku[i][m]))
                        all_row_options[i].append(cell_options[p])
                        all_col_options[m].append(cell_options[p])
                        all_square_options[(i - i % 3) + int((m - m % 3) / 3)].append(cell_options[p])
                        sudoku[i][m] = 0
                        # print(str(cell_options) + "    " + str(sudoku[i][m]))

                if not changed:
                    # print("meowwwwww")
                    return False

    if finished:
        return True


def solve_sudoku(sudoku):
    update_sudoku(sudoku)
    iterate_options(sudoku, 9)


# running program
with open("SampleSudoku's", "r") as File1:
    sudoku_input = [[0 for _ in range(9)] for _ in range(9)]
    temp = File1.readlines()
    for j, line in enumerate(temp):
        for i in range(0, 9):
            sudoku_input[j][i] = int(line[i:i + 1])

print("input:")
for k in range(9):
    print(sudoku_input[k])

solve_sudoku(sudoku_input)

print("solution:")
for k in range(9):
    print(sudoku_input[k])

# TODO: add more sample sudoku's to solve
# TODO: add the ability to also check with upper/lower rows/column for a narrower margin of options
# TODO: look on the internet for more efficient ways to implement this program
# TODO: add and improve the logic and timing of the program
# TODO: cleanup code and learn python  programming design guides
# TODO: break down the project in multiple more readable files
# TODO: add a GUI to make the program look nicer
