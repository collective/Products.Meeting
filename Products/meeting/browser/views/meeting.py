from zope.interface import implements
from DateTime import DateTime
from plone.memoize.instance import memoize

from Products.CMFCore.utils import getToolByName
from Products.CMFPlone import utils
from Products.Five import BrowserView
from Products.meeting.browser.interfaces import IMeetingSummary,IMeetingDocuments

class MeetingSummary(BrowserView):
    implements(IMeetingSummary)

    def __init__(self, context, request, *args, **kw):
        super(MeetingSummary,self).__init__(context, request, *args, **kw)
        utool = getToolByName(context, 'portal_url')
        self.portal_url = utool()
        # this has a messed up context, but we don't care in this case
        self.portal = utool.getPortalObject()

    @memoize
    def meeting_contents(self,type=None):
        """
          returns the contents of a meeting
          can filter out specific types from the meeting e.g. meeting_contents(type='SignupSheet')
          will return the SignupSheet.
        """
        context = self.context
        
        portal_catalog = getToolByName(context, 'portal_catalog')
        if type == None:
            query = {
                     'portal_type':['MeetingDocumentCollection','SignupSheet'],
                 }
        else:
            query = {'portal_type':type,
                 }

        # ensure that the query is only done within the current meeting
        # by adding a path parameter
        query['sort_on'] = 'getObjPositionInParent' 
        if context.Type() == 'Meeting Document Collection':
            query['path'] = {'query' : '/'.join(context.aq_parent.getPhysicalPath()),
                                                 'depth' : 1}
        else:
            query['path'] = {'query' : '/'.join(context.getPhysicalPath()),
                                                 'depth' : 1}
        

        return portal_catalog(query)

    @memoize
    def meeting_documents(self):
        """
         returns meeting documents with their corresponding codes
        """
        meeting_docs = self.getDocuments
        return meeting_docs

    @memoize
    def country_name(self,value=''):
        """ get the country by name """
        context = self.context
        ctool = getToolByName(context, 'portal_countryutils')
        countryname = ctool.getCountryByIsoCode(context.getCountry()).name
        return countryname

    @memoize
    def full_location(self,value=''):
        """ combine country and location to generate location """
        context = self.context
        location = "%s, %s" % (context.getLocation(),self.country_name())
        return location

    @memoize
    def collections(self):
        context = self.context
        collections = context.listFolderContents(contentFilter={"portal_type" : "MeetingDocumentCollection"})
        return collections

    @memoize
    def collections_with_docs(self):
        """ return the collections that have documents """
        collections = self.collections()
        collections_with_docs = [item.id for item in collections if len(item['documents']) > 0]
        return collections_with_docs


    @memoize
    def collection_docs(self,collection):
        """ return the documents for a given collection """
        return collection.getDocuments

class MeetingDocuments(BrowserView):
    implements(IMeetingDocuments)

    def __init__(self, context, request, *args, **kw):
        super(MeetingDocuments, self).__init__(context, request, *args, **kw)
        utool = getToolByName(context, 'portal_url')
        self.portal_url = utool()
        # this has a messed up context, but we don't care in this case
        self.portal = utool.getPortalObject()
                                            
