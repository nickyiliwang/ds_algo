import itertools


def shortedPathForAllPairs(graph):  # Floyd-Warshall
    n = len(graph)

    for step in range(n):
        for row in range(n):
            for col in range(n):

                if graph[row][col] > graph[row][step] + graph[step][col]:
                    graph[row][col] = graph[row][step] + graph[step][col]


def path(bunnies):
    print(bunnies)
    bunnies = [0] + bunnies + [-1]
    path_to_bunnies = []

    for i in range(len(bunnies) - 1):
        path_to_bunnies.append((bunnies[i], bunnies[i + 1]))

    return path_to_bunnies


def solution(times, time_limit):
    shortedPathForAllPairs(times)

    n = len(times)
    bunny_count = n - 2  # first row is "Start", last row is "Bulkhead"
    rescued_bunnies = []

    for bunny in range(n):
        if times[bunny][bunny] < 0:  # check the diagonal
            rescued_bunnies = [bunny for bunny in range(bunny_count)]
            return rescued_bunnies

    for bunny in reversed(range(bunny_count + 1)):

        for bunnies in itertools.permutations(range(1, bunny_count + 1), r=bunny):
            total_time = 0

            path_to_bunnies = path(list(bunnies))

            for start_time, end_time in path_to_bunnies:
                total_time += times[start_time][end_time]

            if total_time <= time_limit:
                rescued_bunnies = sorted(list(bunny - 1 for bunny in bunnies))
                return rescued_bunnies

    return rescued_bunnies


print(
    solution(
        [
            [0, 2, 2, 2, -1],
            [9, 0, 2, 2, -1],
            [9, 3, 0, 2, -1],
            [9, 3, 2, 0, -1],
            [9, 3, 2, 2, 0],
        ],
        1,
    )
)
