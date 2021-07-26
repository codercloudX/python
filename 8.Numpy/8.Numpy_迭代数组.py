import numpy as np

a = np.arange(6).reshape(2, 3)
print(a)
for x in np.nditer(a):
    print(x, end=",")
print("\n")
for x in np.nditer(a, order="F"):  # Fortran order,列序优先
    print(x, end=",")
print("\n")
for x in np.nditer(a, order="C"):  # C order,行序优先
    print(x, end=",")
print("\n")
