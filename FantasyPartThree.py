#########################
#Reed Zhang p.1 4/7/2015#
#########################

def multiplyVectorMatrix(v,m):
    product = [0 for i in range(len(m[0]))]
    for i in range(len(m)):
        for j in range(len(m[i])):
            product[j]+=v[i]*m[i][j]
    print(product)

def printMatrix(m):
    print('---MATRIX:')
    for row in m:
        s = ''
        for element in row:
            truncated = round(element,2)
            length = len(str(truncated))
            for i in range(10-length):
                s += ' '
            s += str(round(element,2))
        print(s)
    print('==============================')

def main():
 #   M = [[1 for COL in range(4)] for ROW in range(3)] #M  =  3-rows x 4-cols matrix
    V = [1,2,4]
    M = [[1,2,3],[4,5,6],[7,8,9]]
    print(V)
    print('times')
    printMatrix(M)
    print('equals')
    multiplyVectorMatrix(V,M)
    
main()