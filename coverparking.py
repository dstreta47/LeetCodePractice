#Cover parking

import sys

def min_roof_length(parking_spots, k):
    # Input validations...
    # what if k > len(parking_spots)?
    if not parking_spots or k == 0: return 0
    if k > len(parking_spots): return sys.maxsize

    parking_spots.sort()
    ans = sys.maxsize
    for i in range(0, len(parking_spots) - k + 1):
        p1 = parking_spots[i + k - 1]
        p2 = parking_spots[i]
        ans = min(ans, parking_spots[i + k - 1] - parking_spots[i] + 1)
    return ans

print(min_roof_length([12, 6, 5, 2],3))
