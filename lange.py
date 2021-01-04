from forbiddenfruit import curse

from lange_.ap import AP
from lange_.gp import GP

curse(list, "__neg__", lambda l: AP(*l))
curse(list, "__inv__", lambda l: GP(*l))
