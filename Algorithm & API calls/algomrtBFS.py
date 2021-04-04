import sys
import json
import pprint

start = input("Enter your starting MRT station :\n")
end = input("Enter your ending MRT station \n")
current_time = int(1200)
cost_per_stop = float(10)
cost_per_transfer = float(200)
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
    # hack around broken data
    if (route["StopSequence"] == 4
            and route["Distance"] == 9.1
            and key == ("34", 1)):
        route["StopSequence"] = 14
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
def find_service(i):
    for (service, direction), route in routes_map.items():
        for j in range(len(route)-1):
            if path[i] == route[j]["MRTCode"] and path[i+1] == route[j+1]["MRTCode"]:
                return (
                	service, 
                	stop_code_map[path[i]]["Description"],
                	stop_code_map[path[i + 1]]["Description"]
            	)

for i in range(len(path) - 1):
    print (find_service(i))
print (len(path), "stops")