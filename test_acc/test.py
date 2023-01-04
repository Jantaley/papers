import ctypes
import numpy.ctypeslib as npctl
from numpy.ctypeslib import ndpointer
import numpy as np
mylib = ctypes.cdll.LoadLibrary("./cppfuncs.so")

# char_p_test = bytes("中国","utf8")#汉字需用采用utf8编码

# int_arr4 = ctypes.c_int*4


# int_arr = int_arr4()

# int_arr[0] = 1

# int_arr[1] = 3

# int_arr[2] = 5

# int_arr[3] = 9

# char_arr2 = ctypes.c_char*2

# char_arr22 = char_arr2*2

# char_arr22a = char_arr22()

# char_arr22a[0][0] = b'a'

# char_arr22a[0][1]=  b'b'

# char_arr22a[1][0] = b'c'

# char_arr22a[1][1] = b'd'

# mylib.test(9999,'a',char_p_test,int_arr,char_arr22a)


#####
np.random.seed(100)
input_arr = np.random.rand(2)
input_arr[0] = 6106998.5
input_arr[1] = 29.25
input_arr = input_arr.astype(np.float32)
mylib.float_accsum.argtypes=[npctl.ndpointer(dtype=np.float32,flags="aligned, C_CONTIGUOUS"),ctypes.c_int]
mylib.float_accsum.restype = ctypes.c_float;
ret = mylib.float_accsum(input_arr, 2);

print("send = ",input_arr,"return=", ret)