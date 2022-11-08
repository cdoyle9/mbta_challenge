from collections import deque


def create_graph(get_stops, routes):
  """
  This function accepts a map of routes and then queries the api for all stops
  associated with each route.  Stop objects are created for each stop and linked
  to their respective Route objects.  When duplicate stops are found, the routes
  are linked via their intersections fields.

  @param routes - A list of routes

  @returns the updated routes and a map of all stops for those routes
  """
  print('Linking routes...')

  # Initialize a map to hold all stops
  stop_map = {}

  for route in routes:
    # Get stops for each route
    route_stops = get_stops(route_ids=[route.id])

    # Iterate over every stop in this route
    for stop in route_stops:
      name = stop.name

      # Link the route and the stop
      route.stops[name] = stop
      stop.routes[route.name] = route

      # Check if this stop has been seen before in another route
      if name in stop_map:

        # If found, link all routes to each other as intersections
        for r in stop_map[name].routes.values():
          r.intersections[route.name] = route
          route.intersections[r.name] = r

        # link this route to current stop
        stop_map[name].routes[route.name] = route

      # Otherwise, add this stop to the map of stops
      else:
        stop_map[name] = stop

  return stop_map



def get_intersecting_stops(stop_map):
  """
  Returns a list of stops where two or more routes intersect
  """
  intersecting_stops = []
  for stop in stop_map.values():
    if len(stop.routes) > 1:
      intersecting_stops.append(stop)

  return intersecting_stops



def calculate_valid_routes(trip, stop_map):
  """
  This function calculates the routes to take in order to fulfil the trip passed in.
  It works by using a graph of linked routes and stops and performing a breadth-first search
  on the first stop passed in with the trip parameter.
  
  @param trip - A string specifying a start and end destination, i.e. Davis to Kendall/MIT
  @param stop_map - A map of all stops of interest linked to their corresponding routes

  @returns A list of routes that someone could take to get from the start point to the destination.
  """
  print(f'Calculating valid routes for {trip}...')

  parts = trip.split(' to ')

  # Check that a start and stop destination was provided
  if len(parts) != 2:
    raise ValueError('Invalid trip input.  Must be in the format of "Stop1 to Stop2"')

  start = parts[0]
  end = parts[1]

  q = deque()

  try:
    start_routes = stop_map[start].routes
    end_routes = stop_map[end].routes
  except KeyError as e:
    raise ValueError(f'Stop {e} was not found')

  # Initialize queue with all routes associated with the first stop
  for route in start_routes.values():
    q.append((route, []))

  
  # Breadth-first search for a route associated with the destination stop
  while len(q) > 0:
    current_route, visited_routes = q.popleft()
    visited_routes.append(current_route)

    # Solution
    if current_route.name in end_routes:
      return visited_routes

    # Keep searching
    else:
      for route in current_route.intersections.values():

        # Add new route to the queue only if it hasn't been visited yet to prevent traversing infinitely in a circle
        if route not in visited_routes:
          q.append((route, [*visited_routes]))

  raise ValueError('No route found')
