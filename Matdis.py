import itertools
from geopy.distance import geodesic

# 1. Data Koordinat Lokasi di Kampus
locations = {
    "Rektorat UNTAD": (-0.8917, 119.8901),
    "Fakultas Teknik": (-0.8925, 119.8912),
    "Fakultas MIPA": (-0.8910, 119.8890),
    "Fakultas Ekonomi": (-0.8905, 119.8920)
}

nodes = list(locations.keys())

# 2. Membuat Matriks Jarak
distance_matrix = {}
for loc1 in nodes:
    distance_matrix[loc1] = {}
    for loc2 in nodes:
        if loc1 == loc2:
            distance_matrix[loc1][loc2] = 0
        else:
            dist = geodesic(locations[loc1], locations[loc2]).meters
            distance_matrix[loc1][loc2] = round(dist, 2)

# 3. Fungsi Utama Solver TSP
def solve_tsp(nodes, distance_matrix):
    start_node = nodes[0]
    other_nodes = nodes[1:]
    min_distance = float("inf")
    best_route = None

    for perm in itertools.permutations(other_nodes):
        current_route = [start_node] + list(perm) + [start_node]
        current_distance = 0

        for i in range(len(current_route) - 1):
            u = current_route[i]
            v = current_route[i + 1]
            current_distance += distance_matrix[u][v]

        if current_distance < min_distance:
            min_distance = current_distance
            best_route = current_route

    return best_route, min_distance

# 4. Bagian Eksekusi Utama (Tombol Start)
if __name__ == "__main__":
    rute_terbaik, jarak_minimum = solve_tsp(nodes, distance_matrix)
    
    print("Rute Terpendek:")
    for halte in rute_terbaik:
        print(f" -> {halte}")
    print(f"\nTotal Jarak Keseluruhan: {jarak_minimum} meter")
