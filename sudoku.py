from sudoku_class import *

asudoku=sudoku()

for n in range(30, 75, 5):
    completed=0
    for trials in range(1,50):
        asudoku.makepuzzle(n)
        asudoku.solve()
        asudoku.solved()
        if asudoku.solved()== True:
            completed = completed + 1
    print(n,completed/trials)
