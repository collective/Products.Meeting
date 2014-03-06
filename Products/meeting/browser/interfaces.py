from zope.interface import Interface, Attribute


class IMeetingSummary(Interface):
    """ Meeting Summary"""

    def meeting_contents():
        """Finds the contents of the meeting
        """
    def country_name():
        """ get the country by name """

    def full_location():
        """ combine country and location to generate location """

class IMeetingDocuments(Interface):
    """ Meeting Documents"""

