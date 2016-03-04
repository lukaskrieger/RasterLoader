# RasterLoader
Qgis plugin for loading raster files from locations specified in vector data.

##Scenario
A possible scenario is that different raster data exists in a folder structure at your harddrive. Additionally, Vector data (e.g. from a PostGIS) database is available, that contains the additional description of this raster data (e.g. date, processing_date, sensor, path_to_file...). This plugin makes it possible that a query is run on the vector data returning only the items of interest. Afterwards, the raster_data of interest can be loaded by loading all rasters from the vector datas *path_to_file* field.

##Usage
Select the vector data layer that contains a field pointing to your raster data (e.g. path_to_file) and then click on the RasterLoader button. The raster loader is located in the Plugins submenu
