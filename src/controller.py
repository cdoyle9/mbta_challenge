from src.models import Route, Stop
from src.api import MBTA_api
from src.constants import rail_type_map


class Controller:
  """
  The controller is a wrapper around the API that manages parsing and transformation of data.
  Here, queries passed in are formatted for the api, and json data returned from api requests
  is converted into model classes for simplification and convenience.
  """

  def __init__(self):
    self.api = MBTA_api()

  def get_routes(self, types=None):
    '''
    Queries API for all routes of the specified types

    @param {string[]} types - Rail types to filter on such as "Light Rail", "Heavy Rail", etc
    '''
    print(f'Getting routes of type {types}...')

    # Convert types into query paramter
    type_filter = ""
    if types:
      type_filter = "filter[type]="

      # Convert rail type to corresponding code
      for type in types:
        try:
          type_filter = type_filter + str(rail_type_map[type]) + ','
        except KeyError as e:
          raise ValueError(f'Invalid rail type: {e}')

      # Remove trailing comma
      type_filter = type_filter[0:-1]


    data = self.api.get_routes(type_filter)


    # Format the data into a more easily usable shape
    routes = []
    for route in data:
      r = Route(
        id= route['id'],
        name=route['attributes']['long_name']
      )
      routes.append(r)

    return routes


  def get_stops(self, route_ids=None):
    '''
    Queries the API for all stops associated with the route ids passed in

    @param {string[]} route_ids - An array of route ids
    '''
    print(f'Getting stops for routes {route_ids}...')

    # Create routes query paramter
    route_filter = ""
    if route_ids:
      route_filter = "filter[route]="

      # Add routes to filter
      for route_id in route_ids:
        route_filter = route_filter + route_id + ','

      # Remove trailing comma
      route_filter = route_filter[0:-1]


    data = self.api.get_stops(route_filter)


    # Format the data into a more easily usable shape
    stops = []
    for stop in data:
      s = Stop(
        id=stop['id'],
        name=stop['attributes']['name']
      )
      stops.append(s)

    return stops
