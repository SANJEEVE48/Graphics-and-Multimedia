import matplotlib.pyplot as plt
LEFT, RIGHT, BOTTOM, TOP = 0, 1, 2, 3
def inside(p, edge, clip_win):
    x, y = p
    xmin, xmax, ymin, ymax = clip_win
    if edge == LEFT:
        return x >= xmin
    elif edge == RIGHT:
        return x <= xmax
    elif edge == BOTTOM:
        return y >= ymin
    elif edge == TOP:
        return y <= ymax
def intersect(p1, p2, edge, clip_win):
    xmin, xmax, ymin, ymax = clip_win
    x1, y1 = p1
    x2, y2 = p2

    if edge == LEFT:
        x = xmin
        y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
    elif edge == RIGHT:
        x = xmax
        y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
    elif edge == BOTTOM:
        y = ymin
        x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
    elif edge == TOP:
        y = ymax
        x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)

    return (x, y)

def clip_polygon(polygon, clip_win):
    output = polygon
    for edge in [LEFT, RIGHT, BOTTOM, TOP]:
        input_list = output
        output = []
        if not input_list:
            break
        s = input_list[-1]
        for p in input_list:
            if inside(p, edge, clip_win):
                if not inside(s, edge, clip_win):
                    output.append(intersect(s, p, edge, clip_win))
                output.append(p)
            elif inside(s, edge, clip_win):
                output.append(intersect(s, p, edge, clip_win))
            s = p
    return output

def draw_polygon(points, color, label):
    if not points:  # Prevents error if polygon is empty
        return
    x, y = zip(*(points + [points[0]]))
    plt.plot(x, y, color=color, label=label)

def draw_clip_window(clip_win):
    xmin, xmax, ymin, ymax = clip_win
    x = [xmin, xmax, xmax, xmin, xmin]
    y = [ymin, ymin, ymax, ymax, ymin]
    plt.plot(x, y, 'k--', label="Clipping Window")
if __name__ == "__main__":
    polygon = [(1, 2), (5, 8), (9, 5), (6, 1), (2, 0)]
    clip_window = (2, 7, 1, 6)  # xmin, xmax, ymin, ymax

    clipped = clip_polygon(polygon, clip_window)

    plt.figure()
    draw_polygon(polygon, 'b', "Original Polygon")
    draw_polygon(clipped, 'r', "Clipped Polygon")
    draw_clip_window(clip_window)

    plt.legend()
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()
