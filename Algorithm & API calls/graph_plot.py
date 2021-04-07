import folium
from folium import features
from dijkstra_bus import dijkstra_bus
from bfs_bus import bfs_bus
from dijkstra_mrt import dijkstra_mrt
from bfs_mrt import bfs_mrt


class plot_graph:

    def bus_dijs(self, start, end):
        latlng = []
        result_list = dijkstra_bus(start, end)
        for i in range(len(result_list[0])):
                latlng.append(result_list[0][i][0])

        dij_bus = folium.Map(location=[1.3521, 103.8198], tiles='CartoDB positron', prefer_canvas=True)

        for i in range(len(result_list[0])):
            if i == 0:
                folium.Marker(location=[latlng[i][0], latlng[i][1]], popup=str(result_list[0][i][1])+'\n'+str(result_list[0][i][2]),
                              color='red', icon=folium.Icon(color='red', icon='info-sign'), radius=8).add_to(dij_bus)
                folium.PolyLine(locations=latlng).add_to(dij_bus)
            elif i == len(result_list[0]) - 1:
                folium.Marker(location=[latlng[i][0], latlng[i][1]], popup=str(result_list[0][i][1])+'\n'+str(result_list[0][i][2]),
                              color='green', icon=folium.Icon(color='green', icon='info-sign'), radius=8).add_to(
                    dij_bus)
                folium.PolyLine(locations=latlng).add_to(dij_bus)
            else:
                folium.Marker(location=[latlng[i][0], latlng[i][1]], popup=str(result_list[0][i][1])+'\n'+str(result_list[0][i][2]), radius=8).add_to(
                    dij_bus)
                folium.PolyLine(locations=latlng).add_to(dij_bus)
        dij_bus.save("dij_bus.html")

    def bus_bfs(self, start, end):
        latlng = []
        result_list = bfs_bus(start, end)
        print(result_list)
        for i in range(len(result_list[0])):
                latlng.append(result_list[0][i][0])

        bus_bfs = folium.Map(location=[1.3521, 103.8198], tiles='CartoDB positron', prefer_canvas=True)

        for i in range(len(result_list[0])):
            if i == 0:
                folium.Marker(location=[latlng[i][0], latlng[i][1]], popup=str(result_list[0][i][1])+'\n'+str(result_list[0][i][2]),
                              color='red', icon=folium.Icon(color='red', icon='info-sign'), radius=8).add_to(bus_bfs)
                folium.PolyLine(locations=latlng).add_to(bus_bfs)
            elif i == len(result_list[0]) - 1:
                folium.Marker(location=[latlng[i][0], latlng[i][1]], popup=str(result_list[0][i][1])+'\n'+str(result_list[0][i][2]),
                              color='green', icon=folium.Icon(color='green', icon='info-sign'), radius=8).add_to(
                    bus_bfs)
                folium.PolyLine(locations=latlng).add_to(bus_bfs)
            else:
                folium.Marker(location=[latlng[i][0], latlng[i][1]], popup=str(result_list[0][i][1])+'\n'+str(result_list[0][i][2]), radius=8).add_to(
                    bus_bfs)
                folium.PolyLine(locations=latlng).add_to(bus_bfs)
        bus_bfs.save("bus_bfs.html")

    def mrt_dijs(self, start, end):
        latlng = []
        result_list = bfs_mrt(start, end)
        # print(result_list)
        for i in range(len(result_list[0])):
            latlng.append(result_list[0][i][0])

        dij_mrt = folium.Map(location=[1.3521, 103.8198], tiles='CartoDB positron', prefer_canvas=True)

        for i in range(len(result_list[0])):
            if i == 0:
                folium.Marker(location=[latlng[i][0], latlng[i][1]], popup=str(result_list[0][i][1])+'\n'+str(result_list[0][i][2]),
                              color='red', icon=folium.Icon(color='red', icon='info-sign'), radius=8).add_to(dij_mrt)
                folium.PolyLine(locations=latlng).add_to(dij_mrt)
            elif i == len(result_list[0]) - 1:
                folium.Marker(location=[latlng[i][0], latlng[i][1]], popup=str(result_list[0][i][1])+'\n'+str(result_list[0][i][2]),
                              color='green', icon=folium.Icon(color='green', icon='info-sign'), radius=8).add_to(
                    dij_mrt)
                folium.PolyLine(locations=latlng).add_to(dij_mrt)
            else:
                folium.Marker(location=[latlng[i][0], latlng[i][1]], popup=str(result_list[0][i][1])+'\n'+str(result_list[0][i][2]), radius=8).add_to(
                    dij_mrt)
                folium.PolyLine(locations=latlng).add_to(dij_mrt)
        dij_mrt.save("dij_mrt.html")

    def mrt_bfs(self, start, end):
        latlng = []
        result_list = bfs_mrt(start, end)
        # print(result_list)
        for i in range(len(result_list[0])):
            latlng.append(result_list[0][i][0])

        mrt_bfs = folium.Map(location=[1.3521, 103.8198], tiles='CartoDB positron', prefer_canvas=True)

        for i in range(len(result_list[0])):
            if i == 0:
                folium.Marker(location=[latlng[i][0], latlng[i][1]], popup=str(result_list[0][i][1])+'\n'+str(result_list[0][i][2]),
                              color='red', icon=folium.Icon(color='red', icon='info-sign'), radius=8).add_to(mrt_bfs)
                folium.PolyLine(locations=latlng).add_to(mrt_bfs)
            elif i == len(result_list[0]) - 1:
                folium.Marker(location=[latlng[i][0], latlng[i][1]], popup=str(result_list[0][i][1])+'\n'+str(result_list[0][i][2]),
                              color='green', icon=folium.Icon(color='green', icon='info-sign'), radius=8).add_to(
                    mrt_bfs)
                folium.PolyLine(locations=latlng).add_to(mrt_bfs)
            else:
                folium.Marker(location=[latlng[i][0], latlng[i][1]], popup=str(result_list[0][i][1])+'\n'+str(result_list[0][i][2]), radius=8).add_to(
                    mrt_bfs)
                folium.PolyLine(locations=latlng).add_to(mrt_bfs)
        mrt_bfs.save("mrt_bfs.html")