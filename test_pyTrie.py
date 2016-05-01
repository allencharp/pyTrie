
from pyTrie import PyTrie

import unittest

class TestPyTrie(unittest.TestCase):

	def setUp(self):
		pass

	def test_pytrie_add(self):
		pytrie = PyTrie()
		pytrie.add("abc")
		self.assertEquals(pytrie.root.nodes[0].key, 'a')
		self.assertEquals(pytrie.root.nodes[0].nodes[0].nodes[0].nodes[0].key, '')
		self.assertEquals(pytrie.root.nodes[0].nodes[0].key, 'b')
		pytrie.add("abd")
		self.assertEquals(pytrie.root.nodes[0].nodes[0].nodes[1].key, 'd')

	def test_pytrie_get(self):
		pytrie = PyTrie()
		pytrie.add("abc")
		pytrie.add("abd")
		pytrie.add("a")
		pytrie.add("bbb")
		for path in pytrie.get("a"):
			self.assertIn(path, ["a","abc","abd"])
		for path in pytrie.get('bbbb'):
			self.assertEqual('a', 'b')  # we could not step into here....

	def test_pytrie_delete(self):
		pytrie = PyTrie()
		pytrie.add("abcd")
		pytrie.add("abdd")
		pytrie.add("a")
		pytrie.add("bbbd")
		for path in pytrie.get("a"):
			self.assertIn(path, ["a","abcd","abdd"])
		pytrie.delete("abcd")
		for path in pytrie.get("a"):
			self.assertIn(path, ["a","abdd"])

	def test_pytrie_general(self):
		pytrie = PyTrie()
		with open("sample.txt") as f:
			for line in f.readlines():
				for word in line.split(' '):
					pytrie.add(word)

		for i in pytrie.get("s"):
			print i
			#self.assertEqual(i, "Google")


if __name__ == '__main__':
	unittest.main()


