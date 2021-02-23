# Uses python3

# Key idea
# Let's sort the segments considering the end of each segment
# If we take the segment that has the shortest end coordinate (let's call this segment s), two things can happen:
# 1) Subsequent segment has the start point behind s end point and the end point after s end point (because the segments are sorted by evaluating the end point)
#    So, in this case, by taking s end point we cover also the subsequent segment
# 2) Subsequent segment starts after s end point
#    So we gotta take s end point in order to cover s otherwise s will be uncovered

def optimal_points(segments):
    points = []
    # sort segments based on the end of the segment
    segments.sort(key = lambda elem : elem[1])

    # take the end of the first segment
    points.append(segments[0][1])
    last_added = segments[0][1]
    

    for s in segments:
        if (not (last_added >= s[0] and last_added <= s[1])) and (s[1] not in points):
            points.append(s[1])
            last_added = s[1]

    return points

    
if __name__ == '__main__':
    n = int(input())
    segments = []
    for i in range(n):
        pair = list(map(int,input().split()))
        segments.append(pair)
    points = optimal_points(segments)
    print(len(points))
    for point in points:
        print(point, end=' ')
