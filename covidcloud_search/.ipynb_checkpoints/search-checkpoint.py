import os
import requests

from typing import List, Union


default_drs_url = 'https://drs.covidcloud.ca/ga4gh/drs/v1/objects/'
default_search_url = 'https://ga4gh-search-adapter-presto-covid19-public.prod.dnastack.com/search'

def ga4gh_get_drs(
    query: str = '',
    url: str = default_drs_url,
) -> Union[List[dict], dict]:
    
    """
    Get DRS from DNAstack's covidcloud
    
    :param query: DRS ID. Leave '' to get all drs data.
    :param url: API url

    :return: Json response/s in dict format

    Example:
    url = 'https://drs.covidcloud.ca/ga4gh/drs/v1/objects/'
    query = '0000bee7-6e47-4e0c-b3e4-9e574eac508b'
    drs_data  = ga4gh_get_drs(query, url)
    """
    
    extended_url = os.path.join(url, query)
    response = requests.get(extended_url)
    
    if response.status_code == 200:
        if query:
            return response.json()['object']
        else:
            return response.json()['objects']
    
    else:
        return response.status_code
    

def ga4gh_search_db(
    query: str,
    url: str = default_search_url
) -> List[dict]:

    """
    Returns list formatted ga4gh search response from a url and query

    :param query: SQL query
    :param url: API url
    
    :return: Json response/s in dict format

    Example:
    url = 'https://ga4gh-search-adapter-presto-covid19-public.prod.dnastack.com/search'
    query = {'query': 'SELECT * FROM coronavirus_dnastack_curated.covid_cloud_production.sequences_view'}
    meta_data  = ga4gh_search_db(query, url)

    """

    response = requests.post(url, json=query)
    
    if response.status_code == 200:
        response_url = response.json()['pagination']

        data = []
        while response_url:
            response = requests.get(response_url['next_page_url'])
            
            if response.status_code == 200:
                data += response.json()['data']
                response_url = response.json()['pagination']
            
            else:
                return response.status_code

        return data
    
    else:
        return response.status_code