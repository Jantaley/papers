'''
for the design reference of broadcast
'''
from opdef import * 
import numpy as np
sop=scalarop()
vop=vectorop()
top=tensorop()

#tight unalighed
ashape = [4,3,1,5]
bshape = [1,3,2,1]
a=np.arange(np.multiply.reduce(ashape))
b=np.arange(np.multiply.reduce(bshape))
cshape=np.maximum(ashape,bshape)
c0=np.empty(cshape)
ac=c0.flatten()
bc=c0.flatten()

sop.broadcast(cshape,ashape,ac,a)
a0=a.reshape(ashape)
ac0=ac.reshape(cshape)
sop.broadcast(cshape,bshape,bc,b)
b0=b.reshape(bshape)
bc0=bc.reshape(cshape)
res=ac+bc


#aligned to bankwidth
ashape = [4,3,1,5,16]
bshape = [1,3,2,1,16]
a=np.arange(np.multiply.reduce(ashape))
a=a.reshape(-1,16)
b=np.arange(np.multiply.reduce(bshape))
b=b.reshape(-1,16)
cshape=np.maximum(ashape,bshape)
c0=np.empty(cshape)
ac=c0.reshape(-1,16)
bc=c0.reshape(-1,16)

sop.broadcast(cshape[0:-1],ashape[0:-1],ac,a)
a0=a.reshape(ashape)
ac0=ac.reshape(cshape)
sop.broadcast(cshape[0:-1],bshape[0:-1],bc,b)
b0=b.reshape(bshape)
bc0=bc.reshape(cshape)
res=ac+bc
