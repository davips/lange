![test](https://github.com/davips/hange/workflows/test/badge.svg)
[![codecov](https://codecov.io/gh/davips/hange/branch/main/graph/badge.svg)](https://codecov.io/gh/davips/hange)

# hange
Haskell-like intervals for Python

# Intallation
```bash
pip install autoreadme
rewritereadme
```

# Example
A typical *README-edit.md* file would be:

```markdown
# Uses
We can cook using the following Python code:
<<cook>>

But we can also clean:
<<clean>>
```

The example file (given in this repo as *examples/README-edit.md*) depends on two scripts.
Each script should have a `# ...` line where the output until that moment is expected to appear:

*examples/cook.py*:
```python3
# Cooking
x = 2 * 8
print("This script prints something:", x)
# ...
```

*examples/clean.py*:
```python3
# Cleaning
y = 34 % 5
print("this script prints another thing.", y)
# ...
```

Running...
```bash
rewritereadme -i examples/README-edit.md -s examples/ -o examples/README.md examples/README-edit.md
```
...will result in the following markdown:

<blockquote>
# Uses

We can cook using the following Python code:

<details>
<summary>Cooking</summary>
<p>

```python3
x = 2 * 8
print("This script prints something:", x)
```

```
This script prints something: 16
```

</p>
</details>

But we can also clean:
<details>
<summary>Cleaning</summary>
<p>

```python3
y = 34 % 5
print("this script prints another thing.", y)
```

```
this script prints another thing. 4
```

</p>
</details>
</blockquote>
