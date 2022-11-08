from src.test.fixtures import routes_data, stops_data
from src.constants import rail_type_map
from src.models import Route, Stop

rail_type_map['test'] = -1


class MockController():
  """
  A controller that exposes methods that return mock data.  This is much more convenient to
  use in testing, as it eliminates the need for slow API calls. 
  """

  def get_routes(self, types):
    """
    Provides mock data comparable to what the api would return for testing purposes
    """

    rail_types = []
    for type in types:
      try:
        rail_types.append(rail_type_map[type])
      except KeyError as e:
        raise ValueError(f'Invalid rail type: {e}')

    routes = []
    for route in routes_data:
      if route['type'] in rail_types:
        routes.append(Route(
          id=route['id'],
          name=route['name']
        ))

    return routes


  def get_stops(self, route_ids):
    """
    Provides mock data comparable to what the api would return for testing purposes
    """

    data = []
    for route in route_ids:
      data = [*data, *stops_data[route]]
      
    stops = []
    for stop in data:
      stops.append(Stop(
        id=f'{stop}',
        name=f'{stop}'
      ))

    return stops