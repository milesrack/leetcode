#!/usr/bin/env python3

class Node:
	def __init__(self):
		self.children = {}
		self.end = False

class Trie:

	def __init__(self):
		self.trie = Node()

	def insert(self, word: str) -> None:
		temp = self.trie
		for i in range(len(word)):
			if word[i] not in temp.children:
				temp.children[word[i]] = Node()
			temp = temp.children[word[i]]
		temp.end = True

	def search(self, word: str) -> bool:
		temp = self.trie
		for i in range(len(word)):
			if word[i] not in temp.children:
				return False
			temp = temp.children[word[i]]
		return temp.end

	def startsWith(self, prefix: str) -> bool:
		temp = self.trie
		for i in range(len(prefix)):
			if prefix[i] not in temp.children:
				return False
			temp = temp.children[prefix[i]]
		return True
