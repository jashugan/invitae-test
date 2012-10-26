from collections import OrderedDict
from xml.etree.ElementTree import Element

class Node(Element):

    def __repr__(self):
        return "<Node '{}' at {}>".format(self.tag, id(self))

    def __eq__(self, other):
        return (
            self.tag == other.tag and
            self._compare_text(other) and
            self.tail == other.tail and
            self.attrib == other.attrib and
            list(self) == list(other))
    
    def _compare_text(self, other):
        if self.text and other.text:
            return self.text.strip() == other.text.strip()
        return self.text == other.text


class XMLMerger(object):

    @staticmethod
    def merge(roots):
        roots_by_tag_attrib = OrderedDict()
        for root in roots:
            attrib = tuple(sorted(
                [(k,v) for k,v in root.attrib.items()], 
                lambda a,b: cmp(a[0], b[0])))
            key = (root.tag, root.text, attrib)
            roots_by_tag_attrib.setdefault(key, []).extend(list(root))
        new_roots = []
        for tag, text, attrib in roots_by_tag_attrib:
            new_root = Node(tag, dict(attrib))
            new_root.text = text
            new_root.extend(XMLMerger.merge(
                roots_by_tag_attrib[(tag, text, attrib)]))
            new_roots.append(new_root)
        return new_roots