import re
import os
from unittest import TestCase
from xml.etree import ElementTree

from api import merge
from merger import Node


class ParseAndMergeTestCase(TestCase):

    def setUp(self):
        self.files = [
            open('xml_files/{}'.format(f)) for f in os.listdir('xml_files') if 
            f.startswith('in')]

    def tearDown(self):
        for handle in self.files:
            handle.close()

    def test_returns_merged_xml_file_like_object(self):
        merged_file = merge(self.files)
        expected_file = open('xml_files/out.xml')
        self.assertEqual(
            self._nodify(ElementTree.parse(merged_file).getroot()),
            self._nodify(ElementTree.parse(expected_file).getroot()))

    @classmethod
    def _nodify(cls, root):
        new_root = Node(root.tag, root.attrib)
        new_root.text = root.text
        new_root.extend([
            cls._nodify(child) for child in root])
        return new_root