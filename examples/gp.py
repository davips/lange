# Geometric Progression

# Bounded
from lange import gp
print(gp[0.4, 0.8, ..., 2])
# ...

# Infinite + slicing
prog = gp[0.4, 0.8, ...]
print(prog[:5])
# ...

# As list
print(list(prog[:5]))
# ...

print(prog[:5].l)
# ...
