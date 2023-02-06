# from numba import jit
# @jit
def get_det(mat):
    mat = mat.astype('float')
    n = mat.shape[0]#shape0==shape1
    res = 1
    #遍历列
    for col in range(n):
        row = col
        res *= mat[row][col]
        #寻找不是0的位置row
        while mat[row][col] == 0 and row < n - 1:
            row += 1
        #化简mat[row,col]下面的每一元素为0
        for i in range(row + 1, n):
            if mat[i][col] == 0:
                pass
            else:
                k = - mat[i][col] / mat[row][col]
                for j in range(col ,n):
                    mat[i][j] += mat[row][j] * k
    return res

"""
测试：与numpy自带的计算行列式函数进行结果比较
"""
from numpy.random import rand, seed
from numpy.linalg import det
#生成随机行列式
seed(100)
n = 5 
A = rand(n ** 2)
mat = A.reshape(n, n)
#打印numpy函数和自定义函数的结果
print(det(mat), get_det(mat))
#利用iPython的命令对比运行时间，猜猜谁快^
#%timeit det(mat) #100000 loops, best of 3: 7.31 µs per loop
#%timeit get_det(mat) #10000 loops, best of 3: 52.4 µs per loop
#jit 100000 loops, best of 3: 3.52 µs per loop