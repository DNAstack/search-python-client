import unittest

from search_python_client.search import DrsClient, SearchClient


class TestDrsClient(unittest.TestCase):
    def setUp(self):
        self.base_url = 'https://drs.covidcloud.ca/ga4gh/drs/v1/'

    def test_get_object_info(self):
        self.drs_client = DrsClient(self.base_url)
        object_id = '0000bee7-6e47-4e0c-b3e4-9e574eac508b'
        object_info = self.drs_client.get_object_info(object_id)
        self.assertEqual(object_info.id.values[0], object_id)

    def test_get_object_info_auth(self):
        self.drs_client = DrsClient(self.base_url, auth=('user', 'pass'))
        object_id = '0000bee7-6e47-4e0c-b3e4-9e574eac508b'
        object_info = self.drs_client.get_object_info(object_id)
        self.assertEqual(object_info.id.values[0], object_id)

    def test_get_object_info_wallet(self):
        self.drs_client = DrsClient(self.base_url, wallet=123)
        object_id = '0000bee7-6e47-4e0c-b3e4-9e574eac508b'
        object_info = self.drs_client.get_object_info(object_id)
        self.assertEqual(object_info.id.values[0], object_id)


class TestSearchClient(unittest.TestCase):
    def setUp(self):
        base_url = 'https://ga4gh-search-adapter-presto-covid19-public.staging.dnastack.com'
        self.search_client = SearchClient(base_url=base_url)

    def test_get_table_list(self):
        tables_iterator = self.search_client.get_table_list()
        tables = [next(tables_iterator, None) for i in range(10)]
        tables = list(filter(None, tables))
        self.assertEqual(len(tables), 10)

    def test_get_table_info(self):
        table_name = 'coronavirus_dnastack_curated.covid_cloud_staging.annotations'
        table_info = self.search_client.get_table_info(table_name)
        self.assertEqual(table_info.loc['description', 'name'], table_name)

    def test_get_table_data(self):
        table_name = 'coronavirus_dnastack_curated.covid_cloud_staging.annotations'
        table_data_iterator = self.search_client.get_table_data(table_name)
        table_data = [next(table_data_iterator, None) for i in range(10)]
        table_data = list(filter(None, table_data))
        self.assertEqual(len(table_data), 10)

    def test_search_table(self):
        table_name = 'coronavirus_dnastack_curated.covid_cloud_staging.annotations'
        query = f'SELECT * FROM {table_name} LIMIT 100'
        table_data_iterator = self.search_client.search_table(query)
        table_data = [next(table_data_iterator, None) for i in range(10)]
        table_data = list(filter(None, table_data))
        self.assertEqual(len(table_data), 10)


if __name__ == '__main__':
    unittest.main()
