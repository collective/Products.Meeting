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

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope import interface
from Products.ATContentTypes.content.folder import ATFolder
from Products.ATContentTypes.content.event import ATEvent
from Products.meeting.interfaces.meeting import IMeeting
from Products.meeting.config import *

# additional imports from tagged value 'import'
from Products.ATCountryWidget.Widget import CountryWidget, AreaWidget
from Products.ATVocabularyManager.namedvocabulary import NamedVocabulary
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import *
from archetypes.uploadreferencewidget.widget import UploadReferenceWidget

##code-section module-header #fill in your manual code here
try:
    from Products.LinguaPlone.public import *
except ImportError:
    # No multilingual support
    pass

from Products.meeting.Extensions.utils import document_types
##/code-section module-header

schema = Schema((

    StringField(
        name='title',
        widget=StringWidget(
            label="Meeting Name",
            description="The name or title of the meeting",
            label_msgid='meeting_label_title',
            description_msgid='meeting_help_title',
            i18n_domain='meeting',
        ),
        searchable=1
    ),

    StringField(
        name='country',
        widget=CountryWidget
        (
            label="Country where the event will be held",
            label_msgid='meeting_label_country',
            i18n_domain='meeting',
        ),
        languageIndependent=1,
        searchable=1
    ),

    StringField(
        name='location',
        widget=StringWidget(
            label='Location',
            label_msgid='meeting_label_location',
            i18n_domain='meeting',
        ),
        searchable=1
    ),

    StringField(
        name='type',
        widget=SelectionWidget(
            label="Meeting Type",
            description="The type of meeting",
            label_msgid='meeting_label_type',
            description_msgid='meeting_help_type',
            i18n_domain='meeting',
        ),
        languageIndependent=1,
        schemata="List of documents",
        vocabulary=NamedVocabulary("""meeting_types"""),
        searchable=1
    ),

    ReferenceField(
        name='list_of_documents',
        widget=UploadReferenceWidget
        (
            label="List of Documents",
            description="the list of documents for the meeting",
            label_msgid='meeting_label_list_of_documents',
            description_msgid='meeting_help_list_of_documents',
            i18n_domain='meeting',
        ),
        languageIndependent=1,
        schemata="List of documents",
        multiValued=True,
        relationship="list_of_documents",
        searchable=1
    ),

    ReferenceField(
        name='registration',
        widget=UploadReferenceWidget
        (
            label="Registration Form",
            description="Registration form and information for the meeting",
            label_msgid='meeting_label_registration',
            description_msgid='meeting_help_registration',
            i18n_domain='meeting',
        ),
        languageIndependent=1,
        schemata="Registration",
        multiValued=1,
        relationship="registration_form",
        searchable=1,
        allowed_types=['File','Document','Meeting Document','Signup Sheet']
    ),

    TextField(
        name='travel_hotel',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label="Accomodation Information",
            description="Information about accomodation for the meeting",
            label_msgid="meeting_label_accomodation_information",
            description_msgid="meeting_help_accomodation_information",
            i18n_domain='meeting',
        ),
        default_output_type='text/html',
        schemata="Travel and Accomodation",
        searchable=1
    ),

    TextField(
        name='travel_visa',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label="Travel Information",
            description="Information on travel and visa requirements",
            label_msgid="meeting_label_travel_information",
            description_msgid="meeting_help_travel_information",
            i18n_domain='meeting',
        ),
        default_output_type='text/html',
        schemata="Travel and Accomodation",
        searchable=1
    ),

    StringField(
        name='photos',
        widget=StringWidget(
            label="Photos",
            description="Link to Photos related to the Meeting",
            label_msgid="meeting_label_photos",
            description_msgid="meeting_help_photos",
            i18n_domain='meeting',
        ),
        validators = ('isURL',),
        schemata="Photos",
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Meeting_schema = getattr(ATFolder, 'schema', Schema(())).copy() + \
    getattr(ATEvent, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
# Meeting Details
#schemata = "Meeting Details"
#Meeting_schema['title'].schemata = schemata
#Meeting_schema['description'].schemata = schemata
#Meeting_schema['text'].schemata = schemata
#Meeting_schema['eventUrl'].schemata = schemata
#Meeting_schema['type'].schemata = schemata
#Meeting_schema['contactPhone'].schemata = schemata
#Meeting_schema['contactEmail'].schemata = schemata
#Meeting_schema['contactName'].schemata = schemata
#Meeting_schema['startDate'].schemata = schemata
#Meeting_schema['endDate'].schemata = schemata
#Meeting_schema['country'].schemata = schemata
#Meeting_schema['location'].schemata = schemata
# Metadata
Meeting_schema['id'].schemata = 'metadata'
Meeting_schema['relatedItems'].schemata = 'metadata'
Meeting_schema['subject'].required = 0
Meeting_schema['endDate'].languageIndependent = 1
Meeting_schema['startDate'].languageIndependent = 1
Meeting_schema['subject'].widget.visible = {"edit": "invisible", "view": "invisible"}
Meeting_schema['attendees'].required = 0
Meeting_schema['attendees'].widget.visible = {"edit": "invisible", "view": "invisible"}
#Meeting_schema['remoteUrl'].required = 0
#Meeting_schema['remoteUrl'].widget.visible = {"edit": "invisible", "view": "invisible"}
Meeting_schema['relatedItems'].required = 0
# Main/Frontpage
Meeting_schema['text'].widget.label = 'Announce'
Meeting_schema['description'].widget.label = 'Summmary'

# Move Stuff Around
Meeting_schema.moveField('country', after='endDate')
Meeting_schema.moveField('type', after='location')

##/code-section after-schema

class Meeting(ATFolder, ATEvent):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(ATFolder,'__implements__',()),) + (getattr(ATEvent,'__implements__',()),)
    # zope3 interfaces
    interface.implements(IMeeting)

    # This name appears in the 'add' box
    archetype_name = 'Meeting'

    meta_type = 'Meeting'
    portal_type = 'Meeting'
    allowed_content_types = ['MeetingDocumentCollection', 'MeetingDocument', 'SignupSheet', 'Folder', 'File'] + list(getattr(ATFolder, 'allowed_content_types', [])) + list(getattr(ATEvent, 'allowed_content_types', []))
    filter_content_types = 1
    global_allow = 1
    content_icon = 'meeting.png'
    immediate_view = 'base_view'
    default_view = 'meeting_summary'
    suppl_views = ()
    typeDescription = "Meeting"
    typeDescMsgId = 'description_edit_meeting'

    _at_rename_after_creation = True

    schema = Meeting_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(Meeting, PROJECTNAME)
# end of class Meeting

##code-section module-footer #fill in your manual code here
def createMeetingCollectionsAfterCreation(document, events, **kwargs):
    """ hardcoded, UNEP specific
         way of pre adding document collections
         eventually you will be able to preset
        collection types.
    """
    for item in document_types:
        #if it already exists then skip it
        if item[0] in document.objectIds():
            pass
        # if it doesn't exist make it
        else:
            document.invokeFactory(id=item[0], title=item[1], type_name='MeetingDocumentCollection')
            

##/code-section module-footer



