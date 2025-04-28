import streamlit as st
import leafmap.foliumap as leafmap

# Convert coordinates
lat = 30 + 11/60 + 44.9/3600
lon = 67 + 0/60 + 47.4/3600

# Create map
m = leafmap.Map(center=[lat, lon], zoom=15)
m.add_basemap('HYBRID')  # Satellite view with labels

# Add office marker
m.add_marker(
    location=[lat, lon],
    popup='Our Office<br>30°11\'44.9"N 67°00\'47.4"E',
    tooltip='Click for info',
    icon={'icon': 'building', 'iconColor': 'white', 'markerColor': 'red', 'prefix': 'fa'}
)

# Add drawing tools
m.add_draw_control()

# Display
st.title('Office Location with Interactive Map')
st.folium(m, width=800, height=600)