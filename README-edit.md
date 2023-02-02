![test](https://github.com/davips/lange/workflows/test/badge.svg)
[![codecov](https://codecov.io/gh/davips/lange/branch/main/graph/badge.svg)](https://codecov.io/gh/davips/lange)
<a href="https://pypi.org/project/lange">
<img src="https://img.shields.io/pypi/v/lange.svg?label=release&color=blue&style=flat-square" alt="pypi">
</a>
![Python version](https://img.shields.io/badge/python-3.8...-blue.svg)
[![license: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

<!--- [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5501845.svg)](https://doi.org/10.5281/zenodo.5501845) --->
<!--- [![arXiv](https://img.shields.io/badge/arXiv-2109.06028-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2109.06028) --->
[![API documentation](https://img.shields.io/badge/doc-API%20%28auto%29-a0a0a0.svg)](https://davips.github.io/lange)

# lange
Lazy lists (i.e. Haskell-like ranges) for Python.
[Latest release](https://pypi.org/project/lange) |
[Current code](https://github.com/davips/lange) |
[API documentation](https://davips.github.io/lange)

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
