
from lxml import etree

from moai.utils import XPath

class ExampleContent(object):
    def __init__(self, provider):
        self.provider = provider
        self.id = None
        self.modified = None
        self.deleted = None
        self.sets = None
        self.metadata = None

    def update(self, path):
        doc = etree.parse(path)
        xpath = XPath(doc, nsmap={'x':'http://example.org/data'})
        
        self.root = doc.getroot()

        id = xpath.string('//x:id')
        self.id = 'oai:grains-%s' % id
        self.modified = xpath.date('//x:modified')
        self.deleted = False

        self.metadata = {
                         'title': [xpath.string('//x:title')],
                         'identifier': xpath.strings('//x:identifier'),
                         'subject': xpath.strings('//x:subject'),
                         'language': xpath.strings('//x:language'),
                         'type': xpath.strings('//x:type'),
                         'relation': xpath.strings('//x:relation'),
                         'date': xpath.strings('//x:issued')}
        
        self.sets = {u'stout': {u'name':u'stout',
                                  u'description':u'metabolic set'}}