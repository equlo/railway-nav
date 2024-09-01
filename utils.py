# StationApp/utils.py

import heapq

def dijkstra(graph, start, end):
    queue = []
    heapq.heappush(queue, (0, start))
    distances = {location: float('inf') for location in graph}
    distances[start] = 0
    previous_nodes = {location: None for location in graph}

    while queue:
        current_distance, current_location = heapq.heappop(queue)

        if current_distance > distances[current_location]:
            continue

        for neighbor, weight in graph[current_location]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_location
                heapq.heappush(queue, (distance, neighbor))

    path = []
    while end:
        path.insert(0, end)
        end = previous_nodes[end]

    return path, distances[path[-1]]
