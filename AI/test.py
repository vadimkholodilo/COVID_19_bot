
from model import *

loaded_model = get_model()
print(loaded_model)


lst = [1, 0, 0, 0, 0, 0, 0, 1]
print(loaded_model(lst))