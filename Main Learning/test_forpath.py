import os
import sys
print(os.path.dirname(__file__))
sys.path.append(os.path.dirname(__file__))

print(sys.path)

print(os.getcwd())