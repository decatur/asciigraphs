# asciigraphs
Python package to parse functions from their graphs.

# install

```bash
pip install git+https://github.com/decatur/asciigraphs.git
```

# Example Single Function

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
 
 # Example Multiple Functions
```python
from ..asciigraph import parse_ascii_funcs

g, h = parse_ascii_funcs(glyphs=['*', '+'], graph="""
       g()
       3|     *
       2|*   *
       1| * *
       0|--*------------

       h() 
       3|  +
       2|++ 
       0|---------------
   """)

print(g)  # {0: 2, 1: 1, 2: 0, 3: 1, 4: 2, 5: 3}
print(h)  # {0: 2, 1: 2, 2: 3}
 ```
