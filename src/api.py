import requests
import json
from functools import cache

from src.constants import base_url, api_key

class MBTA_api:
  """
  This class is a minimal wrapper around the MBTA API that exposes a few
  request methods for convenience. It holds the api key and automatically
  adds it to each request.
  """

  def __init__(self):
    self._base_url = base_url
    self._api_key = api_key


  @cache
  def get_routes(self, filter):
    """
    Constructs a GET request to the routes endpoint
    """
    url = self._base_url + '/routes'

    return self._get_request(url, filter)


  @cache
  def get_stops(self, filter):
    """
    Constructs a GET request to the stops endpoint
    """
    url = self._base_url + '/stops'

    return self._get_request(url, filter)

   
  def _get_request(self, url, filter):
    """
    A generic function that takes a url and optional filter and makes a GET
    request using the api token
    """

    if filter:
      url = url + f'?{filter}'

    headers = None
    if self._api_key:
      headers = {
        'x-api-key': self._api_key
      }

    response = requests.get(url, headers)

    data = json.loads(response.text)

    return data['data']
