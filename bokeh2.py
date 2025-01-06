import requests
import pandas as pd
import json
from math import pi
from bokeh.plotting import figure, show, output_file, save
from bokeh.transform import cumsum
from bokeh.io import output_notebook, show

output_file(r'C:\GreenGIS\NearMissDash\plot2.html')

#Setup JSON BIN IO
JSONBIN_ACCESS_KEY = '$2a$10$J23yWei2a5JsxL9JkiWOXuZsgZ.qR/GRj74Jre.4i/Te3XjaT0A2y'
JSONBIN_API_URL = f'https://api.jsonbin.io/v3/b/66db5907acd3cb34a87f7d42' # BIN

# Fetching JSON from JSONBin API
headers = {
    'X-Master-Key': JSONBIN_ACCESS_KEY,
}

response = requests.get(JSONBIN_API_URL, headers=headers)

if response.status_code == 200:
    data = response.json()['record']  # Extract the record part from JSONBin data
else:
    print("Failed to fetch data from JSONBin", response.status_code)

features = [feature['properties'] for feature in data['features']]
df = pd.DataFrame(features)

custom_colors = {
    'Collision1': '#C84107',    
    'Collision2': '#E96830',      
    'Miss1': '#EE810E',     
    'Miss2': '#F9A64F',    
    'Unsafe': '#FBB92C'         
    }

# Filter out rows where 'report_type' is null
filtered_df = df[df['event_type'].notna()]
# Prepare data for pie chart 2
pie_data_2 = filtered_df.groupby('event_type').size().reset_index(name='value')
pie_data_2['angle'] = pie_data_2['value'] / pie_data_2['value'].sum() * 2 * pi
pie_data_2['color'] = pie_data_2['event_type'].map(custom_colors)
pie_data_2['custom_label'] = ["Collision with Stationary Object or Vehicle", "Collision with Moving Object or vehicle", "Near Miss with Stationary Object or Vehicle", "Near Miss with Moving Object or Vehicle", "Unsafe Condition or Location"]

# Pie chart 2: Based on 'event_type'
p2 = figure(height=250, title="Submissions by Event Type", toolbar_location="right",
            tools="hover, reset, save", tooltips="@event_type: @value", x_range=(-0.5, 1.0))

p2.wedge(x=-0.1, y=1, radius=0.25,
         start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
         line_color="white", fill_color='color', legend_field='custom_label', source=pie_data_2)

p2.axis.axis_label = None
p2.axis.visible = False
p2.grid.grid_line_color = None


# Display
show(p2)
save(p2)

print(pie_data_2)
