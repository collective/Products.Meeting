from Products.ATVocabularyManager.config import TOOL_NAME as ATVOCABULARYTOOL
from Products.CMFCore.utils import getToolByName

document_types = (
('working documents',u'working documents'),
('information documents',u'information documents'),
('conferencepapers',u'conference papers'),
('reference documents',u'reference documents'),
('presentations',u'presentations'),
('finalreports',u'final reports'),
) 

def createSimpleVocabs(portal, simpleVocabDictionary):
    """
    creates simple ATVM vocabularies out of tuples stored in the dictionary
    simpleVocabDictionary.    
    code taken from http://plone.org/documentation/tutorial/archgenxml-getting-started/vocabulary-manager
    
    """

    atvm = getToolByName(portal, ATVOCABULARYTOOL)
    
    for vkey in simpleVocabDictionary.keys():
        # create vocabulary if it doesn't exist:
        vocabname = vkey
        if not hasattr(atvm, vocabname):
            # print >>out, "adding vocabulary %s" % vocabname
            atvm.invokeFactory('SimpleVocabulary', vocabname)
        vocab = atvm[vocabname]
        for (ikey, value) in simpleVocabDictionary[vkey]:
            if not hasattr(vocab, ikey):
                vocab.invokeFactory('SimpleVocabularyTerm', ikey)
                vocab[ikey].setTitle(value)   
                

def createHierarchicalVocabs(portal, hierarchicalVocabDictionary):
    """
    creates TreeVocabularyTerms out of dictionaries 

    """
    atvm = getToolByName(portal, ATVOCABULARYTOOL)
      
    #if hasattr(atvm, 'regions'):        
        # delete it to get (possibly) new version installed
        #atvm.manage_delObjects(['regions',])

    
    def createVocabularyTerms(vocabulary, id, title, subDictionary):
        """
        vocabulary    the TreeVocabulary(Term) to operate on
        id,title      the new terms title and id
        subDictionary a (maybe empty) dictionary containing (termId, termTitle) keys with dictionaries again.
        
        creates a new term within vocabulary and recursively
        checks whether there are subvocabularies to create
        """
        if not hasattr(vocabulary, id):
            vocabulary.invokeFactory('TreeVocabularyTerm', id, title=title)
        
        newTerm = vocabulary[id]
      
        
        for key, value in subDictionary.iteritems():
            createVocabularyTerms(newTerm, key[0], key[1], value)
        
    
    
    for vkey in hierarchicalVocabDictionary.keys():
        # create vocabulary if it doesn't exist:
        vocabname = vkey

        if not hasattr(atvm, 'vehicles'):#vocabname[0]):  
            # just to be sure, normally vocabulary is created in Install.py    
            atvm.invokeFactory('TreeVocabulary', vocabname[0], title=vocabname[1])
        
        # new terms will be created, title changes in dictionary won't affect
        # existing terms
        vocab = atvm[vocabname[0]]
        
        
        for (id, title), value in hierarchicalVocabDictionary[vkey].iteritems():
            if not hasattr(vocab, id):
                createVocabularyTerms(vocab, id, title, value)                                                             
                  
