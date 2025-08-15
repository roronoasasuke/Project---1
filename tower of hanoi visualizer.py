def center(s, width):
    pad = max(width - len(s), 0)
    left = pad // 2
    right = pad - left
    return " " * left + s + " " * right

def draw(pegs, n):
    width = 2 * n + 1
    lines = []
    for level in range(n - 1, -1, -1):
        row = []
        for p in pegs:
            size = p[level] if level < len(p) else 0
            if size == 0:
                row.append(center("|", width))
            else:
                disk = "=" * (2 * size - 1)
                row.append(center(disk, width))
        lines.append("   ".join(row))
    base = "   ".join("-" * width for _ in range(3))
    labels = "   ".join(center(x, width) for x in ["A", "B", "C"])
    print("\n".join(lines))
    print(base)
    print(labels)
    print()

def move(pegs, from_idx, to_idx, n, total_n):
    disk = pegs[from_idx].pop()
    pegs[to_idx].append(disk)
    draw(pegs, total_n)

def hanoi(k, a, b, c, pegs, total_n):
    if k == 0:
        return
    hanoi(k - 1, a, c, b, pegs, total_n)
    move(pegs, a, c, k, total_n)
    hanoi(k - 1, b, a, c, pegs, total_n)

n = 7
A = list(range(n, 0, -1))
B = []
C = []
draw([A[:], B[:], C[:]], n)
hanoi(n, 0, 1, 2, [A, B, C], n)