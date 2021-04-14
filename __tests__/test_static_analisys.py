import unittest
from src.translation_finder import find_translations_in_string

class TestStaticAnalisys(unittest.TestCase):
    def test_it_raises_an_exepction_when_the_useTranslation_is_not_initialized(self):
        with self.assertRaises(BaseException) as context:
            find_translations_in_string("t('lol')")

        self.assertTrue("The translations are not initialized" in str(context.exception))

    def test_is_returns_a_translation_within_a_string(self):
        result = find_translations_in_string("""
        const { t } = useTranslation('product');
        ...
        {t('lol')}
        ...
        {t('xpto')}
        """)

        self.assertTrue(len(result) == 2)

    def test_get_namespace_from_t_func(self):
        result = find_translations_in_string("""
        const { t } = useTranslation();
        ...
        {t('test.lol')}
        """)

        self.assertTrue(len(result) == 1)
        self.assertEqual('test', result[0].namespance)

    def test_get_chained_key(self):
        result = find_translations_in_string("""
        const { t } = useTranslation();
        ...
        {t('test.foo.bar')}
        """)

        self.assertTrue(len(result) == 1)
        self.assertEqual('test', result[0].namespance)
        self.assertEqual('foo.bar', result[0].key)

    def test_get_with_default_namespace(self):
        result = find_translations_in_string("""
        const { t } = useTranslation();
        ...
        {t('bar')}
        """, "test")

        self.assertTrue(len(result) == 1)
        self.assertEqual('test', result[0].namespance)
        self.assertEqual('bar', result[0].key)

if __name__ == '__main__':
    unittest.main()