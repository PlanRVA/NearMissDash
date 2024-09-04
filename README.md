# NearMiss

Hi! Welcome to the Regional Near Miss Dashboard GitHub page. The NM Dashboard is made and managed by **PlanRVA**. 

# Unfiled Items
- app1.ipynb : This is the main python file to run the app.
- LICENSE : MIT License. 
- .gitattributes : Unsure.
- pyenv.cfg : Unsure.
- README.md : Yer lookin' at it.
# Files
Within the NM folders, there are:
- Include : Unsure.
- json : The GeoJSON of events is in this folder, events.geojson. 
- Lib : Necessary libraries.
- scripts : Python scripts to handle venv, activate, and the original scripts for creating the GeoJSON and SQL, and pip. The update.events.ipynb will pull the JSONBIN.io API and update a geoJSON locally. The create.sql.ipynb can then be used to overwrite the SQL file to update it.
- sql : An SQL Source File of the events recorded in the app.
- static : Images used on the site and the stylesheet.
- templates : HTML pages used on the site (about, apphome, contact, dashboard, defs) and a dump.html for TBD bits of code.

To make a Near Miss Dash - 
-branch project.
-change file paths.
-change json api connection or otherwise.
-change Mapbox basemap to the desired basemap (current one is custom).
-change where map is centered and change initial map icon placement in the apphome.html.
-change colors and logos.
