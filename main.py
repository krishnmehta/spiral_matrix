def PrintMatrix(m):
    top = 0
    left = 0
    bottom = len(m) - 1
    right = len(m[0]) - 1
 
    while True:
        if left > right:
            break
 
        for i in range(left, right + 1): #Printing the top row
            print(m[top][i], end=' ')
        top += 1
 
        if top > bottom:
            break
 
    
        for j in range(top, bottom + 1): #Printing the right column
            print(m[j][right], end=' ')
        right -= 1
 
        if left > right:
            break
 
    
        for k in range(right, left - 1, -1): #Printing the bottom row
            print(m[bottom][k], end=' ')
        bottom -= 1
 
        if top > bottom:
            break
 
        for l in range(bottom, top - 1, -1): #Printing the left column
            print(m[l][left], end=' ')
        left += 1
 
 
if __name__ == '__main__':
 
    m1 = [[1, 2, 3],
        [4,5,6],
        [7,8,9]]
    
    m2 = [[1, 2, 3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]]
 
    PrintMatrix(m1) #Printing matrix m1 in spiral order
    print()
    PrintMatrix(m2) #Printing matrix m2 in spiral order