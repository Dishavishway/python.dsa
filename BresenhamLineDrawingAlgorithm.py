def bresenham_line(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    slope = dy > dx

    if slope:
        x1, y1 = y1, x1  # Swap x1 and y1
        x2, y2 = y2, x2  # Swap x2 and y2

    if x1 > x2:
        x1, x2 = x2, x1  # Swap x1 and x2
        y1, y2 = y2, y1  # Swap y1 and y2

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    p = 2 * dy - dx
    two_dy = 2 * dy
    two_dy_minus_dx = 2 * (dy - dx)

    if slope:
        x, y = y1, x1
    else:
        x, y = x1, y1

    points = [(x, y)]

    while x < x2:
        x += 1
        if p < 0:
            p += two_dy
        else:
            y += 1 if y1 < y2 else -1
            p += two_dy_minus_dx
        if slope:
            points.append((y, x))
        else:
            points.append((x, y))

    return points

# Example usage:
x1, y1 = 1, 2
x2, y2 = 7, 6
line_points = bresenham_line(x1, y1, x2, y2)
for point in line_points:
    print(point)
