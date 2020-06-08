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


def find_cell_options(i, m):
    return list(set(all_row_options[i]) & set(all_col_options[m]) &
                set(all_square_options[(i - i % 3) + int((m - m % 3) / 3)]))


def iterate_options(sudoku, num):
    finished = True
    for i in range(9):
        for m in range(9):
            if sudoku[i][m] != 0:
                continue
            if sudoku[i][m] == 0:
                finished = False

            # print(all_row_options[i])
            # print(all_col_options[m])
            # print(all_square_options[(i - i % 3) + int((m - m % 3) / 3)])
            cell_options = find_cell_options(i, m)
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
                        return True

                    else:
                        # print(str(cell_options) + "    " + str(sudoku[i][m]))
                        all_row_options[i].append(cell_options[p])
                        all_col_options[m].append(cell_options[p])
                        all_square_options[(i - i % 3) + int((m - m % 3) / 3)].append(cell_options[p])
                        sudoku[i][m] = 0
                        # print(str(cell_options) + "    " + str(sudoku[i][m]))
                return False

    return finished


def initial_solve(sudoku):
    changed = False
    for i in range(9):
        for m in range(9):
            if sudoku[i][m] != 0:
                continue
            cell_options = find_cell_options(i, m)
            if len(cell_options) == 1:
                all_row_options[i].remove(cell_options[0])
                all_col_options[m].remove(cell_options[0])
                all_square_options[(i - i % 3) + int((m - m % 3) / 3)].remove(cell_options[0])
                sudoku[i][m] = cell_options[0]
                print("yes momma")
                print(i)
                print(m)
                changed = True
    return changed


def naked_pairs(sudoku):
    pass


def section_check(sudoku):
    changed = False

    for w in range(0, 3):
        for q in range(0, 3):
            answers = [[z, 0, -1, -1] for z in range(1, 10)]
            for i in range(0, 3):
                for j in range(0, 3):
                    if sudoku[i + w*3][j + q*3] != 0:
                        continue

                    cell_options = find_cell_options(i + w*3, j + q*3)

                    for k in cell_options:
                        answers[k - 1][1] += 1
                        answers[k - 1][2] = i + w*3
                        answers[k - 1][3] = j + q*3

            for i in range(9):
                if answers[i][1] == 1:
                    sudoku[answers[i][2]][answers[i][3]] = answers[i][0]
                    # print("next" + str(i) + "oo" + str(j) + "  " + str(w) + "  " + str(q))
                    all_square_options[w*3 + q].remove(answers[i][0])
                    all_row_options[answers[i][2]].remove(answers[i][0])
                    all_col_options[answers[i][3]].remove(answers[i][0])
                    changed = True
                    print(answers[i][2])
                    print(answers[i][3])
                    # print(answers[i])
                    print("yepp")
                    print_sudoku(sudoku)
    return changed


def solve_sudoku(sudoku):
    update_sudoku(sudoku)
    changing = True

    while changing:
        if initial_solve(sudoku) or section_check(sudoku):
            print("yes")
            continue
        else:
            changing = False

    naked_pairs(sudoku)
    iterate_options(sudoku, 9)


def print_sudoku(sudoku):
    for k in range(9):
        print(sudoku[k])


# running program
with open("s2", "r") as File1:
    sudoku_input = [[0 for _ in range(9)] for _ in range(9)]
    temp = File1.readlines()
    for n, line in enumerate(temp):
        for i in range(0, 9):
            sudoku_input[n][i] = int(line[i:i + 1])

print("input:")
print_sudoku(sudoku_input)

solve_sudoku(sudoku_input)

print("solution:")
print_sudoku(sudoku_input)

# TODO: add more sample sudoku's to solve
# TODO: add the ability to also check with upper/lower rows/column for a narrower margin of options
# TODO: look on the internet for more efficient ways to implement this program
# TODO: add and improve the logic and timing of the program
# TODO: cleanup code and learn python  programming design guides
# TODO: break down the project in multiple more readable files
# TODO: add a GUI to make the program look nicer
