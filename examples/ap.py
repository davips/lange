# Arithmetic Progression

# "Forbidden" syntax.
import lange
print(-[0.6, 0.8, ..., 2])
# ...

# Conservative syntax.
from lange_ import a_
print(a_[0.6, 0.8, ..., 2])
# ...

pr = a_[0.6, 0.8, ...]
print(pr[:5])
# ...
