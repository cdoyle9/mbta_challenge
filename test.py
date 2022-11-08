import unittest

from src.test.utils import MockController
from main import problem1, problem2, problem3


class TestProblem1(unittest.TestCase):
  """
  A class to hold tests for Problem 1
  """

  @classmethod
  def setUpClass(cls) -> None:
    cls.mockController = MockController()
    return super().setUpClass()


  def test_mock_data(self):
    """
    Tests that problem1 retrieves the names of test data
    """

    solution, error = problem1(self.mockController, types=['test'])

    self.assertEqual(error, None)
    self.assertIn('test1', solution)
    self.assertIn('test2', solution)
    self.assertIn('test3', solution)


  def test_default_case(self):
    """
    Tests the default logic of problem1, which is to retrieve the names of all subway lines
    """

    solution, error = problem1(self.mockController)

    self.assertEqual(error, None)
    self.assertIn('Red Line', solution)
    self.assertIn('Mattapan Trolley', solution)
    self.assertIn('Orange Line', solution)
    self.assertIn('Green Line B', solution)
    self.assertIn('Green Line C', solution)
    self.assertIn('Green Line D', solution)
    self.assertIn('Green Line E', solution)
    self.assertIn('Blue Line', solution)


  def test_light_rail(self):
    """
    Tests that problem1 only returns heavy rail names when specified
    """

    solution, error = problem1(self.mockController, types=['Heavy Rail'])

    self.assertEqual(error, None)
    self.assertIn('Red Line', solution)
    self.assertIn('Orange Line', solution)
    self.assertIn('Blue Line', solution)


  def test_commuter_rail(self):
    """
    Tests that problem1 can retrieve the names of commuter rail lines
    """

    solution, error = problem1(self.mockController, types=['Commuter Rail'])

    self.assertEqual(error, None)
    self.assertIn('Fairmount Line', solution)    
    self.assertIn('Fitchburg Line', solution)
    self.assertIn('Framingham/Worcester Line', solution)
    self.assertIn('Franklin/Foxboro Line', solution)
    self.assertIn('Greenbush Line', solution)
    self.assertIn('Haverhill Line', solution)
    self.assertIn('Kingston Line', solution)
    self.assertIn('Lowell Line', solution)
    self.assertIn('Middleborough/Lakeville Line', solution)
    self.assertIn('Needham Line', solution)
    self.assertIn('Newburyport/Rockport Line', solution)
    self.assertIn('Providence/Stoughton Line', solution)
    self.assertIn('Foxboro Event Service', solution)


  def test_types_error(self):
    """
    Test error handling for invalid rail type
    """

    misspelled_rail = 'Light Railasdfaadfs'

    solution, error = problem1(self.mockController, types=[misspelled_rail])

    self.assertEqual(solution, None)
    self.assertEqual(str(error), f"Invalid rail type: '{misspelled_rail}'")


class TestProblem2(unittest.TestCase):
  """
  A class to hold tests for Problem 2
  """

  @classmethod
  def setUpClass(cls) -> None:
    cls.mockController = MockController()
    return super().setUpClass()


  def test_mock_data(self):
    """
    Tests that problem2 can find the most and least stops as well as intersections from
    a small set of test data
    """

    solution, error = problem2(self.mockController, types=['test'])

    self.assertEqual(error, None)
    self.assertIn("The route(s) with the most stops: ['test1'] with 6 stops", solution[0])
    self.assertIn("The route(s) with the least stops: ['test2'] with 4 stops", solution[1])
    self.assertIn("stopA is an intersection for routes: test1, test2", solution)
    self.assertIn("stopB is an intersection for routes: test1, test3", solution)
    self.assertIn("stopF is an intersection for routes: test2, test3", solution)


  def test_default_case(self):
    """
    Tests the default run of problem2, which is to find the subway routes with the most and least
    stops, as well as all stops where two or more routes intersect
    """

    solution, error = problem2(self.mockController)

    self.assertEqual(error, None)
    self.assertIn("The route(s) with the most stops: ['Green Line D'] with 25 stops", solution[0])
    self.assertIn("The route(s) with the least stops: ['Mattapan Trolley'] with 8 stops", solution[1])
    self.assertIn("Park Street is an intersection for routes: Red Line, Green Line B, Green Line C, Green Line D, Green Line E", solution)
    self.assertIn("Downtown Crossing is an intersection for routes: Red Line, Orange Line", solution)
    self.assertIn("Ashmont is an intersection for routes: Red Line, Mattapan Trolley", solution)
    self.assertIn("State is an intersection for routes: Orange Line, Blue Line", solution)
    self.assertIn("Haymarket is an intersection for routes: Orange Line, Green Line D, Green Line E", solution)
    self.assertIn("North Station is an intersection for routes: Orange Line, Green Line D, Green Line E", solution)
    self.assertIn("Government Center is an intersection for routes: Green Line B, Green Line C, Green Line D, Green Line E, Blue Line", solution)
    self.assertIn("Boylston is an intersection for routes: Green Line B, Green Line C, Green Line D, Green Line E", solution)
    self.assertIn("Arlington is an intersection for routes: Green Line B, Green Line C, Green Line D, Green Line E", solution)
    self.assertIn("Copley is an intersection for routes: Green Line B, Green Line C, Green Line D, Green Line E", solution)
    self.assertIn("Hynes Convention Center is an intersection for routes: Green Line B, Green Line C, Green Line D", solution)
    self.assertIn("Kenmore is an intersection for routes: Green Line B, Green Line C, Green Line D", solution)
    self.assertIn("Science Park/West End is an intersection for routes: Green Line D, Green Line E", solution)


  def test_types_error(self):
    """
    Test error handling for invalid rail type
    """

    misspelled_rail = 'Light Railasdfaadfs'

    solution, error = problem2(self.mockController, types=[misspelled_rail])

    self.assertEqual(solution, None)
    self.assertEqual(str(error), f"Invalid rail type: '{misspelled_rail}'")


