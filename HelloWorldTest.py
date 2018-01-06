import unittest
import sys, io
from unittest.mock import patch

class TestHelloWorld(unittest.TestCase):

	@patch('builtins.input', return_value="Hello World")
	def test_HelloWorld(self, sth):
		try:
			out = io.StringIO()
			sys.stdout = out
			import HelloWorld
			output = out.getvalue().strip()
			assert output == 'Hello World'
		finally:
			pass

if __name__ == "__main__":
    unittest.main()
