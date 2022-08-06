# дз 6 задача про планеты

def find_farthest_orbit(arr):
    return [i for i in arr if i[0] * i[1] == max([i[0] * i[1] for i in arr if i[0] != i[1]])]


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
