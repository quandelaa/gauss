# gauss

A linear algebra library that provides functions to calculate lengthy, and tireful calculations automatically.

TODO:
- work on LU decomposition until it ultimately works
- complete row_space and column_space functions

## Installation
Install via GitHub repository:

```bash
pip install git+https://github.com/quandelaa/gauss.git
```

## Example
```python
import gauss

A = [[1, 2, 3],
     [1, 4, 5],
     [2, 1, 13]]

U = gauss.ref(A)
R = gauss.rref(A)

rank = gauss.rank(A)
inv = gauss.inverse(A)

print(U)
print(R)

print(rank)
print(inv)
```

## License

This project is licensed under the MIT License - see the LICENSE file for details

---

* All made by `quandela`
