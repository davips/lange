![test](https://github.com/davips/lange/workflows/test/badge.svg)
[![codecov](https://codecov.io/gh/davips/lange/branch/main/graph/badge.svg)](https://codecov.io/gh/davips/lange)

# lange
Lazy lists (i.e. Haskell-like ranges) for Python.

## Installation
### from package
```bash
# Set up a virtualenv. 
python3 -m venv venv
source venv/bin/activate

# Install from PyPI
pip install lange
```

### from source
```bash
cd my-project
git clone https://github.com/davips/lange ../lange
pip install -e ../lange
```


### Features
 * Stable floating-point range generation, e.g.: `0.8 - 0.6 == 0.2` up to 28 digits (customizable).
 * Infinite `[1 2 ...]` or bounded.
 * O(1) access/evaluation `lst[3443]`


### Examples

<<ap>>

<<gp>>
