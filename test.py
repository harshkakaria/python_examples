import time
from importlib import reload
import py_modules
print('program entering into sleeping state')
time.sleep(30)
reload(py_modules)
print('program entering into sleeping state')
time.sleep(30)
reload(py_modules)
print('this is the last line of the program')











