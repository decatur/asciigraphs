from ..asciigraph import parse_ascii_func, parse_ascii_funcs, diff_func

f = parse_ascii_func(glyph='*', graph="""
    3|     *
    2|*   *
    1| * *
    0|--*------------
""")

print(f)  # {0: 2, 1: 1, 2: 0, 3: 1, 4: 2, 5: 3}
print(diff_func(f))  # {1: -1.0, 2: -1.0, 3: 1.0, 4: 1.0, 5: 1.0}

g, h = parse_ascii_funcs(glyphs=['*', '+'], graph="""
       3|     *
       2|*   *
       1| * *
       0|--*------------

       3|  +
       2|++ 
       0|---------------
   """)

print(g)  # {0: 2, 1: 1, 2: 0, 3: 1, 4: 2, 5: 3}
print(h)  # {0: 2, 1: 2, 2: 3}
