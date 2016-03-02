# -*- coding: utf-8 -*-
"""
/***************************************************************************
 RasterLoaderDialog
                                 A QGIS plugin
 Loads rasters from a location given in a shapefile column
                             -------------------
        begin                : 2016-03-02
        git sha              : $Format:%H$
        copyright            : (C) 2016 by Lukas Krieger
        email                : lukaskrieger@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt4 import QtGui, uic

from qgis.core import *
import qgis

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'raster_loader_dialog_base.ui'))


class RasterLoaderDialog(QtGui.QDialog, FORM_CLASS):

    paths = []
    names = []

    def __init__(self, parent=None):
        """Constructor."""
        super(RasterLoaderDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

        
        self.comboBoxLabel.setText('Choose field name to be used as raster loading path:')
        self.comboBoxNameLabel.setText('Choose field name to be used as name for loaded rasters:')
        self.lineEditLabel.setText('If applicable, chose an extension to appended to each field name:')
        self.additionalNameLabel.setText('If applicable, chose an extension name for raster:')
        
        self.descriptionLabel.setText('A sample path of rasters that will be loaded looks like this:')
        self.descriptionName.setText('With name:')

        #Fill the combo box with possible field values
        shapeLayer = qgis.utils.iface.activeLayer()
        if shapeLayer is None or shapeLayer.type() != QgsMapLayer.VectorLayer:
            print "Wrong layer in dialog"
            return
        prov = shapeLayer.dataProvider()
        self.comboBox.addItem('')
        self.comboBoxNames.addItem('')
        for field in prov.fields():
            self.comboBox.addItem(field.name())
            self.comboBoxNames.addItem(field.name())


        #Call on comboBox change
        self.comboBox.currentIndexChanged.connect(self.updatePaths)
        self.comboBoxNames.currentIndexChanged.connect(self.updatePaths)
        #Call on comboBox change
        self.lineEdit.textChanged.connect(self.updatePaths)
        self.lineEditNames.textChanged.connect(self.updatePaths)

        self.updatePaths()



    def updatePaths(self):

        #Clear list
        self.paths = []
        self.names = []

        shapeLayer = qgis.utils.iface.activeLayer()
        prov = shapeLayer.dataProvider()
        features = prov.getFeatures()
        
        fieldPath = self.comboBox.currentText()
        additionalPath = self.lineEdit.text()
        
        fieldName = self.comboBoxNames.currentText()
        additionalName = self.lineEditNames.text()
        
        for feat in features:
            
            path = ''
            if not fieldPath == '':
                path = str(feat.attribute(fieldPath))
            path = path+str(additionalPath)
            
            name = ''
            if not fieldName == '':
                name = str(feat.attribute(fieldName))
            name = name+str(additionalName)

            self.paths.append(path)
            self.names.append(name)
            
        if len(self.paths) > 0:
            self.exampleLabel.setText(self.paths[0])
        else:
            self.exampleLabel.setText('')
        
        if len(self.names) > 0:
            self.exampleName.setText(self.names[0])
        else:
            self.exampleName.setText('')

    def accept(self):
        if len(self.paths) == len(self.names):
            for i in range(len(self.paths)):
                path = self.paths[i]
                name = self.names[i]

                rlayer = QgsRasterLayer(path, name)
                if not rlayer.isValid():
                    print "Path: ", path, "failed to load."
                else:
                    QgsMapLayerRegistry.instance().addMapLayer(rlayer)

