# -*- coding: utf-8 -*-
"""
/***************************************************************************
 RasterLoader
                                 A QGIS plugin
 Loads rasters from a location given in a shapefile column
                             -------------------
        begin                : 2016-03-02
        copyright            : (C) 2016 by Lukas Krieger
        email                : lukaskrieger@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load RasterLoader class from file RasterLoader.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .raster_loader import RasterLoader
    return RasterLoader(iface)
