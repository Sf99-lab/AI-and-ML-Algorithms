from random import randint

tsp = [
    [0, 400, 500, 300],
    [400, 0, 300, 500],
    [500, 300, 0, 400],
    [300, 500, 400, 0]
]


def random_tours(tsp):
    cities = list(range(len(tsp)))
    tours = []

    for _ in range(len(tsp)):
        i = randint(0, len(cities) - 1)
        rand_city = cities[i]
        tours.append(rand_city)
        cities.remove(rand_city)

    return tours


# tour:  1 0 3 2 (example)
#        B A D C
def len_of_tour(tsp, tour):
    length = 0

    for i in range(1, len(tour)):
        length += tsp[tour[i-1]][tour[i]]
    return length


def extract_neighbours(tour):
    neighbours = []

    for i in range(len(tour)):
        for j in range(i+1, len(tour)):
            neighbour = tour
            neighbour[i], neighbour[j] = tour[j], tour[i]
            neighbours.append(neighbour)

    return neighbours


def find_best_neighbour(tsp, neighbours):
    # get initial neighbour
    best_path_len = len_of_tour(tsp, neighbours[0])
    best_neighbour = neighbours[0]

    for n in neighbours:
        curr_len = len_of_tour(tsp, n)
        if curr_len < best_path_len:
            best_path_len = curr_len
            best_neighbour = n

    return best_neighbour, best_path_len


def basic_hill_climbing(tsp):
    tour = random_tours(tsp)
    tour_len = len_of_tour(tsp, tour)
    neighbours = extract_neighbours(tour)
    best_neighbour, best_path_len = find_best_neighbour(tsp, neighbours)

    while best_path_len < tour_len:
        tour = best_neighbour
        tour_len = best_path_len
        neighbours = extract_neighbours(tour)
        best_neighbour, best_path_len = find_best_neighbour(tsp, neighbours)

    return tour, tour_len


print(basic_hill_climbing(tsp))
