from Products.meeting.Extensions.utils import createSimpleVocabs
from Products.meeting.Extensions.utils import document_types
from StringIO import StringIO
from Products.CMFCore.utils import getToolByName

#define simple vocabularies
vocabs = {}
vocabs['meeting_types'] = (
  ("CEP - IGM",u'CEP - IGM'),
  ("CEP - MONCOM",u'CEP - MONCOM'),
  ("SPAW - ISTAC",u'SPAW - ISTAC'),
  ("SPAW - Workshop",u'SPAW - Workshop'),
  ( "SPAW - COP",u'SPAW - COP'),
  ("SPAW - STAC",u'SPAW - STAC'),
  ("LBS - ISTAC",u'LBS - ISTAC'),
  ("LBS - Workshop",u'LBS - Workshop'),
        )

vocabs['document_types'] = document_types

#(
#('attachments',u'attachments'),
#('conferencepapers',u'conferencepapers'),
#('presentations',u'presentations'),
#('reference documents',u'reference documents'),
#('information documents',u'information documents'),
#('working documents',u'working documents'),
#) 

def install(portal):
    """
    install scripts for meeting product
    """
    out = StringIO()

    #turn of folder creation
    #mt = getToolByName(portal,'portal_membership')#.getPortalObject()
    #mt.memberareaCreationFlag = 0
    # add meeting portlet to the top of right slots
    #portal = getToolByName(portal,'portal_url').getPortalObject()
    #for slot in ['here/meeting_portlet/macros/portlet']:
    #   if slot not in portal.right_slots:
    #       portal.right_slots = [slot] + list(portal.right_slots)

    #setup vocabs
    #createHierarchicalVocabs(portal,meetingHierarchicalVocabs)
    createSimpleVocabs(portal,vocabs)
    #setPloneProperties(portal,out)

    return out.getvalue()



def uninstall(portal):
    """
    undo the settings made in install
    """
    pass
