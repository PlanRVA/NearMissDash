import requests
import pandas as pd
import json
from math import pi
from bokeh.plotting import figure, show, output_file, save
from bokeh.transform import cumsum
from bokeh.models import LabelSet, ColumnDataSource

output_file(r'C:\GreenGIS\NearMissDash\plot1.html')

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

# Custom colors for 'report_type' and 'event_type'
custom_colors = {
    'Collision': '#C84107',    
    'Near Miss': '#EE810E',     
    'Dangerous Location': '#FBB92C',
    }

#  Prepare data for pie chart 1
pie_data_1 = df.groupby('report_type').size().reset_index(name='value')
pie_data_1['angle'] = pie_data_1['value']/pie_data_1['value'].sum() * 2 * pi
pie_data_1['color'] = pie_data_1['report_type'].map(custom_colors)
pie_data_2['custom_label'] = ["Collision", "Near Miss", "Dangerous Location"]

# Pie chart 1
p1 = figure(height=300, title="Submissions by Report Type", toolbar_location="right",
            tools="hover, reset, save", tooltips="@report_type: @value", x_range=(-0.5, 1.0))

p1.wedge(x=0, y=1, radius=0.2,
         start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
         line_color="white", fill_color='color', legend_field='custom_label', source=pie_data_1)

p1.axis.axis_label = None
p1.axis.visible = False
p1.grid.grid_line_color = None

# Display
show(p1)
save(p1)