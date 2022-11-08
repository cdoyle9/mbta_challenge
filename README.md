This repo is a solution to a coding challenge involving the MBTA API.


## Usage
This program can be run by entering `python main.py` from the root directory.  This runs the
program with the default settings to solve all 3 problems for subway routes.  The program
can be run with command line arguments to specify only certain problems to run, i.e.
`python main.py --problem-3`.  Rail types may be passed in as comma-separated values in a string
using `--rail-types` to run the solutions for different rail lines.  For example, 
`python main.py --rail-types 'Light Rail, Bus'`. The options are 'Light Rail', 'Heavy Rail', 
'Commuter Rail', 'Bus', and 'Ferry'.  Finally, the `--trip` option can be used to pass a start 
and end destination to Problem 3, and it will try to find a route or series of routes connecting 
the two stops. For example, `python main.py --trip 'Chestnut Hill to Broadway'` will return 
`Green Line D / Red Line`.

** If you want to use an api key for the MBTA API, you must add it to a `.env` file as `API_KEY`
and then run `source .env` **


## Testing
The code can be tested by running `python -m unittest test` from the root directory.  The unit tests
cover various inputs to all three problems, including valid and invalid data.  Individual problems
can be tested with the format `python -m unittest test.TestProblem1`, and individual tests with the
format `python -m unittest test.TestProblem1.test_mock_data`


## Problem 1
Problem 1 asks for the names of all subway routes, which are classified as 'light rail' and 
'heavy rail' in the API. The solution is a simple api call to /routes filtering on light and
heavy rail types.  The decision was made to ask the api to filter the results because only
the filtered data is needed.  Additionally, the api returns data as a string, which needs to
be parsed and processed.  Only returning the needed data eliminates unnecessary processing
of extra data.


## Problem 2
Problem 2 asks for the routes with the most and least stops, as well as the names of all stops
where two or more routes intersect.  To solve this problem and Problem 3, a graph structure is
created that links all relevant routes and stops after querying for the data.  In the process, it
also links all routes that intersect, which simplifies the work for Problem 3.  It is trivial
to find the routes with the most and least stops after each route is given a dictionary with
its respective stops.  It is also simple to generate a list of all stops where two or more
routes intersect, by searching for all stops linked to two or more routes. 


## Problem 3
Problem 3 asks for a function that can take two stops as input, and output a series of routes 
that someone could take to get from one stop to the other.  It is solved with a breadth-first search
algorithm run on the route graph.  Starting from the first stop as the root node, it searches each
route associated with that stop to see if they include the destination stop. If a route is not found
to contain the destination, all of its intersecting routes (except the routes already traversed to
reach that point) are queued for the same search.  This repeats until a solution is found or all 
layers have been traversed.  This causes the algorithm to search though all possible connecting
routes while avoiding going in an infinite circle.  The first route found that includes the
destination causes that route's path to be returned as a probable ideal solution.  Breadth-first 
search is preferable to depth-first because it is more likely to return the smallest number of
connecting routes.  Someone travelling from Ashmont to Arlington would probably much rather take the 
Red Line to the Green B Line, than take the Red Line to Orange to Blue and then to Green.



