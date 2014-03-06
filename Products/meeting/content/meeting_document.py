# -*- coding: utf-8 -*-
#
# File: meeting_document.py
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

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope import interface
from Products.ATContentTypes.content.file import ATFile
from Products.meeting.interfaces.meeting_document import IMeetingDocument
from Products.meeting.config import *

# additional imports from tagged value 'import'
from Products.ATVocabularyManager.namedvocabulary import NamedVocabulary

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='type',
        widget=SelectionWidget(
            label="Document Type (e.g. working paper)",
            description="Choose the type that applies",
            label_msgid='meeting_label_type',
            description_msgid='meeting_help_type',
            i18n_domain='meeting',
        ),
        vocabulary=NamedVocabulary("""document_types"""),
        searchable=1
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

MeetingDocument_schema = getattr(ATFile, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class MeetingDocument(ATFile):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(ATFile,'__implements__',()),)
    # zope3 interfaces
    interface.implements(IMeetingDocument)

    # This name appears in the 'add' box
    archetype_name = 'Meeting Document'

    meta_type = 'MeetingDocument'
    portal_type = 'MeetingDocument'
    allowed_content_types = [] + list(getattr(ATFile, 'allowed_content_types', []))
    filter_content_types = 0
    global_allow = 1
    content_icon = 'meetingdocument.png'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "Meeting Document"
    typeDescMsgId = 'description_edit_meetingdocument'

    _at_rename_after_creation = True

    schema = MeetingDocument_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(MeetingDocument, PROJECTNAME)
# end of class MeetingDocument

##code-section module-footer #fill in your manual code here
##/code-section module-footer



