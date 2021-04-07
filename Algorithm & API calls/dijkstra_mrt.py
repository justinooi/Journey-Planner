import sys
import json
import pprint
from datetime import datetime, timedelta
import math
import heapq

def dijkstra_mrt(start, end):

    result_array = []

    current_time = int(1200)
    cost_per_stop = float(10)
    cost_per_transfer = float(50) #simulate inconvinience to change buses
    print ("Loading Transport Data...\n")

    stops = json.loads(open("mrtstops.json").read())
    routes = json.loads(open("mrtroute.json").read())

    print ("Initializing  tables...\n")
    stop_desc_map = {stop["Description"]: stop for stop in stops}
    stop_code_map = {stop["MRTCode"]: stop for stop in stops}

    routes_map = {}

    for route in routes:

        key = (route["ServiceNo"], route["Direction"])
        if key not in routes_map:
            routes_map[key] = []
        # hack around broken data
        if (route["StopSequence"] == 4
                and route["Distance"] == 9.1
                and key == ("34", 1)):
            route["StopSequence"] = 14
        routes_map[key] += [route]

    print ("Initializing Graph...\n")
    graph = {}
    for service, path in routes_map.items():
        # hack around broken data
        path.sort(key = lambda r: r["StopSequence"])
        for route_index in range(len(path) - 1):
            key = path[route_index]["MRTCode"]
            if key not in graph:
                graph[key] = {}
            curr_route_stop = path[route_index]
            next_route_stop = path[route_index + 1]
            curr_distance = curr_route_stop["Distance"] or 0
            next_distance = next_route_stop["Distance"] or curr_distance
            distance = next_distance - curr_distance
            assert distance >= 0, (curr_route_stop, next_route_stop)
            curr_code = curr_route_stop["MRTCode"]
            next_code = next_route_stop["MRTCode"]
            graph[curr_code][(next_code, service)] = distance

    print ("Running Dijkstras Algorithm for MRT...\n")

    def dijkstras(graph, start, end):
        seen = set()
        # maintain a queue of paths
        queue = []
        # push the first path into the queue
        heapq.heappush(queue, (0, 0, 0, [(start, None)]))
        while queue:
            # get the first path from the queue
            (curr_cost, curr_distance, curr_transfers, path) = heapq.heappop(queue)
            # get the last node from the path
            (node, curr_service) = path[-1]
            # path found
            if node == end:
                return (curr_cost, curr_distance, curr_transfers, path)
            if (node, curr_service) in seen:
                continue
            seen.add((node, curr_service))
            # enumerate all adjacent nodes, construct a new path and push it into the queue
            for (adjacent, service), distance in graph.get(node, {}).items():
                new_path = list(path)
                new_path.append((adjacent, service))
                new_distance = curr_distance + distance
                new_cost = distance + curr_cost
                new_transfers = curr_transfers
            #If path service is not the same as initial service, add transfer cost to total trip
                if curr_service != service:
                    new_cost += cost_per_transfer
                    new_transfers += 1
                new_cost += cost_per_stop
                heapq.heappush(queue, (new_cost, new_distance, new_transfers, new_path))

    (cost, distance, transfers, path) = dijkstras(graph, stop_desc_map[start]["MRTCode"], stop_desc_map[end]["MRTCode"])

    for code, service in path:

        if service is None:
            service = (0, 0)

        latlng_tuple = (stop_code_map[code]["Latitude"], stop_code_map[code]["Longitude"])
        result_tuple = (latlng_tuple, service[0], stop_code_map[code]["Description"])
        result_array.append(result_tuple)

    time = (distance / 50) * 60

    result_list = [result_array, len(path)-1, distance, time, transfers - 1]

    return result_list
