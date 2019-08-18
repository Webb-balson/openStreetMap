import folium

map = folium.Map(location = [12.901712,77.631244], zoom_start=15)

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[12.901712,77.631244], popup="Hi I am a Marker", icon=folium.Icon(color='green')))
map.add_child(fg)

map.save("Oxford.html")
