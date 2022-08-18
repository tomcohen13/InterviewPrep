def surfaceArea(A):
    if not A: 
        return 0
    # define dimensions of 2d array
    H = len(A) # rows
    W = len(A[0]) # columns
    
    total = 0
    # go over board cells
    for i in range(H):
        for j in range(W):
            
            print(A[i][j])
            
            if A[i][j] > 0: 
                total += 2 # top + bottom
            
            # sides
            # case 1: outer shell
            if i == 0:
                total += A[i][j]
            if i == H - 1:
                total += A[i][j]
            if j == 0: 
                total += A[i][j]
            if j == W - 1:
                total += A[i][j]
            # 
            neighbors = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
            for ni,nj in neighbors:
                # if valid
                if (ni >= 0 and nj >= 0 and ni < H and nj < W) and A[i][j] 
> A[ni][nj]:
                    total += A[i][j] - A[ni][nj]
                    
    return total
                
            

