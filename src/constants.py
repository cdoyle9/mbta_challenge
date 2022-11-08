import os

base_url = 'https://api-v3.mbta.com'
api_key = os.getenv('API_KEY')
rail_type_map = {
  'Light Rail': 0,
  'Heavy Rail': 1,
  'Commuter Rail': 2,
  'Bus': 3,
  'Ferry': 4
}
