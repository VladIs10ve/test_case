# Узнать пересекаются ли треугольники, найти площадь пересечения.
def task(x1, y1, x2, y2, x3, y3, x4, y4):
    x1_min = min(x1, x2)
    x1_max = max(x1, x2)
    y1_min = min(y1, y2)
    y1_max = max(y1, y2)

    x2_min = min(x3, x4)
    x2_max = max(x3, x4)
    y2_min = min(y3, y4)
    y2_max = max(y3, y4)

    x_left = max(x1_min, x2_min)
    x_right = min(x1_max, x2_max)
    y_low = max(y1_min, y2_min)
    y_high = min(y1_max, y2_max)

    if x_right - x_left < 0 or y_high - y_low < 0:
        return False
    else:
        return abs(x_right - x_left) * abs(y_high - y_low)


print(task(0, 3, 3, 0, 1, 1, 2, 2))
