import os
from xml.etree import ElementTree
from StringIO import StringIO

from merger import XMLMerger


def merge(files):
    parsed = []
    for handle in files:
        parsed.append(ElementTree.parse(handle).getroot())
    xml_out = StringIO()
    merged = XMLMerger.merge(parsed)
    if merged:
        xml_out.write(ElementTree.tostring(merged[0]))
        xml_out.seek(0)
    return xml_out