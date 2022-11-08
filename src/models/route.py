

class Route:
  """
  A simplified model of a MBTA route containing only the information needed to
  solve the challenges
  """

  def __init__(self, id, name):
    self.id = id
    self.name = name
    self.stops = {}
    self.intersections = {}


