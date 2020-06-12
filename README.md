# asciigraphs
Python package to parse functions from their graphs.

# install

```bash
pip install git+https://github.com/decatur/asciigraphs.git
```

# Example

```python
from ..asciigraph import parse_ascii_func

f = parse_ascii_func(glyph='*', graph="""
        3|     *
        2|*   *
        1| * *
        0|--*------------
    """)

    print(f)  # {0: 2, 1: 1, 2: 0, 3: 1, 4: 2, 5: 3}
 ```
