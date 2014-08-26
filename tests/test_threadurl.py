import unittest
from threadurl import ThreadUrl
from os.path import dirname

class testThreadUrl(unittest.TestCase):

	def setUp(self):
		self.threadurl = ThreadUrl()
		self.threadurl.load()

	def test_url_list(self):
		urls = ['http://linuxextreme.org','http://renanvicente.com']
		self.threadurl.trigger(urls)

	def test_url_list_from_file(self):
		urls = open(dirname(realpath(__file__)) + '/test_file.txt','r')
		self.threadurl.trigger(urls)
		
	def test_method(self):
		urls = ['http://linuxextreme.org','http://renanvicente.com']
		self.method = "HEAD"
		self.threadurl.trigger(urls)

	def test_verbose(self):
		import sys
		from StringIO import StringIO

		self.threadurl.verbose = True
		url = ['http://renanvicente.com']
		saved_stdout = sys.stdout
		try:
			out = StringIO()
			sys.stdout = out
			self.threadurl.trigger(url)
			output = out.getvalue().strip()
			assert output == "(200, 'http://renanvicente.com')"
		finally:
			sys.stdout = saved_stdout


if __name__ == '__main__':
	unittest.main()
