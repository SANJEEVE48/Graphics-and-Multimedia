import matplotlib.pyplot as plt

def plot_point(x, y):
    plt.plot(x, y, 'bo')

def bresenham_line(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x, y = x1, y1
    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1

    if dx > dy:
        err = dx / 2.0
        while x != x2:
            plot_point(x, y)
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy / 2.0
        while y != y2:
            plot_point(x, y)
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy
    plot_point(x, y)

def midpoint_circle(xc, yc, r):
    x = 0
    y = r
    p = 1 - r
    while x <= y:
        for a, b in [(x, y), (y, x), (-x, y), (-y, x), (-x, -y), (-y, -x), (x, -y), (y, -x)]:
            plot_point(xc + a, yc + b)
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1

plt.figure(figsize=(6, 6))
plt.axis('equal')
plt.grid(True)

bresenham_line(2, 2, 20, 10)
midpoint_circle(10, 10, 8)

plt.title("Bresenham Line and Midpoint Circle")
plt.show()
