from typing import Dict, List, Any


def parse_ascii_func(glyph: str, graph: str, index: List[Any] = None) -> Dict[int, int]:
    """
    Parse a single ascii function
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

    f = dict(sorted(f.items()))
    if index:
        f = {index[x]: y for x, y in f.items()}
    return f


def parse_ascii_funcs(glyphs: List[str], graph: str, index: List[Any] = None) -> List[Dict[int, int]]:
    """
    Parse multiple ascii functions
    """
    return [parse_ascii_func(glyph, graph, index) for glyph in glyphs]