class TestProblem3(unittest.TestCase):
  """
  A class to hold tests for Problem 3
  """

  @classmethod
  def setUpClass(cls) -> None:
    cls.mockController = MockController()
    return super().setUpClass()


  def test_mock_data_1(self):
    """
    Tests that a single route is returned as the path from A to D
    """
    trip = 'stopA to stopD'

    solution, error = problem3(self.mockController, trip, types=['test'])

    self.assertEqual(error, None)
    self.assertEqual(solution, ['test1'])


  def test_mock_data_2(self):
    """
    Tests that the algorithm can find the intersecting route to map a path from A to M
    """
    trip = 'stopA to stopM'

    solution, error = problem3(self.mockController, trip, types=['test'])

    self.assertEqual(error, None)
    self.assertEqual(solution, ['test1', 'test3'])

  
  def test_mock_data_3(self):
    """
    Tests that the algorithm still returns only a single route for this path, even though the
    single path isn't queued first in the search algorithm.  Essentially tests that breadth-first
    search is working.
    """
    trip = 'stopA to stopF'

    solution, error = problem3(self.mockController, trip, types=['test'])

    self.assertEqual(error, None)
    self.assertEqual(solution, ['test2'])


  def test_example1(self):
    """
    Test answer for a path from Davis to Kendall/MIT
    """
    trip = 'Davis to Kendall/MIT'

    solution, error = problem3(self.mockController, trip, types=['Light Rail', 'Heavy Rail'])

    self.assertEqual(error, None)
    self.assertEqual(solution, ['Red Line'])


  def test_example2(self):
    """
    Test answer for a path from Ashmont to Arlington
    """
    trip = 'Ashmont to Arlington'

    solution, error = problem3(self.mockController, trip, types=['Light Rail', 'Heavy Rail'])

    self.assertEqual(error, None)
    self.assertEqual(solution, ['Red Line', 'Green Line B'])


  def test_example3(self):
    """
    Test answer for a path from Wedgemere to Kendall/MIT including commuter rail lines
    """

    trip = 'Wedgemere to Kendall/MIT'

    solution, error = problem3(self.mockController, trip, types=['Light Rail', 'Heavy Rail', 'Commuter Rail'])

    self.assertEqual(error, None)
    self.assertEqual(solution, ['Lowell Line', 'Orange Line', 'Red Line'])


  def test_types_error(self):
    """
    Test error handling for invalid rail type
    """

    trip = 'Ashmont to Arlington'
    misspelled_rail = 'Light Railasdfaadfs'

    solution, error = problem3(self.mockController, trip, types=[misspelled_rail])

    self.assertEqual(solution, None)
    self.assertEqual(str(error), f"Invalid rail type: '{misspelled_rail}'")


  def test_stop_error(self):
    """
    Test error handling for invalid rail type
    """

    invalid_stop = 'asdf'
    trip = f'{invalid_stop} to North Station'

    solution, error = problem3(self.mockController, trip)

    self.assertEqual(solution, None)
    self.assertEqual(str(error), f"Stop '{invalid_stop}' was not found")



if __name__ == '__main__':
    unittest.main()
    