import torch
import numpy as np
torch.random.manual_seed(123124)
data  = torch.randn(5,16)
data2 = torch.randn(10,16)
data2[-5:, :] = data
w = torch.randn(16,16)
resp0 = (data.numpy()).dot(w.numpy())
resp1 = (data2.numpy()).dot(w.numpy())[-5::]
r0= torch.matmul(data, w) 
r1= torch.matmul(data2, w)[-5: :]
diff0 = r0 - r1
np.savetxt("a.txt",w.numpy(),delimiter=" ")
np.savetxt("w.txt",w.numpy(),delimiter=" ")

print("[5,16][16,16]two numpy multi diff [10,16][16,16]\n", resp0 - resp1, "\n")
print("[5,16][16,16]two torch multi diff [10,16][16,16]\n", r0 - r1, "\n")
print("[5,16][16,16]numpy - torch multi diff [5,16][16,16]\n", resp0 - r0.numpy(), "\n")
print("[10,16][16,16]numpy - torch multi diff [10,16][16,16]\n", resp1 - r1.numpy())


