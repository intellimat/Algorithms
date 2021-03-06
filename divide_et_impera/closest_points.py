#Uses python3
import math

def get_minimum_distance(points):
    points.sort(key = lambda p : p[0])  # Sorts points based on x coordinate
    minimum_distance = recursive_function(points, 0, len(points)-1)
    return minimum_distance

def recursive_function (points, left, right):
    if right - left + 1 == 3:   # Three elements present
        p1 = points[left]
        p2 = points[left+1]
        p3 = points[right]
        d_min = min(get_distance(p1,p3), get_distance(p2,p1), get_distance(p2,p3))
        return d_min

    if right == left + 1:   # Two elements present
        d_min = get_distance(points[left], points[right])
        return d_min

    mid = left + (right-left) // 2

    d1 = recursive_function(points, left, mid)
    d2 = recursive_function(points, mid+1, right)    

    if d1 <= d2:
        d_min = d1
    else:
        d_min = d2

    mid_line = points[mid][0]

    y_sorted_points = [p for p in points[left:right+1] if (p[0] >= (mid_line-d_min) and p[0] <= (mid_line+d_min))]

    y_sorted_points.sort(key = lambda p : p[1])


    for i in range(0, len(y_sorted_points)):
        p1 = y_sorted_points[i]
        for j in range(i+1, min(i+7, len(y_sorted_points))):
            p2 = y_sorted_points[j]
            d_p1_p2 = get_distance(p1,p2)
            if  d_p1_p2 < d_min:
                d_min = d_p1_p2
    
    return d_min

def get_distance(p1,p2):
    p1_x = p1[0]
    p1_y = p1[1]

    p2_x = p2[0]
    p2_y = p2[1]

    delta_x = abs(p1_x - p2_x)
    delta_y = abs(p1_y - p2_y)

    d = math.sqrt((delta_x * delta_x) + (delta_y * delta_y))

    return round(d, 4)

if __name__ == '__main__':
    n = int(input())

    points = []
    for i in range(n):
        t = tuple(map(int,input().split())) # t represents a point
        points.append(t)

    minimum_distance = get_minimum_distance(points)

    print(minimum_distance)
