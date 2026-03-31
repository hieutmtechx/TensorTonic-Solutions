def rating_normalization(matrix):
    """
    Mean-center each user's ratings in the user-item matrix.
    """
    # Write code here

    norm_matrix = []
    for row in matrix:
        count = 0
        sum = 0
        for element in row:
            if (element > 0):
                count += 1
                sum += element
        
        mean = (sum / count) if (count > 0) else 0
    
        norm_row = []
        for element in row:
            if (element > 0):
                norm_row.append(element - mean)
            else:
                norm_row.append(element)

        norm_matrix.append(norm_row)

    return norm_matrix