import folium

# m = folium.Map()
m = folium.Map(location=(22.6273, 120.3014), zoom_start=16)

m.save("docs/index.html")

