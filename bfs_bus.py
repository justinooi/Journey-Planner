import sys
import json
import pprint

def bfs_bus(start, end):

    result_array = []

    print ("Loading Transport Data...\n")

    stops = json.loads(open("busstops.json").read())
    routes = json.loads(open("routes.json").read())

    print ("Initializing  tables...\n")
    stop_desc_map = {stop["Description"]: stop for stop in stops}
    stop_code_map = {stop["BusStopCode"]: stop for stop in stops}
    routes_map = {}

    for route in routes:
        key = (route["ServiceNo"], route["Direction"])
        if key not in routes_map:
            routes_map[key] = []
        routes_map[key] += [route]

    print ("Initializing Graph...\n")
    graph = {}
    for service, path in routes_map.items():
        for route_index in range(len(path) - 1):
            key = path[route_index]["BusStopCode"]
            if key not in graph:
                graph[key] = set()
            graph[path[route_index]["BusStopCode"]].add(path[route_index + 1]["BusStopCode"])

    print ("Running BFS....\n")

    def bfs(graph, start, end):
        # maintain a queue of paths
        from queue import Queue
        seen=set()
        queue = Queue()
        # push the first path into the queue
        queue.put([start])
        while queue:
            # gets first path from queue
            path = queue.get()
            # gets last node from the path
            node = path[-1]
            # path found
            if node == end:
                return path
            # if node has been visited before: add to seen
            if node in seen:
                continue
            seen.add(node)
            # adds in all adjacent nodes, construct a new path and push it into the queue
            for adjacent in graph.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.put(new_path)

    path = bfs(graph, stop_desc_map[start]["BusStopCode"], stop_desc_map[end]["BusStopCode"])

    def get_path(i):
        for (service, direction), route in routes_map.items():
            for j in range(len(route) - 1):
                if path[i] == route[j]["BusStopCode"]:
                    if stop_code_map[path[i]]["Latitude"] == 0 and stop_code_map[path[i]]["Longitude"] == 0:
                        return None
                    return (
                        (stop_code_map[path[i]]["Latitude"], stop_code_map[path[i]]["Longitude"]),
                        service,
                        stop_code_map[path[i]]["Description"]
                    )

    def find_service(i):
        for (service, direction), route in routes_map.items():
            for j in range(len(route) - 1):
                if path[i] == route[j]["BusStopCode"] and path[i + 1] == route[j + 1]["BusStopCode"]:
                    return (
                        service
                    )

    transfer_counter = 0

    for i in range(len(path) - 1):
        past_service = None
        if i > 0:
            past_service = find_service(i - 1)
        service = find_service(i)

        if service is not past_service and past_service is not None:
            transfer_counter += 1

    for i in range(len(path)):
        if get_path(i) is None:
            continue
        else:
            result_array.append(get_path(i))

    print(len(path))
    result_list = [result_array, len(path) - 1, transfer_counter]

    return result_list
