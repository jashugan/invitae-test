from unittest import TestCase
from StringIO import StringIO

from merger import XMLMerger, Node

class NodeTestCase(TestCase):

    def test_equal_to_similar_node(self):
        node1 = Node('my_tag', {'my_attr': 'my_val'})
        node1.append(Node('my_child'))
        node2 = Node('my_tag', {'my_attr': 'my_val'})
        node2.append(Node('my_child'))
        self.assertEqual(node1, node2)

    def test_equal_to_node_with_same_children(self):
        node1 = Node('my_tag')
        node1.append(Node('my_child1'))
        node2 = Node('my_tag')
        node2.append(Node('my_child1'))
        self.assertNotEqual(node1, node2)

    def test_not_equal_to_node_with_different_children(self):
        node1 = Node('my_tag')
        node1.append(Node('my_child1'))
        node2 = Node('my_tag')
        node2.append(Node('my_child2'))
        self.assertNotEqual(node1, node2)

    def test_whitespace_is_ignored_in_text(self):
        node1 = Node('my_tag')
        node1.text = 'Hello\n\n'
        node2 = Node('my_tag')
        node2.text = 'Hello'
        self.assertEqual(node1, node2)


class XMLMergerTestCase(TestCase):

    def test_merge_two_root_nodes_with_no_overlap(self):
        root1 = Node('variants')
        root1.append(Node('variant', {'attr1': 'test'}))

        root2 = Node('variants')
        root2.append(Node('variant'))

        expected_root = Node('variants')
        expected_root.extend([
            Node('variant', {'attr1': 'test'}), Node('variant')])

        self.assertEqual(XMLMerger.merge([root1, root2]), [expected_root])

    def test_merge_two_root_nodes_with_overlap(self):
        roots = []
        for snp_name in ('snp_a', 'snp_b'):
            root = Node('variants')
            var = Node('variant', {'attr1': 'test'})
            snp = Node(snp_name)
            var.append(snp)
            root.append(var)
            roots.append(root)

        expected_root = Node('variants')
        var = Node('variant', {'attr1': 'test'})
        for snp_name in ('snp_a', 'snp_b'):
            snp = Node(snp_name)
            var.append(snp)
        expected_root.append(var)

        self.assertEqual(XMLMerger.merge(roots), [expected_root])