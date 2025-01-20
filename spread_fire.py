import copy


def spread_fire(grid):
    """Update the forest grid based on fire spreading rules."""
    grid_size = len(grid)
    update_grid = copy.deepcopy(grid)

    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == 1:  # אם יש עץ
                # בדיקת גבולות לפני גישה לשכנים
                if i > 0 and grid[i - 1][j] == 2:  # מעלה
                    update_grid[i][j] = 2
                if i < grid_size - 1 and grid[i + 1][j] == 2:  # מטה
                    update_grid[i][j] = 2
                if j > 0 and grid[i][j - 1] == 2:  # שמאלה
                    update_grid[i][j] = 2
                if j < grid_size - 1 and grid[i][j + 1] == 2:  # ימינה
                    update_grid[i][j] = 2

    return update_grid

