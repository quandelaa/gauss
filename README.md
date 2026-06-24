# gauss

A linear algebra library that provides functions to calculate lengthy, tireful calculations automatically

TODO:
- LU decomposition
- Nullity of a matrix

## Installation
Install via GitHub repository:

```bash
uv pip install git+https://github.com/quandelaa/gauss.git
```

## Example
```python
import gauss

A = [[1, 2, 3],
     [1, 4, 5],
     [5, 8, 13]]

U = gauss.ref(A)
R = gauss.rref(A)

print(U)
print(R)

```

## License

This project is licensed under the MIT License - see the LICENSE file for details

---

* All made by `quandela`
