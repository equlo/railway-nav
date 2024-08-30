import heapq

# Example graph representation (node, edges with distances)
graph = {
    'Ticket Counter': {'Platform 1': 1, 'Restroom': 3},
    'Platform 1': {'Ticket Counter': 1, 'Platform 2': 2},
    'Platform 2': {'Platform 1': 2, 'Food Court': 1},
    'Restroom': {'Ticket Counter': 3, 'Food Court': 2},
    'Food Court': {'Platform 2': 1, 'Restroom': 2}
}

def get_shortest_path(start, end):
    queue = [(0, start)]
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    previous_nodes = {vertex: None for vertex in graph}

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_vertex
                heapq.heappush(queue, (distance, neighbor))

    path, current_vertex = [], end
    while previous_nodes[current_vertex] is not None:
        path.append(current_vertex)
        current_vertex = previous_nodes[current_vertex]
    if path:
        path.append(start)
    path.reverse()

    return path, distances[end]
