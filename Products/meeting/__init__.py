# -*- coding: utf-8 -*-
#
# File: meeting.py
#
# Copyright (c) 2007 by []
# Generator: ArchGenXML Version 1.6.0-beta-svn
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#

__author__ = """David Bain <david.bain@alteroo.com>"""
__docformat__ = 'plaintext'


# There are three ways to inject custom code here:
#
#   - To set global configuration variables, create a file AppConfig.py.
#       This will be imported in config.py, which in turn is imported in
#       each generated class and in this file.
#   - To perform custom initialisation after types have been registered,
#       use the protected code section at the bottom of initialize().

import logging
logger = logging.getLogger('meeting')
logger.debug('Installing Product')

import Products.CMFPlone.interfaces
import os
import os.path
from Globals import package_home
from Products.Archetypes import listTypes
from Products.Archetypes.atapi import *
from Products.Archetypes.utils import capitalize
from Products.CMFCore import DirectoryView
from Products.CMFCore import permissions as cmfpermissions
from Products.CMFCore import utils as cmfutils
from Products.CMFPlone.utils import ToolInit
from Products.GenericSetup import EXTENSION
from Products.GenericSetup import profile_registry
from config import *

DirectoryView.registerDirectory('skins', product_globals)
DirectoryView.registerDirectory('skins/meeting',
                                    product_globals)

##code-section custom-init-head #fill in your manual code here
##/code-section custom-init-head


def initialize(context):
    ##code-section custom-init-top #fill in your manual code here
    ##/code-section custom-init-top

    # imports packages and types for registration
    import interfaces
    import content
    import browser


    # Initialize portal content
    all_content_types, all_constructors, all_ftis = process_types(
        listTypes(PROJECTNAME),
        PROJECTNAME)

    cmfutils.ContentInit(
        PROJECTNAME + ' Content',
        content_types      = all_content_types,
        permission         = DEFAULT_ADD_CONTENT_PERMISSION,
        extra_constructors = all_constructors,
        fti                = all_ftis,
        ).initialize(context)

    # Give it some extra permissions to control them on a per class limit
    for i in range(0,len(all_content_types)):
        klassname=all_content_types[i].__name__
        if not klassname in ADD_CONTENT_PERMISSIONS:
            continue

        context.registerClass(meta_type   = all_ftis[i]['meta_type'],
                              constructors= (all_constructors[i],),
                              permission  = ADD_CONTENT_PERMISSIONS[klassname])

    profile_registry.registerProfile(
        name='default',
        title=PROJECTNAME,
        description='Profile for meeting',
        path='profiles/default',
        product='meeting',
        profile_type=EXTENSION,
        for_=Products.CMFPlone.interfaces.IPloneSiteRoot)

    ##code-section custom-init-bottom #fill in your manual code here
    ##/code-section custom-init-bottom

