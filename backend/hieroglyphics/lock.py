import ctypes

a=0x108bb24d0
b=0x123bb32d0
address=id(a)
address2=id(b)
print(address)
z=ctypes.cast(address, ctypes.py_object).value
print(z)