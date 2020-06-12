from typing import Dict, List


def parse_ascii_func(glyph: str, graph: str) -> Dict[int, int]:
    """
    Parses an ascii function
    """

    f = {}
    for line in graph.splitlines():
        parts = line.split('|')
        if len(parts) != 2:
            continue
        y, x_values = parts
        indices = [i for i, c in enumerate(x_values) if c == glyph]
        for i in indices:
            f[i] = int(y.strip())

    return dict(sorted(f.items()))


def parse_ascii_funcs(glyphs: List[str], graph: str) -> List[Dict[int, int]]:
    return [parse_ascii_func(glyph, graph) for glyph in glyphs]


def reindex(f, new_index):
    return {new_index[x]: y for x, y in f.items()}


def diff_func(f):
    keys = list(f.keys())
    values = list(f.values())
    # return dict(zip(shift_keys, [(values[i]-values[i-1]) / (keys[i]-keys[i-1]) for i in shift_keys]))
    return {keys[i]: (values[i]-values[i-1]) for i in range(1, len(keys))}


if __name__ == '__main__':
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
