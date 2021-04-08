import folium
from folium import features
from dijkstra_bus import dijkstra_bus
from bfs_bus import bfs_bus
from dijkstra_mrt import dijkstra_mrt
from bfs_mrt import bfs_mrt


class plot_graph:
    # default map to show when nothing is plotted
    def default(self):
        default = folium.Map(location=[1.3521, 103.8198], tiles='CartoDB positron', prefer_canvas=True)
        folium.Marker(location=[1.3774, 103.8488], popup='SIT@NYP',
                      icon=folium.Icon(color='red', icon='fa-school', prefix='fa')).add_to(default)
        default.save('default.html')

    # dijkstras bus
    def bus_dijs(self, start, end):
        latlng = []
        # call algo function
        result_list = dijkstra_bus(start, end)
        # get lat long stored as a list of tuples
        for i in range(len(result_list[0])):
            latlng.append(result_list[0][i][0])
        # initialize map
        dij_bus = folium.Map(location=[1.3521, 103.8198], tiles='CartoDB positron', prefer_canvas=True)
        # plotting points and drawing lines
        for i in range(len(result_list[0])):
            # indicate start of route
            if i == 0:
                folium.Marker(location=[latlng[i][0], latlng[i][1]],
                              popup=str(result_list[0][i][1]) + '\n' + str(result_list[0][i][2]),
                              color='red', icon=folium.Icon(color='red', icon='info-sign'), radius=8).add_to(dij_bus)
                folium.PolyLine(locations=latlng).add_to(dij_bus)
            # indicate end of route
            elif i == len(result_list[0]) - 1:
                folium.Marker(location=[latlng[i][0], latlng[i][1]],
                              popup=str(result_list[0][i][1]) + '\n' + str(result_list[0][i][2]),
                              color='green', icon=folium.Icon(color='green', icon='info-sign'), radius=8).add_to(
                    dij_bus)
                folium.PolyLine(locations=latlng).add_to(dij_bus)
            else:
                folium.Marker(location=[latlng[i][0], latlng[i][1]],
                              popup=str(result_list[0][i][1]) + '\n' + str(result_list[0][i][2]), radius=8).add_to(
                    dij_bus)
                folium.PolyLine(locations=latlng).add_to(dij_bus)
        # save html
        dij_bus.save("dij_bus.html")

    # breadth first search for bus
    def bus_bfs(self, start, end):
        latlng = []
        # call algo function
        result_list = bfs_bus(start, end)
        # print(result_list)
        # get lat long stored as a list of tuples
        for i in range(len(result_list[0])):
            latlng.append(result_list[0][i][0])
        # initialize map
        bus_bfs = folium.Map(location=[1.3521, 103.8198], tiles='CartoDB positron', prefer_canvas=True)
        # plotting points and drawing line
        for i in range(len(result_list[0])):
            # indicate start of route
            if i == 0:
                folium.Marker(location=[latlng[i][0], latlng[i][1]],
                              popup=str(result_list[0][i][1]) + '\n' + str(result_list[0][i][2]),
                              color='red', icon=folium.Icon(color='red', icon='info-sign'), radius=8).add_to(bus_bfs)
                folium.PolyLine(locations=latlng).add_to(bus_bfs)
            # indicate end of route
            elif i == len(result_list[0]) - 1:
                folium.Marker(location=[latlng[i][0], latlng[i][1]],
                              popup=str(result_list[0][i][1]) + '\n' + str(result_list[0][i][2]),
                              color='green', icon=folium.Icon(color='green', icon='info-sign'), radius=8).add_to(
                    bus_bfs)
                folium.PolyLine(locations=latlng).add_to(bus_bfs)
            else:
                folium.Marker(location=[latlng[i][0], latlng[i][1]],
                              popup=str(result_list[0][i][1]) + '\n' + str(result_list[0][i][2]), radius=8).add_to(
                    bus_bfs)
                folium.PolyLine(locations=latlng).add_to(bus_bfs)
        # save html
        bus_bfs.save("bus_bfs.html")

    # dijkstras mrt
    def mrt_dijs(self, start, end):
        latlng = []
        # call algo function
        result_list = dijkstra_mrt(start, end)
        # get lat long stored as a list of tuples
        for i in range(len(result_list[0])):
            latlng.append(result_list[0][i][0])
        # initialize map
        dij_mrt = folium.Map(location=[1.3521, 103.8198], tiles='CartoDB positron', prefer_canvas=True)
        # plotting points and drawing line
        for i in range(len(result_list[0])):
            # indicate start of route
            if i == 0:
                folium.Marker(location=[latlng[i][0], latlng[i][1]],
                              popup=str(result_list[0][i][1]) + '\n' + str(result_list[0][i][2]),
                              color='red', icon=folium.Icon(color='red', icon='info-sign'), radius=8).add_to(dij_mrt)
                folium.PolyLine(locations=latlng).add_to(dij_mrt)
            # indicate end of route
            elif i == len(result_list[0]) - 1:
                folium.Marker(location=[latlng[i][0], latlng[i][1]],
                              popup=str(result_list[0][i][1]) + '\n' + str(result_list[0][i][2]),
                              color='green', icon=folium.Icon(color='green', icon='info-sign'), radius=8).add_to(
                    dij_mrt)
                folium.PolyLine(locations=latlng).add_to(dij_mrt)
            # plot the marker colour base on the colour of the MRT line
            elif result_list[0][i][1] == 'NS-MRT':
                folium.Marker(location=[latlng[i][0], latlng[i][1]],
                              popup=str(result_list[0][i][1]) + '\n' + str(result_list[0][i][2]),
                              icon=folium.Icon(color='red', icon='fa-train', prefix='fa'), radius=8).add_to(
                    dij_mrt)
                folium.PolyLine(locations=latlng).add_to(dij_mrt)
            elif result_list[0][i][1] == 'EW-MRT':
                folium.Marker(location=[latlng[i][0], latlng[i][1]],
                              popup=str(result_list[0][i][1]) + '\n' + str(result_list[0][i][2]),
                              icon=folium.Icon(color='green', icon='fa-train', prefix='fa'), radius=8).add_to(
                    dij_mrt)
                folium.PolyLine(locations=latlng).add_to(dij_mrt)
            elif result_list[0][i][1] == 'NE-MRT':
                folium.Marker(location=[latlng[i][0], latlng[i][1]],
                              popup=str(result_list[0][i][1]) + '\n' + str(result_list[0][i][2]),
                              icon=folium.Icon(color='purple', icon='fa-train', prefix='fa'), radius=8).add_to(
                    dij_mrt)
                folium.PolyLine(locations=latlng).add_to(dij_mrt)
            elif result_list[0][i][1] == 'CC-MRT':
                folium.Marker(location=[latlng[i][0], latlng[i][1]],
                              popup=str(result_list[0][i][1]) + '\n' + str(result_list[0][i][2]),
                              icon=folium.Icon(color='orange', icon='fa-train', prefix='fa'), radius=8).add_to(
                    dij_mrt)
                folium.PolyLine(locations=latlng).add_to(dij_mrt)
            elif result_list[0][i][1] == 'DT-MRT':
                folium.Marker(location=[latlng[i][0], latlng[i][1]],
                              popup=str(result_list[0][i][1]) + '\n' + str(result_list[0][i][2]),
                              icon=folium.Icon(color='blue', icon='fa-train', prefix='fa'), radius=8).add_to(
                    dij_mrt)
                folium.PolyLine(locations=latlng).add_to(dij_mrt)
        # save html
        dij_mrt.save("dij_mrt.html")

    # breadth first search for mrt
    def mrt_bfs(self, start, end):
        latlng = []
        # call algo function
        result_list = bfs_mrt(start, end)
        # get lat long stored as a list of tuples
        for i in range(len(result_list[0])):
            latlng.append(result_list[0][i][0])
        # initialize map
        mrt_bfs = folium.Map(location=[1.3521, 103.8198], tiles='CartoDB positron', prefer_canvas=True)
        # plotting points and drawing line
        for i in range(len(result_list[0])):
            # indicate start of route
            if i == 0:
                folium.Marker(location=[latlng[i][0], latlng[i][1]],
                              popup=str(result_list[0][i][1]) + '\n' + str(result_list[0][i][2]),
                              color='red', icon=folium.Icon(color='red', icon='info-sign'), radius=8).add_to(mrt_bfs)
                folium.PolyLine(locations=latlng).add_to(mrt_bfs)
            # indicate end of route
            elif i == len(result_list[0]) - 1:
                folium.Marker(location=[latlng[i][0], latlng[i][1]],
                              popup=str(result_list[0][i][1]) + '\n' + str(result_list[0][i][2]),
                              color='green', icon=folium.Icon(color='green', icon='info-sign'), radius=8).add_to(
                    mrt_bfs)
                folium.PolyLine(locations=latlng).add_to(mrt_bfs)
            # plot the marker colour base on the colour of the MRT line
            elif result_list[0][i][1] == 'NS-MRT':
                folium.Marker(location=[latlng[i][0], latlng[i][1]],
                              popup=str(result_list[0][i][1]) + '\n' + str(result_list[0][i][2]),
                              icon=folium.Icon(color='red', icon='fa-train', prefix='fa'), radius=8).add_to(
                    mrt_bfs)
                folium.PolyLine(locations=latlng).add_to(mrt_bfs)
            elif result_list[0][i][1] == 'EW-MRT':
                folium.Marker(location=[latlng[i][0], latlng[i][1]],
                              popup=str(result_list[0][i][1]) + '\n' + str(result_list[0][i][2]),
                              icon=folium.Icon(color='green', icon='fa-train', prefix='fa'), radius=8).add_to(
                    mrt_bfs)
                folium.PolyLine(locations=latlng).add_to(mrt_bfs)
            elif result_list[0][i][1] == 'NE-MRT':
                folium.Marker(location=[latlng[i][0], latlng[i][1]],
                              popup=str(result_list[0][i][1]) + '\n' + str(result_list[0][i][2]),
                              icon=folium.Icon(color='purple', icon='fa-train', prefix='fa'), radius=8).add_to(
                    mrt_bfs)
                folium.PolyLine(locations=latlng).add_to(mrt_bfs)
            elif result_list[0][i][1] == 'CC-MRT':
                folium.Marker(location=[latlng[i][0], latlng[i][1]],
                              popup=str(result_list[0][i][1]) + '\n' + str(result_list[0][i][2]),
                              icon=folium.Icon(color='orange', icon='fa-train', prefix='fa'), radius=8).add_to(
                    mrt_bfs)
                folium.PolyLine(locations=latlng).add_to(mrt_bfs)
            elif result_list[0][i][1] == 'DT-MRT':
                folium.Marker(location=[latlng[i][0], latlng[i][1]],
                              popup=str(result_list[0][i][1]) + '\n' + str(result_list[0][i][2]),
                              icon=folium.Icon(color='lightblue', icon='fa-train', prefix='fa'), radius=8).add_to(
                    mrt_bfs)
                folium.PolyLine(locations=latlng).add_to(mrt_bfs)
        # save html
        mrt_bfs.save("mrt_bfs.html")