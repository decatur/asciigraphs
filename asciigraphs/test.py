from datetime import date
from ..asciigraph import parse_ascii_func

f = parse_ascii_func(glyph='*', graph="""
    3|     *
    2|*   *
    1| * *
    0|--*------------
""")

print(f)  # {0: 2, 1: 1, 2: 0, 3: 1, 4: 2, 5: 3}

ts = parse_ascii_func(glyph='*', graph="""
    3|     *
    2|*   *
    1| * *
    0|--*------------
""", index=[date(2020, 6, day) for day in range(12, 18)])

print(ts)  # {date(2020, 6, 12): 2, date(2020, 6, 13): 1, date(2020, 6, 14): 0, date(2020, 6, 15): 1, date(2020, 6, 16): 2, date(2020, 6, 17): 3}

from ..asciigraph import parse_ascii_funcs

g, h, p = parse_ascii_funcs(glyphs=['*', '+', '#'], graph="""
       g()
       3|     *
       2|*   *
       1| * *
       0|--*------------

     h() p()
       3|  +
       2|++ 
       1|##
       0|--#------------
   """)

print(g)  # {0: 2, 1: 1, 2: 0, 3: 1, 4: 2, 5: 3}
print(h)  # {0: 2, 1: 2, 2: 3}
print(p)  # {0: 2, 1: 2, 2: 3}
