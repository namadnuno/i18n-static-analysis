import json
import unittest

from src.json_reader import get_translation_in_json
from src.translation_finder import find_translations_in_string

class TestJSONReader(unittest.TestCase):
    def test_it_returns_the_translations_keys_of_json(self):
        content = json.loads("""
        {
            "test": "random"
        }
        """)
        translations_keys = get_translation_in_json(content, "namespace");

        self.assertTrue("namespace.test" in translations_keys)

    def test_it_returns_the_namespaced_translations_keys(self):
        content = json.loads("""
        {
            "test": "random",
            "test1": {
                "in": "lol"
            }
        }
        """)
        translations_keys = get_translation_in_json(content, "namespace");

        self.assertTrue("namespace.test1.in" in translations_keys)

if __name__ == '__main__':
    unittest.main()