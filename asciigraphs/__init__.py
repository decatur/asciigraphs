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
