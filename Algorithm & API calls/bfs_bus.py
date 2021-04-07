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
        queue = []
        # push the first path into the queue
        queue.append([start])
        while queue:
            # get the first path from the queue
            path = queue.pop(0)
            # get the last node from the path
            node = path[-1]
            # path found
            if node == end:
                return path
            # enumerate all adjacent nodes, construct a new path and push it into the queue
            for adjacent in graph.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)

    path = bfs(graph, stop_desc_map[start]["BusStopCode"], stop_desc_map[end]["BusStopCode"])
    def find_service(i):
        for (service, direction), route in routes_map.items():
            for j in range(len(route)-1):
                if path[i] == route[j]["BusStopCode"] and path[i+1] == route[j+1]["BusStopCode"]:
                    return (
                        service,
                        stop_code_map[path[i]]["Description"],
                        stop_code_map[path[i + 1]]["Description"]
                    )

    for code in path:
        latlng_tuple = (stop_code_map[code]["Latitude"], stop_code_map[code]["Longitude"])
        result_tuple = (latlng_tuple, service[0], stop_code_map[code]["Description"])
        result_array.append(result_tuple)

    print(result_array)

    result_list = [result_array, len(path)-1, ]

    for i in range(len(path) - 1):
        print (find_service(i))
    print (len(path), "stops")