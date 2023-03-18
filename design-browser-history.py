#!/usr/bin/env python3
class History:
	def __init__(self, url):
		self.url = url
		self.back = None
		self.forward = None

class BrowserHistory:

	def __init__(self, homepage: str):
		self.recent = History(homepage)

	def visit(self, url: str) -> None:
		temp = History(url)
		temp.back = self.recent
		self.recent.forward = temp
		self.recent = temp

	def back(self, steps: int) -> str:
		temp = self.recent
		for i in range(steps):
			if temp.back != None:
				temp = temp.back
		self.recent = temp
		return self.recent.url

	def forward(self, steps: int) -> str:
		temp = self.recent
		for i in range(steps):
			if temp.forward != None:
				temp = temp.forward
		self.recent = temp
		return self.recent.url
