# import libraries
import json
import pandas as pd
import plotly.express as px

#load the geoJSON file
uk_con = json.load(open("west.geojson", 'r'))

# select which property to make the index
print(uk_con["features"][0]["properties"])

# set index to match constituency codes with the coordinates 
con_id_map = {}
for feature in uk_con['features']:
  feature['id'] = feature['properties']['PCON20CD']
  con_id_map[feature['properties']['PCON20NM']] = feature['id']

# load excel file with data and assign index
df=pd.read_csv("final (1).csv")
df['id'] = df['name'].apply(lambda x: con_id_map[x])
df.head()

# create map with slider
fig = px.choropleth_mapbox(df, locations='id', geojson=uk_con, 
                           color='lab_voter %', hover_name="name", 
                           mapbox_style="carto-positron", animation_frame="YEAR", 
                           animation_group="id", zoom=4, center = {"lat": 55, "lon": 0})
fig.update_layout(width=800,
    height=900,
    autosize=False,
    margin=dict(t=0, b=0, l=0, r=0))
fig.show()

# generate html file to upload on github and then embed
import plotly.io as pio
pio.write_html(fig, file='LABOUR MAP.html', auto_open=True)
