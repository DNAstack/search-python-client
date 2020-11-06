import unittest

from search_python_client.search import SearchClient


class TestSearchFunctions(unittest.TestCase):

    def test_ga4gh_get_drs(self):
        id = '0000bee7-6e47-4e0c-b3e4-9e574eac508b'
        drs_data  = ga4gh_get_drs(id)
        self.assertEqual(drs_data['id'], id)

    def test_ga4gh_search_db(self):
        query = 'SELECT * FROM coronavirus_dnastack_curated.covid_cloud_production.sequences_view LIMIT 5'
        meta_data  = ga4gh_search_db(query)
        self.assertEqual(len(meta_data), 5)

if __name__ == '__main__':
    unittest.main()
