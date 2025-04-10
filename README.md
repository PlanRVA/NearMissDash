# NearMiss

Hi! Welcome to the Regional Near Miss Dashboard GitHub page. The NM Dashboard is made and managed by **PlanRVA**. 
Live Dashboard Page: https://nearmissrva.onrender.com/

# Unfiled Items
- app1.ipynb : This is the python file to run the app locally.
- appy.py : This is the python file to run on Render/on a server.
- LICENSE : MIT License. 
- .gitattributes : Unsure.
- pyenv.cfg : Unsure.
- requirements.txt : Libraries needed to run on a server.
- checkboxdict.txt : what the checkbox selection in the app means.
- bokeh1.py, bokeh2.py, plot1.html and plot2.html are for making plots on the dashboard page.
- README.md : Yer lookin' at it.
# Files
Within the NM folders, there are:
- Include : Unsure.
- _pyache_ : compiled python files.
- json : The GeoJSON of events is in this folder, events.geojson. 
- Lib : Necessary libraries.
- scripts : Python scripts to handle venv, activate, and the original scripts for creating the GeoJSON and SQL, and pip. The update.events.ipynb will pull the JSONBIN.io API and update a geoJSON locally. The create.sql.ipynb can then be used to overwrite the SQL file to update it.
- sql : An SQL Source File of the events recorded in the app.
- static : Images used on the site and the stylesheet.
- templates : HTML pages used on the site (about, apphome, contact, dashboard, defs) and a dump.html for TBD bits of code.

To make a Near Miss Dash - 
-branch project.
-change file paths.
-make config.js file with your api keys to store the json data.
-change where map is centered and change initial map icon placement in the apphome.html.
-change colors and logos.
-publish!
