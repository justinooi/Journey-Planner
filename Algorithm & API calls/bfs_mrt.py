import sys
import json
import pprint

def bfs_mrt(start, end):

    result_array = []

    print ("Loading Transport Data...\n")

    stops = json.loads(open("mrtstops.json").read())
    routes = json.loads(open("mrtroute.json").read())

    print ("Initializing  tables..,\n")
    stop_desc_map = {stop["Description"]: stop for stop in stops}
    stop_code_map = {stop["MRTCode"]: stop for stop in stops}
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
            key = path[route_index]["MRTCode"]
            if key not in graph:
                graph[key] = set()
            graph[path[route_index]["MRTCode"]].add(path[route_index + 1]["MRTCode"])

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

    path = bfs(graph, stop_desc_map[start]["MRTCode"], stop_desc_map[end]["MRTCode"])

    def get_path(i):
        for (service, direction), route in routes_map.items():
            for j in range(len(route)-1):
                if path[i] == route[j]["MRTCode"]:
                    return (
                        (stop_code_map[path[i]]["Latitude"], stop_code_map[path[i]]["Longitude"]),
                        service,
                        stop_code_map[path[i]]["Description"]
                    )

    def find_service(i):
        for (service, direction), route in routes_map.items():
            for j in range(len(route) - 1):
                if path[i] == route[j]["MRTCode"] and path[i+1] == route[j+1]["MRTCode"]:
                    return (
                        service
                    )

    transfer_counter = 0

    if len(path) is None:
        path.append('0')

    for i in range(len(path)-1):
        past_service = None
        if i > 0:
            past_service = find_service(i - 1)
        service = find_service(i)
        if service == "CC-MRT" and past_service == "CE-MRT":
            pass
        elif service is not past_service and past_service is not None:
            transfer_counter += 1

    for i in range(len(path)):
        result_array.append(get_path(i))

    result_list = [result_array, len(path)-1, transfer_counter]
    print(result_list)
    return result_list