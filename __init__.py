# -*- coding: utf-8 -*-
"""
/***************************************************************************
 QLtop
                                 A QGIS plugin
 Outil interactif de préanalyse pour le logiciel LTOP
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-09-25
        git sha              : $Format:%H$
        copyright            : (C) 2020 by HEIG-VD | Nicolas Szakacs
        email                : nicolas.szakacs@heig-vd.ch
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; Version 3 of the License                *
 *                                                                         *
 ***************************************************************************/

 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load QLtop class from file QLtop.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .qltop import QLtop
    return QLtop(iface)
