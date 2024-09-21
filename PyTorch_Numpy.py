#Convert PyTorch Tensor to Numpy Array and the opposite
import torch    
import numpy as np

#Convert a Torch Tensor to a Numpy Array
torch_tensor = torch.rand([2,2])
print(f"this is a PyTorch Tensor:{torch_tensor}")
numpy_array = torch_tensor.numpy()
print(f"This is a PyTorch Tensor converted to a Numpy Array {numpy_array}")
new_numpy_tensor = torch.from_numpy(numpy_array)
print(f"This is a Numpy Array converted to a PyTorch Tensor {numpy_array}")
