class TrieNode:
	def __init__(self):
		self.children = {}
		self.word = False

class WordDictionary:

	def __init__(self):
		self.root = TrieNode()

	def addWord(self, word: str) -> None:
		cur = self.root
		for i in range(len(word)):
			if word[i] not in cur.children:
				cur.children[word[i]] = TrieNode()
			cur = cur.children[word[i]]
		cur.word = True

	def search(self, word: str) -> bool:
		def search_helper(node, index):
			if index == len(word):
				return node.word
			elif word[index] in node.children:
				return search_helper(node.children[word[index]], index + 1)
			elif word[index] == '.':
				for child in node.children.values():
					if search_helper(child, index + 1):
						return True
			return False

		return search_helper(self.root, 0)
