# Geometric Progression

# Forbidden syntax.
from lange import *
print(~[0.6, 0.8, ..., 2])
# ...

# Conservative syntax.
from lange_ import g_
print(g_[0.6, 0.8, ..., 2])
# ...

pr = g_[0.6, 0.8, ...]
print(pr[:5])
# ...
