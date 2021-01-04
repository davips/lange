# Geometric Progression

# "Forbidden" syntax.
import lange
print(~[0.4, 0.8, ..., 2])
# ...

# Conservative syntax.
from lange_ import g_
print(g_[0.4, 0.8, ..., 2])
# ...

pr = g_[0.4, 0.8, ...]
print(pr[:5])
# ...
