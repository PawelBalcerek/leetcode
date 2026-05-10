class Solution:
    def search_a_2d_matrix(self, matrix: list[list[int]], target: int) -> bool:
        row_l, row_r = 0, len(matrix) - 1
        row_index = -1

        while row_l <= row_r:
            row_m = (row_l + row_r) // 2
            row = matrix[row_m]

            if row[0] <= target <= row[-1]:
                row_index = row_m
                break
            elif row[-1] < target:
                row_l = row_m + 1
            else:
                row_r = row_m - 1

        if row_index == -1:
            return False
        
        row_to_search = matrix[row_index]
        l, r = 0, len(row_to_search) - 1

        while l <= r:
            m = (l + r) // 2
            
            if row_to_search[m] == target:
                return True
            elif row_to_search[m] < target:
                l = m + 1
            else:
                r = m - 1

        return False
