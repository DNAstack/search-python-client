import unittest

from search_python_client.search import DrsClient, SearchClient


class TestDrsClient(unittest.TestCase):
    def setUp(self):
        url = 'https://drs.covidcloud.ca/ga4gh/drs/v1/'
        self.drs_client = DrsClient(url)

    def test_object_info(self):
        object_id = '0000bee7-6e47-4e0c-b3e4-9e574eac508b'
        object_info = self.drs_client.object_info(object_id)
        self.assertEqual(object_info.loc['id', 'object'], object_id)


class TestSearchClient(unittest.TestCase):
    def setUp(self):
        url = 'https://ga4gh-search-adapter-presto-covid19-public.prod.dnastack.com/'
        self.search_client = SearchClient(url=url)

    def test_list_tables(self):
        tables = self.search_client.list_tables()
        self.assertGreaterEqual(len(tables), 1)

    def test_table_info(self):
        table_name = 'coronavirus_dnastack_curated.coronavirus.annotations'
        table_info = self.search_client.table_info(table_name)
        self.assertEqual(table_info.loc['description', 'name'], table_name)

    def test_table_data(self):
        table_name = 'coronavirus_dnastack_curated.coronavirus.annotations'
        table_data = self.search_client.table_data(table_name, 10)
        self.assertGreaterEqual(len(table_data), 1)

    def test_search_table(self):
        table_name = 'coronavirus_dnastack_curated.coronavirus.annotations'
        query = f'SELECT * FROM {table_name} LIMIT 100'
        table_data = self.search_client.search_table(query)
        self.assertGreaterEqual(len(table_data), 1)


if __name__ == '__main__':
    unittest.main()
