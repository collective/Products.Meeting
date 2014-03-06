# -*- coding: utf-8 -*-
#
# File: meeting_document_collection.py
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
from Products.ATContentTypes.content.link import ATLink
from Products.meeting.interfaces.meeting_document_collection import IMeetingDocumentCollection
from Products.meeting.config import *

# additional imports from tagged value 'import'
from Products.ATVocabularyManager.namedvocabulary import NamedVocabulary
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import *
from Products.AddRemoveWidget.AddRemoveWidget import AddRemoveWidget
from Products.OrderableReferenceField import  OrderableReferenceField, OrderableReferenceWidget
from Products.DataGridField import DataGridField, DataGridWidget
from Products.DataGridField.Column import Column
from Products.DataGridField.SelectColumn import SelectColumn

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

   OrderableReferenceField(
        name='source_documents',
        index="FieldIndex:brains",
        widget=AddRemoveWidget
        (
            label="Source Documents",
            description="Documents in this collection",
            label_msgid='meeting_label_source_documents',
            description_msgid='meeting_help_source_documents',
            i18n_domain='meeting',
        ),
        allowed_types=['File','MeetingDocument','ReflectoFile'],
        multiValued=1,
        relationship="meeting_document",
        searchable=1,
        required=1
    ),

    StringField(
        name='title',
        widget=StringWidget(
            label="Collection Name",
            description="The title for this collection of documents",
            label_msgid='meeting_label_title',
            description_msgid='meeting_help_title',
            i18n_domain='meeting',
        ),
        searchable=1
    ),

    DataGridField(
        name='documents',
        index="FieldIndex:brains",
        widget=DataGridWidget
        (
            label="Meeting Documents",
            description="A Table of documents, including the document code and the link to the document in en,es and fr",
            columns={'document':Column('Document Code'),'english':SelectColumn('English',vocabulary='getDocs'),'spanish':SelectColumn('Spanish',vocabulary='getDocs'),'french':SelectColumn('French',vocabulary='getDocs')},
            label_msgid='meeting_label_documents',
            description_msgid='meeting_help_documents',
            i18n_domain='meeting',
        ),
        schemata="Documents",
        columns=("document","english","spanish","french"),
        searchable=1
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

MeetingDocumentCollection_schema = getattr(ATLink, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
MeetingDocumentCollection_schema['description'].required = 0
MeetingDocumentCollection_schema['description'].widget.visible = {"edit": "invisible", "view": "invisible"}
MeetingDocumentCollection_schema['remoteUrl'].required = 0
MeetingDocumentCollection_schema['remoteUrl'].widget.visible = {"edit": "invisible", "view": "invisible"}
MeetingDocumentCollection_schema['relatedItems'].required = 0
MeetingDocumentCollection_schema['relatedItems'].widget.visible = {"edit": "invisible", "view": "invisible"}
##/code-section after-schema

class MeetingDocumentCollection(ATLink):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(ATLink,'__implements__',()),)
    # zope3 interfaces
    interface.implements(IMeetingDocumentCollection)

    # This name appears in the 'add' box
    archetype_name = 'Meeting Document Collection'

    meta_type = 'MeetingDocumentCollection'
    portal_type = 'MeetingDocumentCollection'
    allowed_content_types = [] + list(getattr(ATLink, 'allowed_content_types', []))
    filter_content_types = 0
    global_allow = 0
    content_icon = 'meetingdocumentcollection.png'
    immediate_view = 'base_view'
    default_view = 'meeting_summary'
    suppl_views = ()
    typeDescription = "Meeting Document Collection"
    typeDescMsgId = 'description_edit_meetingdocumentcollection'

    _at_rename_after_creation = True

    schema = MeetingDocumentCollection_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    security.declarePublic('getDocs')
    def getDocs(self):
        """Returns a list of the available Documents
        """
        source_docs = self.getSource_documents()
        source_doc_list = [(doc.UID(),doc.Title(),)  for doc in source_docs]
        source_doc_list.insert(0, ('none',u'none'))
        return DisplayList(tuple(source_doc_list))


registerType(MeetingDocumentCollection, PROJECTNAME)
# end of class MeetingDocumentCollection

##code-section module-footer #fill in your manual code here
##/code-section module-footer



