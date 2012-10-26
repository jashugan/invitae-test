import re
import os
from unittest import TestCase
from api import merge

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
            re.sub(r'\s+', '', merged_file.read()), 
            re.sub(r'\s+', '', expected_file.read()))