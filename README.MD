#Welcome to the README.MD file of the project "Data Science and Machine Learning with Python".

```py
import numpy as np

np.random.seed(0)
x1 = np.random.randint(10, size=6)
x2 = np.random.randint(10, size=(3, 4))
if x1.ndim == 1:
    print(f"x1: {x1}")
    print(f"x1 shape: {x1.shape}")
    print(f"x1 size: {x1.size}")
    print(f"x1 dtype: {x1.dtype}")
    print(f"x1 itemsize: {x1.itemsize}")
    print(f"x1 nbytes: {x1.nbytes}")
    print(f"x1 strides: {x1.strides}")
    print(f"x1 data: {x1.data}")
    print(f"x1 flags: {x1.flags}")
```
[!NOTE]
> The code above creates a one-dimensional array with 6 elements. The code then prints the shape, size, data type, item size, number of bytes, strides, and data of the array.
> The output of the code is as follows:
> x1: [5 0 3 3 7 9]
> x1 shape: (6,)
> x1 size: 6
>x1 dtype: int32
```py	    
#Iterating over the elements of the array
for i in range(len(x1)):
    print(f"x1[{i}]: {x1[i]}")
```
