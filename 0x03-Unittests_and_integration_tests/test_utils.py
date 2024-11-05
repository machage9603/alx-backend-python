
#!/usr/bin/env python3
"""
Test utils
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import patch, Mock

class TestAccessNestedMap(unittest.TestCase):
	"""_summary_

	Args:
					unittest (_type_): _description_
	"""

	@parameterized.expand(
		[
			({"a": 1}, ("a",), 1),
			({"a": {"b": 2}}, ("a",), {"b": 2}),
			({"a": {"b": 2}}, ("a", "b"), 2)
		]
	)
	def test_access_nested_map(self, nested_map, path, expected_output):
		"""_summary_
		"""
		result = access_nested_map(nested_map, path)
		self.assertEqual(result, expected_output)

	@parameterized.expand(
		[
			({}, ("a",), KeyError),
			({"a": 1}, ("a", "b"), KeyError)
		]
	)
	def test_access_nested_map_exception(self, nested_map, path, expected_output):
		"""_summary_
		"""
		with self.assertRaises(expected_output) as context:
			access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
	"""_summary_

	Args:
		unittest (_type_): _description_
	"""
	@parameterized.expand(
		[
			('http://example.com', {'payload': True}),
			('http://holberton.io', {'payload': False})
		]
	)
	def test_get_json(self, url, expected_output):
		"""_summary_
		"""
		mock_response = Mock()
		mock_response.json.return_value = expected_output
		with patch('requests.get', return_value=mock_response):
			response = get_json(url)

			self.assertEqual(response, expected_output)