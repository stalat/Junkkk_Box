import unittest
from add import add
class TestMath(unittest.TestCase):
	def test_add_two_numbers(self):
		result=add(10,1)
		print result
		assert 11==result
		print "Test Case 1 is executed successfully"

	def test_add_strings(self):
		result=add("User","Case")
		print result
		assert "UserCase"==result
		print "Test Case 2 is executed successfully"

	def test_add_lists(self):
		result=add(["Hello"],["Talat"])
		print result
		assert ['Hello','Talat']==result
		print "Test Case 3 is executed successfully"

	if __name__ == '__main__':
		unittest.main()
