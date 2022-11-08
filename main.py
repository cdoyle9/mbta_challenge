import argparse

from src.utils import create_graph, get_intersecting_stops, calculate_valid_routes
from src.controller import Controller


parser = argparse.ArgumentParser(description='Answer questions about the MBTA system')
parser.add_argument('--problem-1', dest='problem1', action='store_true', default=None,
                    help='Run problem 1')
parser.add_argument('--problem-2', dest='problem2', action='store_true', default=None,
                    help='Run problem 2')
parser.add_argument('--problem-3', dest='problem3', action='store_true', default=None,
                    help='Run problem 3')
parser.add_argument('--rail-types', dest='rail_types', action='store', default='Light Rail, Heavy Rail',
                    help='Comma-separated rails types to filter on')
parser.add_argument('--trip', dest='trip', action='store', default='Ashmont to Arlington',
                    help='A trip of the format "Stop A to Stop B" to calculate a route for')


# Part 1
def problem1(controller, types=['Light Rail', 'Heavy Rail']):
  """
  Answers the question, 'Retrieve data representing all subway routes and print their long names'
  Uses the controller to call the api with a filter for Light Rail and Heavy Rail.  The filter
  is used with the api call rather than using logic to filer on all results because the data is 
  returned as a string and needs to be processed.  Having the api filter beforehand eliminates
  unnecessary processing this program would have to do otherwise.

  @param {Controller} controller - A wrapper around the api client used to make queries to the MBTA api
  @param {string[]} types - The types of rail line to filter for. By default filters for subway routes

  @returns An array containing the names of all the routes found.
  """
  print('Running problem 1...')

  try:
    answer = []

    # Get all routes of specified type.  Default value searches for subway routes.
    routes = controller.get_routes(types=types)

    # Solution: The name of each rail line
    for route in routes:
      answer.append(route.name)

    return answer, None

  except ValueError as error:
    return None, error


# Part 2
def problem2(controller, types=['Light Rail', 'Heavy Rail']):
  """
  Answers the questions:
  2.1 Find the subway route with the most stops
  2.2 Find the subway route with the least stops
  2.3 Find all stops that connect two or more subway routes and print the relevant names

  @param {Controller} controller - A wrapper around the api client used to make queries to the MBTA api
  @param {string[]} types - The types of rail line to filter for.  By default filters for subway routes

  @returns An array containing the answers to all parts of the question
  """
  print('Running problem 2...')

  try:
    answer = []

    most_stops = None
    most_stops_route = ''
    least_stops = None
    least_stops_route = ''

    # Get subway routes
    routes = controller.get_routes(types=types)

    # Get routes and corresponding stops linked together
    stop_map = create_graph(controller.get_stops, routes)
      
    # Find the routes with most and least stops
    for route in routes:

      num_stops = len(route.stops)
      # Check if route has the most stops so far
      if most_stops is None or num_stops > most_stops:
        most_stops = num_stops
        most_stops_route = [route]
      elif num_stops == most_stops:
        most_stops_route.append(route)

      # Check if route has the fewest stops so far
      if least_stops is None or num_stops < least_stops:
        least_stops = num_stops
        least_stops_route = [route]
      elif num_stops == least_stops:
        least_stops_route.append(route)


    # Part 2.1: The route with the most stops
    answer.append(f'The route(s) with the most stops: {[r.name for r in most_stops_route]} with {len(most_stops_route[0].stops)} stops')

    # Part 2.2: The route with the least stops
    answer.append(f'The route(s) with the least stops: {[r.name for r in least_stops_route]} with {len(least_stops_route[0].stops)} stops')

    # Part 2.3: Find all stops where two or more routes intersect
    # Create a list of all stops where two or more routes intersect
    intersecting_stops = get_intersecting_stops(stop_map)

    # Find all stops with multiple intersecting routes
    for stop in intersecting_stops:

      routes_string = ""
      for route in stop.routes.keys():
        routes_string = routes_string + route + ', '
      routes_string = routes_string[0:-2]

      answer.append(f'{stop.name} is an intersection for routes: {routes_string}')

    return answer, None

  except ValueError as error:
    return None, error



# Part 3
def problem3(controller, trip, types=['Light Rail', 'Heavy Rail']):
  """
  Provides functionality for allowing the user to specify any two stops on any subway route and list
  a route you could travel to get from one stop to the other.

  @param {Controller} controller - A wrapper around the api client used to make queries to the MBTA api
  @param {string} trip - A string of the format "Stop A to Stop B"
  @param {string[]} types - The types of rail line to filter for.  By default filters for subway routes

  @returns An array containing the rails in the order you would take them to get from the first stop to the next.
  """
  print('Running problem 3...')

  try:
    answer = []

    routes = controller.get_routes(types=types)

    stop_map = create_graph(controller.get_stops, routes)

    # Gets the first valid route or series of routes from point A to point B
    solution = calculate_valid_routes(trip, stop_map)

    answer = [r.name for r in solution]

    return answer, None

  except ValueError as error:
    return None, error



if __name__ == '__main__':

  args = parser.parse_args()

  # Determine which problems to run
  commands = [args.problem1, args.problem2, args.problem3]
  run_all = False

  # If no specific problem was specified, run all by default
  if all(c == None for c in commands):
    run_all = True

  # Parse rail types argument
  if args.rail_types:
    rail_types = [s.strip() for s in args.rail_types.split(',')]
  
  
  # Initialize controller to handle data from API
  controller = Controller()

  # Run Problem 1 if specified
  if run_all or args.problem1:
    answer1, error1 = problem1(controller, rail_types)

    if error1:
      print(f'Error: {error1}')
    else:
      print()
      print('Problem 1: The names of the specified route types')
      for a in answer1:
        print(a)
    print('\n')


  # Run Problem 2 if specified
  if run_all or args.problem2:
    answer2, error2 = problem2(controller, rail_types)

    if error2:
      print(f'Error: {error2}')
    else:
      print()
      print('Solution 2.1: Route(s) with the most stops')
      print(answer2[0])
      print()

      print('Solution 2.2: Route(s) with the least stops:')
      print(answer2[1])
      print()

      print('Solution 2.3: All stops where two or more routes intersect:')
      for a in answer2[2:-1]:
        print(a)
    print('\n')


  # Run Problem 3 if specified
  if run_all or args.problem3:
    answer3, error3 = problem3(controller, args.trip, rail_types)

    print()
    print('Solution 3: Valid routes')
    if error3:
      print(f'Error: {error3}')
    else:
      print(' / '.join(answer3))
