# Get system resources

import os
import platform
a = platform.machine()
b = platform.platform()
c = platform.uname()
d = platform.python_version()
e = os.getlogin()
f = os.getloadavg()
g = os.listdir()
h = platform.system()
print(a)
print(b)
print(c)
print(d)
print(f)
print(g)
print(h)