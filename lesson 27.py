from datetime import datetime
import math as m
from random import randint, choice


now = datetime.now()
print(now.strftime("%d-%m-%Y"))
print(m.factorial(5))
print(randint(1,6), choice(['apel','jeruk']))